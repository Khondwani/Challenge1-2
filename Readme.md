# Challenge 1: Sighting data visualisation

## Task 1: Collect information through API.
For collecting data from an API thinking of utilising an express server. The express server to get the data from the s3 storage on AWS. Then also thinking about deploying my express server on an EC2 Instance.

## Task 2: Wrangle data. 

For wrangling the data I would like to utilise python for my cleaning process, to read in the csv files and as well as plot the values to a heatmap.

### Steps taken in cleaning the Data:
+ Remove unnecessary columns
+ Remove rows of data that do not have lon/lat data
+ Remove duplicate rows 
+ Speeds of -1 are impossible (My thought maybe speeds can be of -1 you never know haha) so will make those 0 just to make them uniform as to the ones that have a 0.0 
+ After some reading the previous point is invalid for an Accelerometer can read negative speeds. Look at link used for explanation: [Accelerometer-Explanation](https://www.sciencebuddies.org/science-fair-projects/references/accelerometer)

## Task 3: Plot on any mapping tool to create a heat map

The tool I used is called [Folium](https://python-visualization.github.io/folium/) A tool that did exactly what i required which was spitting out an HTML page of the plotted data into heat maps. 

Then I also as added an extra step to have a python script (startProcess.py) that did task 1 and 2. I then wanted for this data to be hosted so i built the express-server that would execute the startProcess.py script. The data produced by the python script (Heatmaps folder) would then be avaible to the iOS application via an endpoint I added to the express server.

Steps to produce the heatmaps on your localmachine:

- Step 1: make sure all required python libraries are installed.
- Step 2: make sure you have installed all npm modules.
- Step 3: You have the option of just running the startProcess.py script without the server.
  -Step 3.1: This will then generate 3 folders: sightings_alerts (Which has the csv files from the s3 storage), CleanedCSVFiles (The wrangeld data), and finally Heatmaps (Contains the generated HTMLpages of the different heat maps).
- Step 4: Running the server locally and using postman to hit the /htmlFiles endpoint to get back html string data of the heatmaps. This also does create the folders that step 3.1 creates.
- For any further assistance do not hesitate to ask!

## Task 4: 

Challenges faced would be firstly trying to understand the data for it was my first time ever working with such data. A lot of reading was required to try aand figure out how acceleration was a -1 value haha, Also the process of cleaning data and also ploting it on a heatmap with the use of python. The other challenge was not being able to use elastic beanstalk to deploy my node.js server. The reasons to this was because my node.js had some python aspect so i had to manually setup an enviroment that contains both node and python. Then also setting up the node.js server to always run even after leaving the ec2 with the use of [PM2](https://pm2.keymetrics.io). This allowed for the node.js server to startup even when the server restarts. These where challenges i enjoyed facing cause I got to learn more interms of BLE devices an how the vitality Drive functionality goes about working.




# Challenge 2: Sighthing data exploration


# [Back To Home](https://github.com/Khondwani/DiscoveryChallenges)
# [Go To Challenge 3 Build iOS Application](https://github.com/Khondwani/DiscoveryiOSChallenge)
