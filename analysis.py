# analysis.py
# A program which takes in information from Fisher's Iris dataset (reference #1), conducts specific analysis, and outputs the results.
# Author Micheal McEnery


# First the program imports Pandas and Numpy (reference #2)
import pandas as pd
import numpy as np

count = 1

# Next the program reads the data file located in the local respository + identifies the dataset as heaving no header (reference #3), and sets the chunk size to one (which will be used to iterate through the data set) (reference #4)
with pd.read_csv("iris.data", header=None, chunksize=1) as reader:
    reader
    for chunk in reader:

        # As each chunk consists of one row from the dataset, the different dataset values are identified and assigned to variables using the .iat function (reference #5)
        sepal_length = chunk.iat[0,0]
        sepal_width = chunk.iat[0,1]
        petal_length = chunk.iat[0,2]
        petal_width = chunk.iat[0,3]
        class_id = chunk.iat[0,4]

        # The below "if" statement checks if the count == 0, and if so opens a new text file and inputs the entry for variable 1.
        if count == 1:
            # The program will then use the open() and write() functions to open a text file called "summary_text_file" and write the specified information for variable #1 in the dataset (reference #6)
            with open('summary_text_file.txt', 'w') as f:
                f.write("Below is a summary for each variable found in Fisher's Iris dataset" + "\n" + "\n")
                f.write(f'For variable {count}, the Sepal length is {sepal_length}cm, the Sepal width is {sepal_width}cm, the Petal length is {petal_length}cm, and the Petal width is {petal_width}cm. The class of plant is {class_id}.' + "\n" + "\n")
                f.close()
        # If an entry has previously been entered into the text file, the "else" statement will instead append all new entrys to the previously accessed text file.
        else:
            # The program will then use the open() and write() functions to append the text file called "summary_text_file" with the specified information from all remaining variables in the dataset (reference #6)
            with open('summary_text_file.txt', 'a') as f:
                f.write(f'For variable {count}, the Sepal length is {sepal_length}cm, the Sepal width is {sepal_width}cm, the Petal length is {petal_length}cm, and the Petal width is {petal_width}cm. The class of plant is {class_id}.' + "\n" + "\n")
                f.close()

        count +=1


# References:
# Reference #1: https://archive.ics.uci.edu/ml/datasets/iris
# Reference #2: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#
# Reference #3: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
# Reference #4: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-chunking
# Reference #5: https://www.stackvidhya.com/get-value-of-cell-from-a-pandas-dataframe/#:~:text=You%20can%20get%20the%20value,cell%20from%20a%20pandas%20dataframe.&text=You%20can%20use%20the%20below,get%20a%20specific%20cell%20value
# Reference #6: https://www.pythontutorial.net/python-basics/python-write-text-file/