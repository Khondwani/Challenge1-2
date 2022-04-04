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



