#!/usr/bin/env python3



def my_useful_function():

    print("Called my useful function")

def my_other_function(arg):

    print("Called my other function with arg {}".format(arg))


print("This code runs whether we run or import the file")
my_useful_function()
my_other_function(7)
print("______________________________________________")

if __name__ == "__main__":

    print("This code only runs when we run (not import) the script")

    my_other_function(23)
    print("______________________________________________")




print("The block above was inside the if, this is not and runs always")
print("______________________________________________")


