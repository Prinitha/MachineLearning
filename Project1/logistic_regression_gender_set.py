"""
@author: Prinitha Nagarajan
UTA_ID : 1001668557
"""

from math import exp
import csv
import sys

def CsvLoadFile(file_name, training=[]):                             
    load_data = open(file_name, 'r')
    content = csv.reader(load_data)
    data = list(content)
    for part in range(len(data)):
        for entity in range(len(data[part])):
            if(data[part][entity] == 'W'):
                data[part][entity] = 0
            elif(data[part][entity] == 'M'):
                data[part][entity] = 1
            data[part][entity] = float(data[part][entity])
        if 1 == 1:
            training.append(data[part])
    return training

def InputContent(height, weight, age):
    test_content = []
    test_content.insert(0,height)
    test_content.insert(1,weight)
    test_content.insert(2,age)
    return test_content


# Make a prediction with coefficients
def predict(row, coefficients):
	output_notation = coefficients[0]
	for val in range(len(row)-1):
		output_notation += coefficients[val + 1] * row[val]
	return 1.0 / (1.0 + exp(-output_notation))

# Estimate logistic regression coefficients using stochastic gradient descent
def GradientDescentCoeff(training_set, learning_rate, epoch_value):
	coefficients = [0.0 for i in range(len(training_set[0]))]
	for epoch in range(epoch_value):
		err = 0
		for row in training_set:
			output_notation = predict(row, coefficients)
			err = row[-1] - output_notation
			err += err ** 2
			coefficients[0] = coefficients[0] + learning_rate * err * output_notation * (1.0 - output_notation)
			for val in range(len(row)-1):
				coefficients[val + 1] = coefficients[val + 1] + learning_rate * err * output_notation * (1.0 - output_notation) * row[val]
	return coefficients

if __name__ == '__main__': 
    csv_File_Name = sys.argv[1]  
    height = int(sys.argv[2])                                           
    weight = int(sys.argv[3])                                           
    age = int(sys.argv[4])                                        
    training_content = [] 
    test_content = InputContent(height, weight, age)                                              
    myDataset = CsvLoadFile(csv_File_Name, training_content) 
    learning_rate = 0.01
    epoch_value = 100
    coefficients = GradientDescentCoeff(myDataset, learning_rate, epoch_value)
    for row in myDataset:
        output_notation = predict(row, coefficients)
        if(int(round(output_notation)) == 0):
            prediction_gender = 'Woman'
            print("Expected value=%.3f, Predicted value=%.3f [%d] - %s" % (row[-1], output_notation, round(output_notation), prediction_gender))
        elif(round(output_notation) == 1.0):
            prediction_gender = 'Man'
            print("Expected value=%.3f, Predicted value=%.3f [%d] - %s" % (row[-1], output_notation, round(output_notation), prediction_gender))
    value = int(round(predict(test_content, coefficients)))
    print("As per you given height, weight and age:-")
    if(value == 0):
        prediction_gender = 'Woman'
        print("Predicted gender for {} is {}".format(test_content,prediction_gender))
    elif(value == 1):
        prediction_gender = 'Man'
        print("Predicted gender for {} is {}".format(test_content,prediction_gender))
    else:
        print("Invalid input!!! Please try again!!!")