# analysis.py
# A program which takes in Fisher's Iris dataset (reference #1), generates a summary for each variable, creates a histogram for each variable, 
# creates scatterplots to show the relationship between the petal and sepal attributes of each variable, and conducts relevant extra analysis.
# Author Micheal McEnery


# First, the program imports Pandas and Numpy (reference #2).
import pandas as pd
import numpy as np


# The code below defines a function which is used to complie the data from the Iris dataset. The attributes of each entry in the dataset are stored in a dictionary, and each dictionary is stored in a list (list_of_variables).
def load_data():
    # This line links the "list_of_variables" used in this function to the "list_of_variables" defined outside of this function.
    global list_of_variables
    # As the chunk size was set to one, each chunk consists of one row from the dataset (reference #4)
    for chunk in reader:
        # For each chunk of the dataset the attributes of each entry are identified and assigned to variables using .iat (.iat returns the value of a cell if given the row index, and column index) (reference #5)
        # As each chunk consists of only one row, the row index following .iat is always "0".
        sepal_l = chunk.iat[0,0]
        sepal_w = chunk.iat[0,1]
        petal_l = chunk.iat[0,2]
        petal_w = chunk.iat[0,3]
        class_id = chunk.iat[0,4]
        # Once value has been assigned to the above five variables, these variables are assigned to keys within a dictionary, with this dictionary then being appended to a list (list_of_variables) (reference #7))
        list_of_variables.append({"sepal_length" : sepal_l, "sepal_width" : sepal_w, "petal_length" : petal_l, "petal_width" : petal_w, "class_id" : class_id})
    # The above process repeats for every chunk/row in the dataset, providing us with a complete list of dictionaries, each dictionary holding the information of one entry in the dataset.


# The code below defines a function which will be used to write a summary of each variable entered in the dataset to a text file.
def summary_generator():
    # The count variable tracks how many variables have had a summary entered in the text file.
    count = 1
    # Below, the word "plant" represents a dictionary in the list_of_variables. (i.e. "for each dictionary in the list of dictionaries")
    for plant in list_of_variables:
        # The below "if" statement checks the count variable. If the count variable is one then no previous summary has been enetered. The program then writes the heading, and the summary for variable 1 into the text file
        if count == 1:
            # The program uses the open() and write() functions to open a text file called "summary_text_file", writes the heading, and writes the specified information for variable 1 (reference #6)
            # The variable number is defined by the count variable, and the attribute values are inserted using the associoated dictionary keys
            with open('summary_text_file.txt', 'w') as f:
                f.write("Below is a summary for each variable found in Fisher's Iris dataset:" + "\n" + "\n")
                f.write(f'For variable {count}, the Sepal length is {plant["sepal_length"]}cm, the Sepal width is {plant["sepal_width"]}cm, the Petal length is {plant["petal_length"]}cm, and the Petal width is {plant["petal_width"]}cm. The class of plant is {plant["class_id"]}.' + "\n" + "\n")
                f.close()
        # If a summary has previously been entered into the text file, the count variable will be > 1, and the "else" statement will instead prompt the program to append all subsequent summaries to the previously accessed text file.
        else:
            # The program will then use the open() and write() functions to append the text file with a summary of all remaining variables in the dataset (reference #6)
            # As above, the variable number is defined by the count variable, and the attribute values are inserted using the associoated dictionary keys
            with open('summary_text_file.txt', 'a') as f:
                f.write(f'For variable {count}, the Sepal length is {plant["sepal_length"]}cm, the Sepal width is {plant["sepal_width"]}cm, the Petal length is {plant["petal_length"]}cm, and the Petal width is {plant["petal_width"]}cm. The class of plant is {plant["class_id"]}.' + "\n" + "\n")
                f.close()
        count +=1
    # The above process loops until a summary has been created for every plant in the list_of_variables


# This line creates an enpty list which will later be populated with dictionaries representing each variable in the Iris dataset.
list_of_variables = []


# Next the program reads the data file titled "iris.data" and identifies the dataset as having no header (reference #3). 
# By setting the chunk size to one, an iterable object is returned and identified as "reader". This will allow the program to assess the dataset one chunk/row at a time through iteration (reference #4).
with pd.read_csv("iris.data", header=None, chunksize=1) as reader:
    load_data()
    summary_generator()
    



# References:
# Reference #1: https://archive.ics.uci.edu/ml/datasets/iris
# Reference #2: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#
# Reference #3: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
# Reference #4: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-chunking
# Reference #5: https://www.stackvidhya.com/get-value-of-cell-from-a-pandas-dataframe/#:~:text=You%20can%20get%20the%20value,cell%20from%20a%20pandas%20dataframe.&text=You%20can%20use%20the%20below,get%20a%20specific%20cell%20value
# Reference #6: https://www.pythontutorial.net/python-basics/python-write-text-file/
# Reference #7: https://pythonexamples.org/python-list-of-dictionaries/