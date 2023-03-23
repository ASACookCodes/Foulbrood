import OSGridConverter
import datetime
import pandas as pd
import os, glob
import sys
import requests
from bs4 import BeautifulSoup

csvpath="CSVs/"

def createCSV(file, name):
    csv = open(csvpath+name+".csv", "a")
    csv.write("area,os,town,number,month\n")
    for line in file:
        line = line.replace(' ','')#FIX THESE TO BE BETTER
        line = line.replace(',','')
        line = line.replace('	',',')
        csv.write(line) 
    csv.close()


def scrapeData(year):
    #Get 2022 dataset and parse using BeautifulSoup 
    source = requests.get('https://www.nationalbeeunit.com/diseases-and-pests/reports-charts-and-maps/disease-incidence/live-efb-report/?year='+year).text
    soup = BeautifulSoup(source, 'html.parser')
    beetable = soup.find("table", class_="table table-bordered table-sm") #Name of the table class
    df = pd.DataFrame(columns=['County', 'OSR', 'Area', 'Number', 'MonthFound'])
    # # Collect ALL the data!
    for row in beetable.find_all('tr'):    
        # Find all data for each column
        columns = row.find_all('td')
    
        if(columns != []):
            county = columns[0].text.strip()
            osr = columns[1].text.strip()
            area = columns[2].text.strip()
            number = columns[3].text.strip()
            month = columns[4].text.strip()
            #df = df.append({'County': county,  'OSR': osr, 'Area': area, 'Number': number, 'MonthFound': month}, ignore_index=True)
            new= pd.DataFrame.from_records([{'County': county,  'OSR': osr, 'Area': area, 'Number': number, 'MonthFound': month}])
            df = pd.concat([df,new], ignore_index=True)
    return df["OSR"]
    
    
def makeWebServer():
    # #create web server
    try:
        # Python 2
        from SimpleHTTPServer import test, SimpleHTTPRequestHandler
    except ImportError:
        # Python 3
        from http.server import test, SimpleHTTPRequestHandler
    test(SimpleHTTPRequestHandler)


def main():
    #remove the existing CSV if it exists
    files = glob.glob('CSVs/*')
    for f in files:
        os.remove(f)

    #Get OS coordinates from BeeBase website for the last five years
    today = datetime.date.today()
    
    for year in range(today.year-5, today.year):
        OScoords = scrapeData(str(year))

        #Convert the OS coords to latitude and longitude and write to a CSV file
        latlngs = open("CSVs/"+str(year)+".csv", "w")
        for coord in OScoords:
            point = str(OSGridConverter.grid2latlong(coord))
            point = point.replace('+','')
            point = point.replace(':',',')
            latlngs.write(point+"\n")
        latlngs.close() 
    
    
main()
makeWebServer()

