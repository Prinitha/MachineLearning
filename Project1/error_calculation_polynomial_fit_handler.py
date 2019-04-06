"""
@author: Prinitha Nagarajan
UTA_ID : 1001668557
"""

import numpy as np
import csv
import sys
import re

def CsvLoadFile(file_name, training=[]):            
    #loaded the CSV file with the given 2 dimensional dataset                  
    load_data = open(file_name, 'r')
    content = csv.reader(load_data)
    data = list(content)
    pattern = '[0-9., ]'
    for part in range(len(data)):
        part = "".join(data[part])
        resultant_part = ''
        for i, e in enumerate(part):
            if re.match(pattern, e):
                if e == ' ' and part[i-1] is not ',':
                    e = ', '
                resultant_part += ''.join(e)
        resultant_part = resultant_part.replace(' ', '')
        part_data = resultant_part.split(",")
        if 1 == 1:
            training.append(part_data)

def extract_values(training):                       
    #separated the data points into x, y and class values
    x_values=[]
    y_values=[]
    classes=[]
    for i in training:
        x_values.append(float(i[0]))
        y_values.append(float(i[1]))
        classes.append(float(i[2]))
    return x_values, y_values, classes

if __name__ == '__main__':    
    #Added the CSV dataset to extract the training values
    csv_File_Name = sys.argv[1]     
    training_content = []   
    CsvLoadFile(csv_File_Name, training_content) 
    x_values, y_values, classes = extract_values(training_content)
    #Manually feeded the data
    a00 = 1.743
    a10 = 3.124
    a01 = 3.058
    b00 = 4.414
    b10 = 1.973
    b01 = 2.959 
    b20 = 0.09704 
    b11 = 0.01854 
    b02 = 0.001007
    c00 = 4.072
    c10 = 2.233
    c01 = 2.95
    c20 = 0.04796
    c11 = 0.007837
    c02 = 0.008888
    c30 = 0.002763
    c21 = 0.0007264
    c12 = 0.0002579
    c03 = -0.0006093
    d00 = 3.981  
    d10 = 2.531  
    d01 = 2.721  
    d20 = -0.07637  
    d11 = 0.06663  
    d02 = 0.05788  
    d30 = 0.0184  
    d21 = 0.004662  
    d12 = -0.01619  
    d03 = -0.002317  
    d40 = -0.0005911  
    d31 = -0.0006795  
    d22 = 0.0006673  
    d13 = 0.0006535  
    d04 = -6.39e-05

    error = []
    error_order1 = error_order2 = error_order3 = error_order4 = 0
    #print(error_order1, error_order2, error_order3, error_order4)
    #For order=1
    # f(x,y) = p00 + p10*x + p01*y
    for i in range(len(x_values)):
        x = x_values[i]
        y = y_values[i]
        error_order1 += (classes[i]-(a00+(a10*x)+(a01*y)))**2
    error.append(error_order1)
    print("The error from function for Order 1 is : ", error_order1)

    #For order=2
    # f(x,y) = p00 + p10*x + p01*y + p20*x^2 + p11*x*y + p02*y^2
    for i in range(len(x_values)):
        x = x_values[i]
        y = y_values[i]
        error_order2 += (classes[i]-(b00+(b10*x)+(b01*y)+(b20*(x**2))+(b11*x*y) + b02*(y**2)))**2
    error.append(error_order2)
    print("The error from function for Order 2 is : ", error_order2)

    #For order=3
    #f(x,y) = p00 + p10*x + p01*y + p20*x^2 + p11*x*y + p02*y^2 + p30*x^3 + p21*x^2*y + p12*x*y^2 + p03*y^3
    for i in range(len(x_values)):
        x = x_values[i]
        y = y_values[i]
        error_order3 += (classes[i]-(c00 + c10*x + c01*y + (c20*(x**2)) + (c11*x*y) + (c02*(y**2)) + (c30*(x**3)) + (c21*(x**2)*y) 
                    + (c12*x*(y**2)) + (c03*(y**3))))**2
    error.append(error_order3)
    print("The error from function for Order 3 is : ", error_order3)

    #For order=4
    #f(x,y) = p00 + p10*x + p01*y + p20*x^2 + p11*x*y + p02*y^2 + p30*x^3 + p21*x^2*y + p12*x*y^2 + p03*y^3 + p40*x^4 + p31*x^3*y + p22*x^2*y^2 + p13*x*y^3 + p04*y^4
    for i in range(len(x_values)):
        x = x_values[i]
        y = y_values[i]
        error_order4 += (classes[i]-(d00 + d10*x + d01*y + (d20*(x**2)) + d11*x*y + (d02*(y**2)) + (d30*(x**3)) + (d21*(x**2)*y) 
                    + (d12*x*(y**2)) + (d03*(y**3)) + (d40*(x**4)) + (d31*(x**3)*y) + (d22*(x**2)*(y**2)) 
                    + (d13*x*(y**3)) + (d04*(y**4))))**2
    error.append(error_order4)
    print("The error from function for Order 4 is : ", error_order4)

    #To find the minimum error among all the error values of different order functions
    minimum_error = min(error)
    print("The minimum of all the errors is: ", minimum_error)

    #To find the order which generated the least error
    for i in range(len(error)):
        if(error[i]==minimum_error):
            print("Lease risk is in the order: ", i+1)