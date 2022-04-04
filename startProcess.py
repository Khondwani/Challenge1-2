import os
import pandas as pd # makes it easy to get data from the csv file 
import folium
from folium import plugins
import requests
import requests, zipfile
from io import BytesIO

def generateHtmlMap(lat,lon,mapName):
    # Create the map of guateng
    mapGuateng = folium.Map([-26.270760, 28.112268], zoom_start=11)
    
    # plot heatmap
    folium.plugins.HeatMap(
        list(zip(lat,lon)),
        radius=30,
        blur=20).add_to(mapGuateng)
    plugins.Fullscreen(position='topright').add_to(mapGuateng)
    # Generate Folders for the maps
    if not os.path.isdir(f"Heatmaps"):
        os.mkdir("Heatmaps")
    # Generate an HTML file containing the heatmap
    mapGuateng.save(f"HeatMaps/{mapName}")

def readInFiles(filename):
    # Generate Folders for the processed CSV
    if not os.path.isdir(f"CleanedCSVFiles"):
        os.mkdir("CleanedCSVFiles")
    # Remove duplicates and create new file
    with open("sightings_alerts/"+filename, 'r') as in_file, open('CleanedCSVFiles/RemovedDuplicates'+filename, 'w') as out_file:
        seen = set() # set for fast O(1) amortized lookup
        for line in in_file:
            if line in seen:
                print(line) 
                continue # skip duplicate

            seen.add(line)
            out_file.write(line)

    #Remove rows with 0 values for long/lat coordinates 
    #ReadInNewFile
    data = pd.read_csv('CleanedCSVFiles/RemovedDuplicates'+filename)
    df = pd.DataFrame(data)
    df=df[(df['lat'] != 0) & (df['lon'] != 0)]
    #print(df[(df['lat'] != 0) & (df['lon'] != 0)])
    df.to_csv('CleanedCSVFiles/RemovedRowsWithZeroValues'+filename, index=False)

    bleDevices = pd.read_csv('CleanedCSVFiles/RemovedRowsWithZeroValues'+filename)

    ble_JanuaryData = bleDevices[bleDevices['phoneTime'].str.contains('2018-01')]
    ble_FebruaryData = bleDevices[bleDevices['phoneTime'].str.contains('2018-02')]

    latJan = ble_JanuaryData['lat']
    lonJan = ble_JanuaryData['lon']

    latFeb = ble_FebruaryData['lat']
    lonFeb = ble_FebruaryData['lon']

    latAll = bleDevices['lat']
    lonAll = bleDevices['lon']

    generateHtmlMap(latJan,lonJan, 'januaryResultsMap' + filename.replace(".csv","") +'.html')
    generateHtmlMap(latFeb,lonFeb, 'februaryResultsMap' + filename.replace(".csv","") + '.html')
    generateHtmlMap(latAll,lonAll, 'allResultsMap' + filename.replace(".csv","") + '.html')




def downloadAndExtractFromUrl(s3Url):
   
    # Downloading the file by sending the request to the URL
    req = requests.get(s3Url)
    # Split URL to get the file name
    filename = s3Url.split('/')[-1]

    # extracting the zip file contents
    zipfolder = zipfile.ZipFile(BytesIO(req.content))
    zipfolder.extractall()
    # Get the list of all files and directories
    path = "sightings_alerts"
    obj = os.scandir(path)
    
    # List all files in the specified path
    print("Files and Directories in '% s':" % path)
    for entry in obj:
        if entry.is_file():
            print(entry.name)
            readInFiles(entry.name)



#Request fom url s3 
s3Url = 'https://s3-eu-west-1.amazonaws.com/discovery-insure-interview-rev1/sightings_alerts.zip'
downloadAndExtractFromUrl(s3Url)


