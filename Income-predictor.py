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
def lines(file):
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


        if (precentage < 0.1) or (precentage > 75):
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


    #place all people in training into a file called training over 50k if over 50k , else put in a file under equal 50k
    try:
        over50k=open("trainover50k.txt","w")
    except IOError as openerrorover50k:
        print(openerrorover50k)
    try:
        lesseq50k=open("trainlesseq50k.txt","w")
    except IOError as openerrorundereq50k:
        print(openerrorundereq50k)

    for line in training:
        for word in line.split(","):
            if ">50K" in word:
                over50k.write(line)
            if "<=50K" in word:
                lesseq50k.write(line)

    #close files
    over50k.close()
    lesseq50k.close()
    #end of fxn

def adveragefxn(listlayout, search):
    #This fxn will recieve the list of how the data is arraged, The call will also send what it wants
    #to find the advearge of.
    #it uses the .isdigt to see if the item is a digt

    #opens the 2 files
    try:
        over50k=open("trainover50k.txt","r")
    except IOError as openerrorover50k:
        print(openerrorover50k)
    try:
        lesseq50k=open("trainlesseq50k.txt","r")
    except IOError as openerrorundereq50k:
        print(openerrorundereq50k)

    #find out what the fxn wants to find the adverage of
    for item in listlayout:
        if item == search:
            numberlookup = listlayout.index(item)#gives item number in list


    searchcounter = 0


    #find last element number




    #over 50k file
    adverageover50k =0
    adveragevalueover50k=0
    adveragecounter=0

    #___________________________________________________________________

    #split file after every comma on file trainover50k
    for line in over50k:
        searchcounter = 0

        for number in line.split(","):

            if searchcounter>13:
                searchcounter=0

            if number.isdigit():
                if searchcounter==numberlookup:
                    adveragevalueover50k = adveragevalueover50k + int(number)
                    adveragecounter=adveragecounter+1
                else:
                    searchcounter=searchcounter+1
            else:
                searchcounter=searchcounter+1




    adverageover50k = adveragevalueover50k/adveragecounter
    print(adverageover50k)
    #____________________________________________________________
    #split file after every comma on file trainundereq50k
    adverageundereq50k=0
    adveragevalueundereq50k=0
    AdverageTotal=0
    adveragecounter=0
    for line in lesseq50k:
        for number in line.split(","):

            if searchcounter>13:
                searchcounter=0

            if number.isdigit():

                if searchcounter==numberlookup:
                    adveragevalueundereq50k =adveragevalueundereq50k + int(number)
                    adveragecounter=adveragecounter+1
                else:
                    searchcounter=searchcounter+1
            else:
                searchcounter=searchcounter+1





    adverageundereq50k = adveragevalueundereq50k/adveragecounter
    print(adverageundereq50k)

    #adverage of adverage
    AdverageTotal = (adverageover50k+adverageundereq50k )/2
    print(AdverageTotal)

    return(AdverageTotal)

#downloads file
listlayout = ["age","workclass","fnlwgt","education","education-no","marital-status","occupation","relationship","race","sex","capital-gain","capital-loss","hours-per-week","native-country","income"]
file=downloadfile()
splitfile(file)
formatfiletrain()
#get adverage age on both over and lesseq files
adverag_age = adveragefxn(listlayout ,"age") #sends list and string called age
adverage_ed_no = adveragefxn(listlayout,"education-no")

#Adverage_ed_no= adveragefxn(listlayout,"education-no")









