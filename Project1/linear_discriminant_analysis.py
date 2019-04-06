import numpy as np
from csv import reader
import sys
import csv
import math


def CsvLoadFile(file_name, training=[]):
    load_data = open(file_name, 'r')
    content = csv.reader(load_data)
    data = list(content)
    for part in range(len(data)):
        for entity in range(len(data[part])):
            if (data[part][entity] == 'W'):
                data[part][entity] = 0
            elif (data[part][entity] == 'M'):
                data[part][entity] = 1
            data[part][entity] = float(data[part][entity])
        if 1 == 1:
            training.append(data[part])
        print(training)
    return training


# String values are converted to float
def StringFloatConversion(dataset, col):
    for val in dataset:
        val[col] = float(val[col])


# To generate the random values
def getValuesRandomly(meanValue, cov, number):
    resultant = []
    print(meanValue[0])
    resultant = np.random.multivariate_normal(meanValue, cov, number)
    return resultant


if __name__ == '__main__':
    csv_File_Name = sys.argv[1]
    training_content = []
    Dataset = CsvLoadFile(csv_File_Name, training_content)
    peopleTotal = []
    for val in Dataset:
        peopleTotal.append([val[0], val[1], val[2]])

    for val in range(len(peopleTotal[0])):
        StringFloatConversion(peopleTotal, val)

    men = []
    for val in Dataset:
        if val[3] == 1:
            men.append([val[0], val[1], val[2]])

    for val in range(len(men[0])):
        StringFloatConversion(men, val)

    women = []
    for val in Dataset:
        if val[3] == 0:
            women.append([val[0], val[1], val[2]])

    for val in range(len(women[0])):
        StringFloatConversion(women, val)

    meanWomen = np.mean(np.array(women), axis=0)
    meanMen = np.mean(np.array(men), axis=0)
    meanTotal = np.mean(np.array(peopleTotal), axis=0)

    # Mean
    meanWomenCorr = np.subtract(np.array(women), meanTotal)
    meanMenCorr = np.subtract(np.array(men), meanTotal)

    # Transpose
    meanWomenCorrTrans = np.transpose(meanWomenCorr)
    meanMenCorrTrans = np.transpose(meanMenCorr)

    # Multiplication
    a = np.dot(meanWomenCorrTrans, meanWomenCorr)
    b = np.dot(meanMenCorrTrans, meanMenCorr)

    # Covariance 
    womenCov = np.divide(a, len(women))
    menCov = np.divide(b, len(men))

    
    lenWomen = len(women)
    lenMen = len(men)
    lenPeople = len(peopleTotal)
    womenProb = lenWomen / lenPeople
    menProb = lenMen / lenPeople
    womenCovProb = womenCov * womenProb
    menCovProb = menCov * menProb
    cov = np.add(menCovProb, womenCovProb)
    print("Men: ", menProb)
    print("Women:", womenProb)
    print("People:", lenPeople)

    # Inverse
    invCov = np.linalg.inv(cov)

    # Probability
    matrix = [womenProb, menProb]
    plan = np.log(matrix)

    womenCheck = []
    menCheck = []
    for val in peopleTotal:
        meanWomenCov = np.dot(meanWomen, invCov)
        section1 = np.dot(meanWomenCov, np.transpose(val))
        section2 = 0.5 * np.dot(meanWomenCov, np.transpose(meanWomen))
        total = section1 - section2 + np.log(menProb)
        womenCheck.append(total)

    for val in peopleTotal:
        meanMenCov = np.dot(meanMen, invCov)
        section3 = np.dot(meanMenCov, np.transpose(val))
        section4 = 0.5 * np.dot(meanMenCov, np.transpose(meanMen))
        aggregation = section3 - section4 + np.log(womenProb)
        menCheck.append(aggregation)

    for val in range(len(menCheck)):
        if menCheck[val] > womenCheck[val]:
            print("men")
        else:
            print("women")

    finalMen = getValuesRandomly(meanMen, cov, 50)
    finalWomen = getValuesRandomly(meanWomen, cov, 50)
    print('\nThe random data generated for Men : \n', finalMen)
    print('\nThe random data generated for Women : \n', finalWomen)