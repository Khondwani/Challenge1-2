## Will use the cleaned data from the CleanedCSV Folder So just make sure that startProcess.py is run before running this ##
import os
import pandas as pd # makes it easy to get data from the csv file 
import matplotlib.pyplot as plt
from datetime import datetime

filenames = ['4cb82c2383ad.csv','4cb82c20117b.csv']

def readInFiles(filename):
   file = pd.read_csv('CleanedCSVFiles/RemovedRowsWithZeroValues'+filename)

   # lets get the total number of devices 
   file_JanuaryData = file[file['phoneTime'].str.contains('2018-01')].copy()
   file_FebruaryData = file[file['phoneTime'].str.contains('2018-02')].copy()

   totalNumberOfDevicesInJan = file_JanuaryData.shape[0]
   totalNumberOfDevicesInFeb = file_FebruaryData.shape[0]

   # Let us generate a bar graph that compares number of devices in the two different months and the two different files
   Months = ['January', 'February']
   NumberOfDevices = [totalNumberOfDevicesInJan,totalNumberOfDevicesInFeb]
   New_Colors = ['green','blue']
   plt.bar(Months, NumberOfDevices, color=New_Colors)
   plt.title('Devices vs Months in: '+filename,fontsize=14)
   plt.xlabel('Months', fontsize=14)
   plt.ylabel('Number Of Devices',fontsize=14)
   plt.show()

   # Find the busiest hours of the day 
   file_JanuaryData['phoneTime'] = pd.to_datetime(file_JanuaryData['phoneTime'])
   resultJan = file_JanuaryData.groupby([pd.Grouper(key='phoneTime',freq='H')]).size().reset_index(name='count')
  
   file_FebruaryData['phoneTime'] = pd.to_datetime(file_FebruaryData['phoneTime'])
   resultFeb = file_FebruaryData.groupby([pd.Grouper(key='phoneTime',freq='H')]).size().reset_index(name='count')

   daysAndTimes = [resultJan.loc[resultJan['count'].idxmax()].phoneTime.hour, resultFeb.loc[resultFeb['count'].idxmax()].phoneTime.hour]
   countOfDevices = [resultJan.loc[resultJan['count'].idxmax()]['count'], resultFeb.loc[resultFeb['count'].idxmax()]['count']]
   New_Colors = ['green','teal']

   plt.bar(daysAndTimes, countOfDevices, color=New_Colors)
   plt.title('Popular hours in: '+filename,fontsize=14)
   plt.xlabel('Time', fontsize=14)
   plt.ylabel('Number Of Devices',fontsize=14)
   plt.show()
   


for filename in filenames:
    readInFiles(filename)