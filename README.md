# This README file outlines the details of the pands-project.


### Task list:
- [x] Research Fisher's Iris data set and write a summary.
- [x] Download the data set and add it to the respository.
- [x] Write a python program called analysis.py which does the following:
    - [x] Outputs a summary of each variable to a single text file.
    - [x] Saves a histogram of each variable to png files.
    - [x] Outputs a scatter plot of each pair of variables.
    - [x] Performs any other analysis you think is appropriate.


## Summary of Data Set:
Fisher's Iris data set was created by R.A. Fisher. This data set contains attribute information relating to different classes of iris plant. This data set concerns three class of iris plant, with 50 instances each (total 150). The classes of iris plant include the Iris-setosa, the Iris-versicolor, and the Iris-virginica. The attributes of concern in this data set include the sepal length and width, and the petal length and width of each class (measured in cm). More information on the data set can be found at the following link (see: reference #1) Much previous work concerning Fisher's Iris data set has been done in the area of machine learning, due mainly to the generally accepted suitability of the data for imprementation in investigations of areas such as classification (reference #24 and #25), and clustering (reference #26). For the purposes of this project, this current investigation aims to develop a python program which functions to generate a summary of each class of iris, as well as, histogram and scatterplot visual representations relating to each class of iris. Furthermore, I have chosen to include barchart representations of the mean attribute size for each class of iris in order to satisfy the final task noted in the task list above. Below is an outline of how the python program I have created achieves each of these goals.


## Program: analysis.py
Detailed information on the functionality of each line in analysis.py can be found within comments in the code. The following is a brief description of functionality. When initialised, analysis.py first creates an object of chunk size 50 called "reader" using pandas.read_csv() from the dataset (iris.data). analysis.py then calls load_data(), which iterates through the "reader" object one chunk (50 rows) at a time and assigns these chunks to corresponding variables from the dataset which are then stored in a list. analysis.py then calls generate_summary(), which using the list of chunk variables, generates a text file featuring a summary for each of the three variables/species of iris in the dataset, including information on the mean, standard deviation, minimum and maximum values of each attribute of each variable. analysis.py then calls generate_histogram(), which using the list of chunk variables, generates a histogram representation of the sizes of each attribute for each variable/species of iris in the dataset. analysis.py then calls generate_scatterplot(), which using the list of chunk variables, generates a scatterplot representation of the relationship between the linked attributes for each pair of variables/species of iris in the dataset. Lastly, analysis.py calls generate_barchart(), which using the list of chunk variables, generates a barchart representation of the mean attribute size of each species of iris for each attribute.

## References:
- Reference #1: https://archive.ics.uci.edu/ml/datasets/iris
- Reference #2: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html#
- Reference #3: https://matplotlib.org/stable/users/getting_started/
- Reference #4: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
- Reference #5: https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#io-chunking
- Reference #6: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iat.html
- Reference #7: https://www.pythontutorial.net/python-basics/python-write-text-file/
- Reference #8: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.mean.html?highlight=mean#pandas.core.groupby.GroupBy.mean
- Reference #9: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.std.html
- Reference #10: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.get.html?highlight=get#pandas.DataFrame.get
- Reference #11: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.count.html
- Reference #12: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.min.html
- Reference #13: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.groupby.GroupBy.max.html
- Reference #14: https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.hist.html
- Reference #15: https://matplotlib.org/3.5.0/gallery/pyplots/pyplot_text.html#sphx-glr-gallery-pyplots-pyplot-text-py
- Reference #16: https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.savefig.html#matplotlib.pyplot.savefig
- Reference #17: https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.clf.html
- Reference #18: https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.patches.Patch.html#matplotlib.patches.Patch
- Reference #19: https://realpython.com/visualizing-python-plt-scatter/#exploring-pltscatter-further
- Reference #20 https://matplotlib.org/stable/api/markers_api.html#module-matplotlib.markers
- Reference #21: https://thispointer.com/python-capitalize-the-first-letter-of-each-word-in-a-string/#:~:text=Use%20title()%20to%20capitalize,of%20word%20to%20lower%20case.
- Reference #22: https://www.geeksforgeeks.org/bar-plot-in-matplotlib/
- Reference #23: https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
- Reference #24: https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.403.8780&rep=rep1&type=pdf
- Reference #25: https://d1wqtxts1xzle7.cloudfront.net/53763693/ZE0601200205-with-cover-page-v2.pdf?Expires=1651073868&Signature=RbEp0NnXWDfHUdRSpSkrxjK9fUCQnSUd67bT1gAcNqib4enbi6-Hu8ySMWS0sAx95YHlCwCYVB6JRaKfdEOeC8MEfelcaTZpa7p3c98NnYlSZBzHx~w5-6cMozQ88sd8TRGDV9UlyzOETPrF96hYK2pd7yNNy42V~G1r0rkfBMONSqJ5lvZT6CGWXrlU52uktjk7vyCiC9GKdcuyGg3oDkGqB9NFPtCbq8hpr5TXeDPmnhhUKwfwhvcaHSMe12BrD8Ht68STdVwhXhbXCPZJgNwOcEpGxrUYO74hBe0EIj8GlJKC2xkgoIT5aKBzaLunyW0QJIsdfQNRZyvR0fdV4Q__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA
- Reference #26: http://carlmeyer.com/pdfFiles/REU2010_Paper.pdf