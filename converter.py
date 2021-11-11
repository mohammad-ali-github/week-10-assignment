input_file_name = "SalesJan2009.csv"
output_file_name = "transaction_data.json"

# 1. Creating an empty list sales_data
sales_data = []

# 2. Opening the input file
input_file = open(input_file_name, 'r')

# 3. Processing the file line by line

# For each line
for line in input_file:
    # Strip the line for new lines and split it on comma
    line = line.strip()
    attributes = line.split(',')
    
    dictionary = {} # Inner dictionary
    previous_attribute = None # Previous attribute or dictionary reference
    
    # For each attribute in reversed iteration
    for attribute in reversed(attributes):
        
        dictionary = {}     # Empty the dictionary
        # If it's the last attribute, just update the previous attribute
        if attribute == attributes[-1]:
            previous_attribute = attribute
        else:
            # Else just add the current attribute as key for value of previous attribute
            dictionary[attribute] = previous_attribute
            previous_attribute = dict(dictionary)

    # Append the dictionary into list
    sales_data.append(dictionary)

# 4. Outputting data to json file

# Import the json module
import json

# Open the output file and dump the data to it
output_file = open(output_file_name, 'w')
json.dump(sales_data, output_file)

# Closing file streams
input_file.close()
output_file.close()