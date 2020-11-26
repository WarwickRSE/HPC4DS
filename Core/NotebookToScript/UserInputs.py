#!/usr/bin/env python3

## Script expects at least one argument that should be an integer. 
# Further arguments can be given. 'debug' is recognised

import sys
import json

#argv contains a list of strings as they were supplied at the command line
#These are split on spaces (which is the standard way) 
# The first item is always the name of the script being run
# This is the full name that was typed, including any folders etc

print(sys.argv)
print("This script was run as "+sys.argv[0])

#Process the rest of the command line args
# This is a basic system that just expects words as arguments
# For mor complicated things, you should use argparse:
# https://docs.python.org/3/library/argparse.html


# Check if something was present at all
if 'debug' in sys.argv[1:]:
    print("Script was run with debug option")

# The first argument should be a number. It doesn't have to be present
length = 0
try:
    length = int(sys.argv[1])
    print("Set length to "+str(length))
except:
    print("Please give a length (integer) for the first parameter")
    exit()



#Sometimes we might want to ask the user to type something in
# Lets keep asking until they give a plausible input
while(True):
    try:
        out_dir = input("Enter name of output directory: ")
        assert(len(out_dir) > 0)
        break
    except:
        print("Input directory can't be empty")


# Suppose we also want to read in a number, and must make sure it's an integer
# user-input checking is very important when reading in like this!

while(True):
    try:
        other_length = int(input("Enter length of widget: "))
        break
    except:
        print("Widget length must be an integer, Please try again")



# For really complicated inputs and setup, you want to use a file
# For this example, we're going to use some super-simple Json because
# it is very powerful. A super simple config file is provided

# Open the file, parse the content
with(open('config.json', 'r')) as infile:
    configs = json.load(infile)

# Default values if options not supplied
widget_name = "Default"

# Do something with the values
for item in configs:
    if item == "widget_name":
        widget_name = configs[item]
    elif item == "widget_options":
        widget_options = configs[item]


# Print everything to demo this working
print("We have created a widget named {} with length {} and other length {}".format(widget_name, length, other_length))
print("Output will be saved in directory {}".format(out_dir))
print("Widget options are as follows {}".format(','.join(widget_options)))

