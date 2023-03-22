from js import init, loadMap, createPoint
import asyncio
from js import document, FileReader
from pyodide import create_proxy
 
async def process_file(event):
    init()
    #Retrieve uploaded files
    fileList = event.target.files.to_py()
 
    #Parse uploaded file as string
    for f in fileList:
        data = await f.text()
    #Split into seperate "lat,lng" lines
    coords = data.splitlines()#("\n")
    #Get each lat and lng and create a heat map point from them
    for coord in coords:
        x = coord.split(",")
        createPoint(float(x[0]), float(x[1]))
    
    #Javascript call to load the map
    loadMap()

def main():
	
	# Create a Python proxy for the callback function
	# process_file() processes events from FileReader
    file_event = create_proxy(process_file)
 
	# Set the listener to the callback
    e = document.getElementById("myfile")
    e.addEventListener("change", file_event, False)
   
 
main()

