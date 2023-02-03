import re
import y_splitter


name_pat = '\w+\n'
y_split_pat = '^.(\w+)'
# Data Structure is storing all structs for each model. 
library = {}

# Adjacency Matrix used to store the logic block input/output connections. also use for the weights of connections
conn = [[]]

# Read file and build them as they get read.

# Open function to open the file "Mock_File.txt"
# it's reference in the variable file1
 
with open('Code/Mock_File.txt') as f:
 
    # Reading from file
    for line in f:
        if re.search(name_pat,line):
            schematic_name = re.search(name_pat,line)
        if re.search('.y_splitter',line):
            to_array = [char for char in line]
            y_split =  y_splitter()
            
    

    
    

        

