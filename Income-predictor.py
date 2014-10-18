#OOP Dt211/2 Assignment
# Due Date 30th of Novemeber
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


#vars that hold url
filedown= "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
h = httplib2.Http(".cache")
file_headers, file =h.request(filedown)
file=file.decode().split("\n")

print (file)


