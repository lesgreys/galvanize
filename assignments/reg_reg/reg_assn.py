import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures

import statsmodels.formula.api as smf

from sklearn import datasets

X, y  = datasets.load_diabetes(return_X_y=True, as_frame=True)

X = X.iloc[:100,:]


sns.pairplot(X, diag_kind='kde')
y.hist()