"""
@author: Prinitha Nagarajan
UTA_ID : 1001668557
"""

import csv
import sys


def CsvLoadFile(file_name, training=[]):            #loaded the CSV file with the given 2 dimensional dataset                  
    load_data = open(file_name, 'r')
    # print("Load Data is: ",load_data)
    content = csv.reader(load_data)
    # print("Content is: ",content)
    data = list(content)
    print("Data is: ",data)
    for part in range(len(data)):
        for entity in range(len(data[part])):
            data[part][entity] = data[part][entity]
        if 1 == 1:
            training.append(data[part])


if __name__ == '__main__':    
    
    csv_File_Name = sys.argv[1]     
    if len(sys.argv) == 2:                                 #made the order mandatory for the user to fill
        print("Well Done! One part completed!")
    else:
        print("Kindly enter the order of the polynomial you would like to evaluate")
        sys.exit()
    training_content = []   
    CsvLoadFile(csv_File_Name, training_content) 