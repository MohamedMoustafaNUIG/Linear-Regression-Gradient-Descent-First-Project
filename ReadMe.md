## What is this project about?

This is a machine learning project. It uses a Supervised Learning algorithm known as (Multivariate) Linear Regression to take several attributes as inputs (in this case three attributes) and uses a hypothesis function to map those inuts onto an output over a continuous range of values (the real numbers).

It uses the Squared Error Cost Function along with the Batch Gradient Descent algorithm to calculate appropriate parameters (&theta;<sub>i</sub>) for the following hypothesis function:

h<sub>&theta;</sub> = &theta;<sub>o</sub> + &theta;<sub>1</sub>att1 + &theta;<sub>2</sub>att2 + &theta;<sub>3</sub>att3

which will be used to predict a fourth attribute.

### The Dataset:

The data used in this case is from the Iris dataset 

(Link: https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv)

The dataset contains the Sepal length and width and the Petal length and width (in that order) of 150 Iris flowers of three different species.

I decided to focus only on the Setosa species' data as different species might have different trends.

### The Data:

Of the four attributes, one was chosen to be the output and the other three the inputs.

I choose to let the Sepal Length to be the output.

### Training and Evaluating

Of the 50 records, 40 were used by the Gradient descent method to find good values for the parameters (&theta;<sub>i</sub>). The final 10 were used to evaluate how accurate the hypothesis function has become after training, by comparing the predictions with the actual values. In this specific case, the predictions were nearly 95%(Java) - 89%(Python) accurate. A larger and more varied dataset might give different results.

### Versions

* Multivariate_LinearRegression.java is the initial Java version of the program. It reads data from a txt file using regular Java buffer reader and uses ArrayLists for storing and accessing the data.

* Multivariate_LinearRegression.py is a python version of this program. It uses the Pandas library for reading and accessing the dataset from a csv file.

* Generic Multivariate Linear Regression.ipynb is a Jupyter notebook implementation of this project, with some additional tweaks (MinMax normalization and max_iter for training).