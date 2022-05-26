#WORK IN PROGRESS - trying to keep format of txt usable in R. Messing up headers since R comment and markdown headers same. 

#Task 0 - get set up
##A Download and install R studio.
##B Explore the help files:
?rnorm #help query
help.search("rnorm") # 
args(lm) ##gets args

##C Start a new project.r file (TXT versoin of this page shoudl work)
##D CLEAN AND SET YOUR WORKING DIRECTORY
rm(list=ls()) #clean the workspace
getwd() #Where are you now?
setwd("/Users/YOU/Desktop/R/") #Set the directory
list.files() # list files in your working directory
ls() #list variables in current workspace.

#TASK 1 - LOOK AT YOUR DATA
dataframe = read.csv("data.csv") #has to be in your working directory
head(dataframe) #Look at the first few lines
tail(dataframe) #Look at the last few lines 
dim(dataframe) #check all the columns/rows are there. Should be 10 rows and 2 columns
str(dataframe) #check data types.  e.g. student numbers sholud be read as "factor", not integer 

#TASK 2 - Split data into groups and get a summary of each - you will need your own data as copmmands below are spcific to previous project
group1 = dataframe[dataframe$type == "walk OR cycle only", ]
group2 = dataframe[dataframe$type == "train and or bus", ]
summary(dataframe)
summary(group1)
summary(group2)

#TASK 3 - DRAW A BARPLOT
counts = table(dataframe) #count frequency of each answer
barplot(counts, col=c("orange", "red"), main = "Graph Title", xlab = "penguins", ylab="giraffes", beside=TRUE, las = 0)

#TASK 4: FIX THE LABELS AND TITLE
#TASK 5: CHANGE THE COLOUR
#TASK 6: CHANGE "las" from 0 to 1. WHat is the difference?


#TASK 7: Read an INDEPENDENT T-TEST (we're pretending this is a good sample)
t.test(group1$time, group2$time)  

#TASK 8: Interpret - Google "t test table" and confirm that number using the "t" number



