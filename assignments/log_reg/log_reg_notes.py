%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import scipy
from sklearn.linear_model import LogisticRegression, LinearRegression
import itertools

plt.style.use('fivethirtyeight')

'''
========================
Standards/Objectives
- Introduce basics of logistic regression
========================
========================
- Explain the key differences and similarities between logistic and linear regression.

log is a classification model vs. lin being a regression 
Other examples of Binary Classification
- Churn / Not Churn
- Win / Not Win
- Reactant / Product
- True / False
- Really any binary categorical variable!
Multinomial Classification We will focus on binary classification in this notebook, but we can study multinomial classification as well where there are >2 categories. Some examples of this maybe:
- First, Second, Third Place
- Genre of music (pop, rap, country, etc.)
- Win, Lose, Tie
- Any thing >2 classes
========================

========================
- Fit and interpret beta coefficients of a logistic regression model in sklearn
========================

========================
- Identify methods for evaluating classification models
========================



'''


