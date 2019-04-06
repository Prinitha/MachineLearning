"""
@author: Prinitha Nagarajan
UTA_ID : 1001668557
"""

import numpy as np
import csv
import sys

def CsvLoadFile(file_name, training=[]):            #loaded the CSV file with the given 2 dimensional dataset                  
    load_data = open(file_name, 'r')
     content = csv.reader(load_data)
     data = list(content)
     for part in range(len(data)):
         for entity in range(len(data[part])):
             data[part][entity] = float(data[part][entity])
         if 1 == 1:
             training.append(data[part])

def extract_values(training):                       #separated the data points into x and y values
    x_values=[]
    y_values=[]
    for i in training:
        x_values.append(i[0])
        y_values.append(i[1])
    return x_values, y_values

def x_ValueInsertion(matrix1, n, x_values, y_values, order):    #creating matrix 1 
    sum_x_values = sum(x_values)
    sum_y_values = sum(y_values)
    function_values = [0] * (2*order+1)                         #saves all the powers of x into a list for ease in extraction
    power = 1
    function_values[0] = n
    for j in range(1,len(function_values)):
        total = sum([i ** power for i in x_values])
        function_values[j]=total
        power +=1
    count = 0
    for i in range(len(matrix1)):
        
        for j in range(len(matrix1)):
            if(j==0):
                count = i
            if((i+j) == count):
                matrix1[i][j] = function_values[count]         #insertion of the values in matrix 1
                count +=1
    return matrix1,function_values

def y_ValueInsertion(matrix2, n, x_values, y_values, order, function_values):   #creating matrix 2
    function_y_values = [0] * (order + 1)                   #saves all the powers of y into a list for ease in extraction
    power = 0
    for j in range(0,len(function_y_values)):
        total = 0
        for i in range(len(y_values)):
            total = total + (y_values[i] * (x_values[i] ** power))
        function_y_values[j] = total
        matrix2[j][0]=total                                 #insertion of the values in matrix 2
        power += 1
    return matrix2
    
def MatrixMultiplication(matrix1, matrix2, order):          #matrix multiplication of the inverse matrix 1 and matrix 2
    result = [[0 for x in range(1)] for y in range(order + 1)]
    total = 0
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result
    
def PrintValues(myMatrix):                                  #extracting the values of the parameters
    print("\nThe values of the parameters are:")
    count = 0
    for i in myMatrix:
        print("b{} is: {}".format(count,i))
        #print("{}b{}".format(i,count))
        count +=1
    count = 0
    print("\nThe representation is :")
    for i in myMatrix:
        print("{}b{}\r".format(i,count))
        sys.stdout.flush()
        count +=1

if __name__ == '__main__':    
    
    csv_File_Name = sys.argv[1]     
    if(len(sys.argv) == 3):                                 #made the order mandatory for the user to fill
        order = sys.argv[2]
    else:
        print("Kindly enter the order of the polynomial you would like to evaluate")
        sys.exit()
    training_content = []   
    CsvLoadFile(csv_File_Name, training_content) 
    x_values, y_values = extract_values(training_content)
    n = len(x_values)
    order = int(order)
    matrix = order+1    
    matrix1 = np.zeros((matrix, matrix))
    function_values=[]
    matrix1,function_values = x_ValueInsertion(matrix1, n, x_values, y_values, order)
    matrix1 = np.linalg.inv(matrix1)                        #performed matrix inversion
    matrix2 = np.zeros((matrix,1))
    matrix2 = y_ValueInsertion(matrix2, n, x_values, y_values, order, function_values)
    product_of_matrices = MatrixMultiplication(matrix1, matrix2, order)
    myMatrix = product_of_matrices
    PrintValues(myMatrix)