#OOP Dt211/2 Assignment
# Due Date 30th of November
#Date Given 16th of October 2014
#Title Income Predictor
#Author: Barry Burke
#Student Number :C13427078
#----------------------------------


# Take in file from web. Split the file 60% training set and 40% predict.
#Take the train part and divide it into people who make over $50k and under or equal to $50k

#data file comes from http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data

import string
import httplib2
#download fxn.
def downloadfile():
    #vars that hold url
    filedown= "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
    h = httplib2.Http(".cache")
    file_headers, file =h.request(filedown)# that is working correctly . Header isent being added to file.
    file = file.decode()
    file = file.split('\n')
    for line in file:
        print (line)
    return file

#find out how many entries are in file
def lines(file):#atm print out the number of byets.
    linecounter=0
    for line in file:
        linecounter +=1
    return(int(linecounter))

#split file downloaded into training and testing. Store in a file
def splitfile(file):

    #will ask the user how much of the file they want to use for training and how much for testing.
    print("How much of the file is to be used for training , precentage.\nThe precntage must be greater than 30 and less than 75")

    while(1==1):
        precentage =0
        precentage = float(input("\n:"))
        ##have to make precentage##


        if (precentage < 30) or (precentage > 75):
            print("Error, please enter a number between 30 and 75")
        else:
            break

    try:
        #declare 2 files - training and testing
        training = open("trainfile.txt","w")#opens and creates a file called trainfile.txt in write mode
    except IOError as etraining:
        print(etraining)#gives error to user if cant open
        quit()

    try:
        test = open ("test.txt","w") #opens and creates a file called test .txt in write mode
    except IOError as etest:
        print(etest)#gives error to user if cant open
        quit()

    NumberOfLines = lines(file)
    print(NumberOfLines) #32563 lines

    counter=0
    #find out how many lines go to each file

    precentage =precentage/100
    TrainingEntries = (NumberOfLines*precentage)
    TestingEntries = NumberOfLines-TrainingEntries

    print ("the number of lines that will be used for training is  %d \nand the numbers used as a test will be %d" % (TrainingEntries, TestingEntries))


    #writes file into 2 seperate files, 1 for training and one for testing
    counter =0
    for line in file:
        if(counter<TrainingEntries):
            training.write(line)
            training.write("\n")
            counter= counter+1

        else:
            test.write(line)
            test.write("\n")
    #closes files

    training.close()
    test.close()
    #end of fxn split file

def formatfiletrain():
    try:
        #declare 2 files - training and testing
        training = open("trainfile.txt","r")#opens a file called trainfile.txt in read mode
    except IOError as etraining:
        print(etraining)#gives error to user if cant open
        quit()

    try:
        test = open ("test.txt","r") #opens  a file called test .txt in read mode
    except IOError as etest:
        print(etest)#gives error to user if cant open
        quit()









#downloads file
file=downloadfile()
splitfile(file)
formatfiletrain()


