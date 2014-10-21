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
    file_headers, file =h.request(filedown)
    file = file.decode()
    print(file)

def splitfile():

    #will ask the user how much of the file they want to use for training and how much for testing.
    print("How much of the file is to be used for training , precentage.\nThe precntage must be greater than 30 and less than 75")

    while(1==1):
        precentage = input("\n:")
        if (precentage <= "30") or (precentage >= "75"):
            print("Error, please enter a number between 30 and 75")
        else:
            break

#downloads file
downloadfile()
splitfile()
