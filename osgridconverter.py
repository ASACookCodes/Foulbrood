import OSGridConverter
import pandas as pd
import os
import sys

year = sys.argv[1]

textpath="datasets/"+year
csvpath="CSVs/"+year

def createCSV():
    file = open(textpath+".txt", "r")
    csv = open(csvpath+".csv", "a")
    csv.write("area,os,town,number,month\n")
    for line in file:
        line = line.replace(' ','')#FIX THESE TO BE BETTER
        line = line.replace(',','')
        line = line.replace('	',',')
        csv.write(line) 
    file.close()
    csv.close()
    


def main():
    #remove the existing CSV if it exists
    if os.path.exists(csvpath+".csv"):
        os.remove(csvpath+".csv")
        
    #remove the existing latlng csv if it exists
    if os.path.exists(year+"latlng.csv"):
        os.remove(year+"latlng.csv")
    
    #Transform the text file into a CSV
    createCSV()
    beedata = pd.read_csv(csvpath+".csv")
    OScoords = beedata["os"]

    #Convert the OS coords to latitude and longitude and write to the csv file
    latlngs = open(csvpath+".csv", "w")
    for coord in OScoords:
        point = str(OSGridConverter.grid2latlong(coord))
        point = point.replace('+','')
        point = point.replace(':',',')
        latlngs.write(point+"\n")
        #print(point)
    latlngs.close() 
    
    #create web server
    try:
        # Python 2
        from SimpleHTTPServer import test, SimpleHTTPRequestHandler
    except ImportError:
        # Python 3
        from http.server import test, SimpleHTTPRequestHandler

    test(SimpleHTTPRequestHandler)
    
main()

