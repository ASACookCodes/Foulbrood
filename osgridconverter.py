import OSGridConverter
import pandas as pd
import os, glob
import sys

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
    


def main():
    #remove the existing CSV if it exists
    files = glob.glob('CSVs/*')
    for f in files:
        os.remove(f)
    
    #Get all datasets and convert to CSVs    
    folder_path = 'datasets'
    for filename in glob.glob(os.path.join(folder_path, '*.txt')):
        with open(filename, 'r') as f:
            filename = os.path.basename(filename)
            name = os.path.splitext(filename)[0] #no file extension
            createCSV(f, name)
            beedata = pd.read_csv(csvpath+name+".csv")
            OScoords = beedata["os"]

            #Convert the OS coords to latitude and longitude and write to the csv file
            latlngs = open(csvpath+name+".csv", "w")
            for coord in OScoords:
                point = str(OSGridConverter.grid2latlong(coord))
                point = point.replace('+','')
                point = point.replace(':',',')
                latlngs.write(point+"\n")
                #print(point)
            latlngs.close() 
    
    # #create web server
    try:
        # Python 2
        from SimpleHTTPServer import test, SimpleHTTPRequestHandler
    except ImportError:
        # Python 3
        from http.server import test, SimpleHTTPRequestHandler

    test(SimpleHTTPRequestHandler)
    
main()

