#!/usr/bin/python

import sys
import argparse
from datetime import datetime

def parse_arg():

    """Parses the args"""    
    if len(sys.argv) < 1:
        print("Args: Input filename")
        raise RuntimeError("Insufficient arguments.")
    
    arg_1 = sys.argv[1]
    #arg_2 = sys.argv[0]
    return arg_1

#Parameter is the filename
filename = parse_arg()

#Create filename for output
output_file_date = datetime.now().strftime("%Y%m%d_%I%M%S")
output_file = output_file_date + '_' + filename

#Access the input file
with open(filename, 'rb') as input_file, open(output_file, 'w') as file_output:
    
    #Create the header"""
    output_file_header = input_file.readline().decode('cp1252').replace('\r','')
    file_output.write(output_file_header)

    #Skip the header in the input file
    next(input_file)

    #iterate over file object line by line
    for line in input_file:

        #Create output file objects
        lines = line.decode().split(',')

        #Create the email username variable
        username = lines[1].split('@')[0]

        #Create variable that display last two characters
        check_email = username[-1:]
        
        #Create file based on business rules and write results to file.
        if check_email.isupper(): #and len(username) < 16:
            output_data = ','.join(lines).replace('\r','')
            file_output.write(output_data)
