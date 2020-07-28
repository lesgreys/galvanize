import numpy as np
import pandas as pd
from scipy.spatial import distance
from collections import Counter
from make_data import make_data

def euclidean_distance(a, b):
    """Compute the euclidean distance between two numpy arrays.

    Parameters
    ----------
    a: numpy array
    b: numpy array

    Returns
    -------
    distance: float
    """
    dist = np.linalg.norm(a-b)
    return dist


def cosine_distance(a, b):
    """Compute the cosine dissimilarity between two numpy arrays.

    Parameters
    ----------
    a: numpy array
    b: numpy array

    Returns
    -------
    distance: float
    """
    dist = distance.cosine(a,b)
    return dist


def manhattan_distance(a, b):
    """Compute the manhattan (L1) distance between two numpy arrays.

    Parameters
    ----------
    a: numpy array
    b: numpy array

    Returns
    -------
    distance: float
    """
    dist = distance.cityblock(a, b)
    return dist


class KNNRegressor:
    """Regressor implementing the k-nearest neighbors algorithm.

    Parameters
    ----------
    k: int, optional (default = 5)
        Number of neighbors that are included in the prediction.
    distance: function, optional (default = euclidean)
        The distance function to use when computing distances.
    """

    def __init__(self, k=5, distance=euclidean_distance):
        """Initialize a KNNRegressor object."""
        self.k = k
        self.distance = distance

    def fit(self, X, y):
        """Fit the model using X as training data and y as target values.

        According to kNN algorithm, the training data is simply stored.

        Parameters
        ----------
        X: numpy array, shape = (n_observations, n_features)
            Training data.
        y: numpy array, shape = (n_observations,)
            Target values.

        Returns
        -------
        self
        """
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        """Return the predicted values for the input X test data.

        Assumes shape of X is [n_test_observations, n_features] where
        n_features is the same as the n_features for the input training
        data.

        Parameters
        ----------
        X: numpy array, shape = (n_observations, n_features)
            Test data.

        Returns
        -------
        result: numpy array, shape = (n_observations,)
            Predicted values for each test data sample.

        """
        train_rows, train_cols = self.X_train.shape
        Xshape, _ = X.shape
        X = X.reshape((-1, train_cols))
        distances = np.zeros((Xshape, train_rows)) 

        for i, x in enumerate(X):
            for j, x_train in enumerate(self.X_train):
                distances[i,j] = self.distance(x_train, X)
        k_neaerest = distances.argsort()[:, :self.k]
        topk = self.y_train[k_neaerest].mean()
        return topk
        


if __name__ == '__main__':
    X, y =  make_data(n_features=2, n_pts=300, noise=0.1)
    knn = KNNRegressor()
    knn.fit(X,y)
    y_pred = knn.predict(X[3:8])
    print(y_pred)