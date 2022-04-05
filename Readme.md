# Challenge 1: Sighting data visualisation

## Task 1: Collect information through API.
For collecting data from an API thinking of utilising an express server. The express server to get the data from the s3 storage on AWS. Then also thinking about deploying my express server on an EC2 Instance.

## Task 2: Wrangle data. 

For wrangling the data I would like to utilise python for my cleaning process, to read in the csv files and as well as plot the values to a heat-map.

### Steps taken in cleaning the Data:
+ Remove unnecessary columns
+ Remove rows of data that do not have lon/lat data
+ Remove duplicate rows 
+ Speeds of -1 are impossible (My thought maybe speeds can be of -1 you never know haha) so will make those 0 just to make them uniform as to the ones that have a 0.0 
+ After some reading the previous point is invalid for an Accelerometer can read negative speeds. Look at link used for explanation: [Accelerometer-Explanation](https://www.sciencebuddies.org/science-fair-projects/references/accelerometer)

## Task 3: Plot on any mapping tool to create a heat map

The tool I used is called [Folium](https://python-visualization.github.io/folium/) A tool that did exactly what i required which was spitting out an HTML page of the plotted data into heat maps. 

Then I also as added an extra step to have a python script (startProcess.py) that did task 1 and 2. I then wanted for this data to be hosted so i built the express-server that would execute the startProcess.py script. The data produced by the python script (Heat-maps folder) would then be available to the iOS application via an endpoint I added to the express server.

Steps to produce the heat-maps on your local-machine:

- Step 1: make sure all required python libraries are installed.
- Step 2: make sure you have installed all npm modules.
- Step 3: You have the option of just running the startProcess.py script without the server.
  -Step 3.1: This will then generate 3 folders: sightings_alerts (Which has the csv files from the s3 storage), CleanedCSVFiles (The wrangled data), and finally Heat-maps (Contains the generated HTMLpages of the different heat maps).
- Step 4: Running the server locally and using postman to hit the /htmlFiles endpoint to get back html string data of the heat-maps. This also does create the folders that step 3.1 creates.
- For any further assistance do not hesitate to ask!

## Task 4: 

Challenges faced would be firstly trying to understand the data for it was my first time ever working with such data. A lot of reading was required to try and figure out how acceleration was a -1 value haha, Also the process of cleaning data and also plotting it on a heat-map with the use of python. The other challenge was not being able to use elastic beanstalk to deploy my node.js server. The reasons to this was because my node.js had some python aspect so i had to manually setup an environment that contains both node and python. Then also setting up the node.js server to always run even after leaving the ec2 with the use of [PM2](https://pm2.keymetrics.io). This allowed for the node.js server to startup even when the server restarts. These where challenges i enjoyed facing cause I got to learn more in-terms of BLE devices an how the vitality Drive functionality goes about working.




# Challenge 2: Sighting data exploration

After trying to figure out what the whole challenge is about I had a few questions to clarify what needs to be done and if i can go above what is being asked of me and i had the pleasure of being acquainted to Devin Norman. He answered all my questions and clarified a few things as to what i was doing if i was heading in the right direction or not. Just a thanks to him and to add on he did speak praises of the Telematics department haha. 

Now as for this challenge i utilised a python script called: statisticalProcess.py that generated different graphs and results with regards to what I found interesting.

The things that i found interesting was if the number of devices and the most popular hours when the devices where at their highest.
I noticed in the csv files that they only contained data for two months being January and February. So this is what i based my statistical study on. If you do check the files generated in the heat-maps, they are separated by the months.

I am not a statistics expert and due to time did not want to focus on reading up on the different types of method. Though the route i took to exploring the data was through visualisation like below:

### Data Set 1:
<img src="https://github.com/Khondwani/Challenge1-2/blob/e1504806694cb2f95eda975655e7dc045f33ae44/4cb82c20117b.png" /> 

In this data set i am looking at the file 4cb82c20117b.csv and as describe in the image above we have a rise in the number of devices in February. This to interpretation can me that multiple users started moving around more in February or discovery insure gained more user. This activity was mostly noticed in the area of Sandton as shown in the heat-maps.

### Data Set 2:
<img src="https://github.com/Khondwani/Challenge1-2/blob/e1504806694cb2f95eda975655e7dc045f33ae44/4cb82c2383ad.png" /> 

This is the total opposite of the image above. I looked at the heat-map and this data was collected from the area of Glenhazel in Johannesburg. It shows January had a higher rate of devices and February lower. 

From these two data sets i had a-lot of thoughts including the heat-maps that most of these heat signatures where usually around places like malls, parks, ,schools and gas stations. This was an interesting fact that people with these devices most must have children due to the high heat signature around schools or be teachers. I could also pickup which shopping place was most visited or the most used gas station due to the heat-maps. 

The other investigation i worked on was seeing which was the most popular hours in the two separate areas. 

### Data Set 1:
<img src="https://github.com/Khondwani/Challenge1-2/blob/e1504806694cb2f95eda975655e7dc045f33ae44/PopularHours4cb82c20117b.png" /> 

So in the area 4cb82c20117b.csv (Sandton) the most popular hours where at 9 that is when we had the most devices being read in January and in February that value reduced to 5. This could show that most of these people that pass these beacons at 5 in the morning are people possibly going to work.

### Data Set 2: 
<img src="https://github.com/Khondwani/Challenge1-2/blob/e1504806694cb2f95eda975655e7dc045f33ae44/PopularHours4cb82c2383ad.png" /> 

It this data set, the most popular time in this area in January was 13 as compared to the previous area the popular hour was 9. This tells me this area is more of a residential place cause the hour 13 is usually when people either head out for lunch or back home. Tho that is just my assumption. In February the most popular hour was 5 just like the previous area.




# [Back To Home](https://github.com/Khondwani/DiscoveryChallenges)
# [Go To Challenge 3 Build iOS Application](https://github.com/Khondwani/DiscoveryiOSChallenge)
