# analysis.py
# A program which takes in Fisher's Iris dataset (reference #1), generates a text file summary for each of the three variables, creates a histogram representation of the attributes of each variable, 
# creates a scatterplot graph to show the relationship between the attributes of each pair of variables, and creates a barchart representation of the mean attribute size of each variable.
# Author: Micheal McEnery


# First, the program imports Pandas and Matplotlib.pyplot (reference #2)(reference #3).
# Pandas will be used for interacting with the dataset, and Matplotlib will be used for generating graphs and statistical representations.
import pandas as pd
import matplotlib.pyplot as plt


# The below line defines a function which iterates through the "reader" object one chunk (50 rows) at a time and assigns these chunks to  corresponding variables from the dataset which are then stored in a list.
def load_data():
    # The line below allows this function to access the list "list_of_variables" defined outside of this function.
    global list_of_variables
    # This counter variable serves to track which chunk is assigned to which variable.
    counter = 1
    # As the chunk size was set to 50, each chunk of "reader" consists of 50 rows from the dataset.
    # As there are 50 rows associoated with each of the three variables, and the variables are organised alphabetically by name, this allows the program to iterate through "reader" and save each chunk to the corresponding variable.
    # The program then appends each of these chunk variables to the list "list_of_variables".
    for chunk in reader:
        if counter == 1:
            setosa = chunk
            list_of_variables.append(setosa)
        elif counter == 2:
            versicolor = chunk
            list_of_variables.append(versicolor)
        elif counter == 3:
            virginica = chunk
            list_of_variables.append(virginica)
        counter += 1


# The below line defines a function which generates a text file featuring a summary for each of the three variables/species of iris in the dataset, including information on the mean, standard deviation, minimum and maximum values of each attribute of each variable.
def generate_summary():
    # The program uses the open() and write() functions to open and write to a text file called "summary_text_file" (reference #7)
    with open('summary_text_file.txt', 'w') as f:
        # This function first writes the heading outlined below.
        f.write("Below is a summary of each of the three variables found in Fisher's Iris dataset:" + "\n")
        # Next, for each chunk ("plant") in the list "list_of_variables", the function writes the details outlined below.
        for plant in list_of_variables:
            # For each of the three chunks, the function writes the name of the species of iris from the dataset.
            # DataFrame.iat() returns the value of a cell if given the row index, and column index (reference #6). This provides the variable name for each of the 3 variables (variable name is always located in column "4" of each chunk).
            # For each of the three chunks, the function also writes the number of rows associoated with each plant.
            # GroupBy.count() counts the number of values is a group, and DataFrame.get() specifies using a key which dataframe column should be referenced (reference #11)(reference #10)
            f.write("\n" + f'For the {plant.iat[0, 4]}, {plant.count().get(4)} entries are noted in the dataset. All entries were measured in cm.' + "\n")
            # The "counter" variable serves to track the column number of each column as information is extracted and analysed from the dataset, starting at column 0 ("sepal length") and going to colmun 3 ("petal width").
            counter = 0
            # Also, for each chunk, for each attribute listed in the list "list_of_attributes", the function assesses and writes the mean and standard deviation, as well as minimum and maximum values of each attribute.
            for attribute in list_of_attributes:
                # {attribute} pulls the name of each attribute from the "list_of_attributes"
                # round() rounds each of the figues return to two decimal places.
                # For each analysis, Dataframe.get() specifies the column to pull data from, with "counter" specificing the column number (reference #10)
                # For mean: GroupBy.mean() computes the mean of the column (reference #8)
                # For standard deviation: Groupby.std() computes the standard deviation of the column (reference #9)
                # For minimum value: Groupby.min() returns the minimum value of the column (reference #12)
    	        # For maximum value: Groupby.max() returns the maximum value of the column (reference #13)
                f.write(f'The mean {attribute} was {round(plant.get(counter).mean(), 2)}, with a standard deviation of {round(plant.get(counter).std(), 2)}. The minimum {attribute} was {round(plant.get(counter).min(), 2)}, and the maximum {attribute} was {round(plant.get(counter).max(), 2)}' + "\n")
                # "counter" increases by 1 to move to the next column
                counter += 1
        # When this function has finished inputting text to the text file, close() closes the text file (reference #7)
        f.close()


# The below line defines a function which generates a histogram representation of the sizes of each attribute for each variable/species of iris in the dataset.
def generate_histogram():
    # For each chunk ("plant") in the list "list_of_variables"
    for plant in list_of_variables:
        # The "counter" variable serves to track the column number of each column as information is extracted and used to construct a histogram, starting at column 0 ("sepal length") and going to colmun 3 ("petal width").
        counter = 0
        # For each attribute in "list_of_attributes", a histrogram is created
        for attribute in list_of_attributes:
            # matplotlib.pyplot.hist() is used to generate a histogram figure (reference #14)
            # DataFrame.get() specifies using a key which dataframe column should be referenced (reference #10)
            # "counter" specifies which column in the chunk to analyse
            # edge color is set to black to improve readability of the graphs (reference # 18)
            plt.hist(plant.get(counter), edgecolor='black')
            # pyplot.ylabel() sets the x-axis label (reference #15)
            plt.xlabel("Size in cm")
            # pyplot.xlabel() sets the y-axis label (reference #15)
            plt.ylabel("Frequency")
            # pyplot.title give the graph a title (reference #15)
            # {attribute} pulls the name of each attribute from the "list_of_attributes"
            # pandas.DataFrame.iat returns the value of a cell if given the row index, and column index (reference #6). This provides the variable name for each of the 3 variables (variable name is always located in column "4").
            plt.title(f"Histogram of {attribute} in {plant.iat[0, 4]}")
            # pyplot.savefig() saves the figure, if given a title, as a specificed file type (in this case .png) to a specified directory (reference #16)
            # pandas.DataFrame.iat returns the value of a cell if given the row index, and column index (reference #6). This directs which folder the figure will be saved in, and also influences the title of the figure.
            # {attribute} pulls the name of each attribute from the "list_of_attributes"
            plt.savefig(f"./images/histograms/{plant.iat[0, 4]}/Histogram of {attribute} in {plant.iat[0, 4]}.png")
            # "counter" increases by 1 to move to the next column
            counter += 1
            # pyplot.clf() clears the figure created above after the figure has been saved as a png, as not to impact the proceeding figures (reference #17)
            plt.clf()


# The below line defines a function which generates a scatterplot representation of the relationship between the linked attributes for each pair of variables/species of iris in the dataset.
def generate_scatterplot():
    # The "counter" variable serves to track which pair of linked attributes are being inputted to the scatterplots (first sepal, then petal attributes)
    counter = 0
    # The below "for loop" serves to loop all code below it twice (once for sepal attributes, and once for petal attributes)
    for _ in range(0, 2):
        # The "combination" variable serves to track which combination of plant variables are being inputted into the scatterplots
        combination = 1
        # The below "for loop" serves to loop all code below it three times, once for each of the three possible variable combinations.
        for _ in range(0, 3):
            # The below "if statement" serves to check the current combination to be inserted into the scatterplots, starting with combination #1
            # The "species-#" variables pull the plant chunks from the "list_of_variables", corresponding to the three possible combinations
            if combination == 1:
                species_1 = list_of_variables[0]
                species_2 = list_of_variables[1]
            elif combination == 2:
                species_1 = list_of_variables[1]
                species_2 = list_of_variables[2]
            elif combination == 3:
                species_1 = list_of_variables[0]
                species_2 = list_of_variables[2]
            # Below, the two pyplot.scatter lines serve to create a signle scatterplot which two sources of information (reference #19)
            # The relevant data columns are selected using the Dataframe.get method, and the counter variable
            # pyplot.scatter also takes in the parameters "color" (which sets the color of the selected data), "marker" (which sets the shape of the data markers)(reference #20), "s" (which sets the size of the data markers), and "alpha" (which sets the transparency of data markers)
            plt.scatter(species_1.get(counter), species_1.get(counter + 1), color="red", marker="x", s=75)
            plt.scatter(species_2.get(counter), species_2.get(counter + 1), color="blue", alpha=0.5)
            # pyplot.title sets the title of the scatterplot, and pull required information as outlined previously in the generate_histogram function
            # The title() function, when applied to a string, capitalises the first characters of each word in the string. This was done to improve the look of each graph (reference #21)
            plt.title(f"{species_1.iat[0, 4]} and {species_2.iat[0, 4]}: {list_of_attributes[counter].title()} and {list_of_attributes[counter + 1].title()}")
            # pyplot.legend inserts a legend into the scatterplot identifying the two variables present in the scatterplot and their associoated colors
            plt.legend([f"{species_1.iat[0, 4]}", f"{species_2.iat[0, 4]}"])
            # Both of the pyplot label lines below provide labels for both the x-axis and the y-axis
            plt.xlabel(f"{list_of_attributes[counter]}".title())
            plt.ylabel(f"{list_of_attributes[counter + 1]}".title())
            # pyplot.savefig saves the figure, if given a title, as a specificed file type (in this case .png) to a specified directory
            plt.savefig(f"./images/scatterplots/{species_1.iat[0, 4]} and {species_2.iat[0, 4]}/Scatterplot of {list_of_attributes[counter]} and {list_of_attributes[counter + 1]} in {species_1.iat[0, 4]} and {species_2.iat[0, 4]}.png")
            # pyplot.clf clears the figure created above after the figure has been saved as a png, as not to impact the proceeding figures 
            plt.clf()
            combination += 1
        counter = 2


# The below line defines a function which generates a barchart representation of the mean attribute size of each species of iris for each attribute.
def generate_barchart():
    # The "counter" variable tracks which column from the dataset should be inputted
    counter = 0
    # For each attribute in the "list_of_attributes" a barchart is created
    for attribute in list_of_attributes:
        # The below line creates am empty dictionary object called "mean_dictionary"
        mean_dictionary = {}
        # For each species of iris in "list_of_variables" the mean values of the specified column and the name of the species in question are saved to variables
        # The variables appended as key value pairs to the previously created "mean_dictionary" using dict.update() (reference #23)
        for plant in list_of_variables:
            mean = plant.get(counter).mean()
            name = plant.iat[0, 4]
            mean_dictionary.update({name : mean})
        # The keys from "mean_dictionary" are then saved to a list titled "names"
        names = list(mean_dictionary.keys())
        # The values from "mean_dictionary" are also saved to a list, titled "means"
        means = list(mean_dictionary.values())
        # pyplot.bar is used to generate a barchart, with the lists "names" and "means" being input as the information for the barchart. Color and column width are also defined (reference #22)
        plt.bar(names, means, color="teal", width=0.5)
        # I have previously outlined the remaining lines in this function in other functions.
        plt.xlabel("Species of Iris")
        plt.ylabel(f"Mean {attribute}")
        plt.title(f"Mean {attribute.title()} of each species of Iris")
        plt.savefig(f"./images/barcharts/Barchart of mean {attribute} in each species.png")
        plt.clf()
        counter += 1


# This line creates a list titled "list_of_variables".
list_of_variables = []
# This line creates a list titled "list_of_attributes" which holds the names of the four attributes associoated with the three variables in the same sequence they are presented in the dataset.
list_of_attributes = ["sepal length", "sepal width", "petal length", "petal width"]


# The program then reads the dataset titled "iris.data" using read_csv() and identifies the dataset as having no header (reference #4)
# The program also sets the chunk size to 50.
# Due to the parameters applied to read_csv(), when the below line is run, an iterable object is returned and identified as "reader", with each chunk in "reader" consisting of 50 rows (reference #5).
# This will allow the program to iterate through the dataset at the rate of 50 rows per chunk.
with pd.read_csv("iris.data", header=None, chunksize=50) as reader:
    # The program then calls the load_data function (defined above).
    load_data()
    # The program then calls the generate_summary function (defined above).
    generate_summary()
    # The program then calls the generate_histogram function (defined above).
    generate_histogram()
    # The program then calls the generate_scatterplot function (defined above).
    generate_scatterplot()
    # The program lastly calls the generate_barchart function (defined above).
    generate_barchart()




# References:
# Reference #1: https://archive.ics.uci.edu/ml/datasets/iris
# Reference #2: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#
# Reference #3: https://matplotlib.org/stable/users/getting_started/
# Reference #4: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
# Reference #5: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-chunking
# Reference #6: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iat.html
# Reference #7: https://www.pythontutorial.net/python-basics/python-write-text-file/
# Reference #8: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.mean.html?highlight=mean#pandas.core.groupby.GroupBy.mean
# Reference #9: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.std.html
# Reference #10: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.get.html?highlight=get#pandas.DataFrame.get
# Reference #11: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.count.html
# Reference #12: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.min.html
# Reference #13: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.max.html
# Reference #14: https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.hist.html
# Reference #15: https://matplotlib.org/3.5.0/gallery/pyplots/pyplot_text.html#sphx-glr-gallery-pyplots-pyplot-text-py
# Reference #16: https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig
# Reference #17: https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.clf.html
# Reference #18: https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch
# Reference #19: https://realpython.com/visualizing-python-plt-scatter/#exploring-pltscatter-further
# Reference #20 https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers
# Reference #21: https://thispointer.com/python-capitalize-the-first-letter-of-each-word-in-a-string/#:~:text=Use%20title()%20to%20capitalize,of%20word%20to%20lower%20case.
# Reference #22: https://www.geeksforgeeks.org/bar-plot-in-matplotlib/
# Reference #23: https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/