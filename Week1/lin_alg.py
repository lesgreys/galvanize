import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline
#MARKOV CHAIN SOLUTION

# l = np.array([.25,.20,.55]).reshape(3,1)
# A = np.array([[.7,.1,0],[.2,.9,.2],[.1,0,.8]])

# l09 = A @ l
# print(f'year 2009: {l09}')
# print(f'year 2014: {A @ l09}')

# n04 = np.array([0,0,1]).reshape(3,1)
# n04c = np.array([1,0,1]).reshape(3,1)
# n04i = np.array([0,1,0]).reshape(3,1)

# for _ in range(1, 100):
#   l = A@l
# print(f'the answer is {l}')

# # x1, x2, x3 = np.dot(A, x)

# n09 = np.dot(A,n04)
# n14 = np.dot(A,n09)

# n09, n14

# c = np.hstack((n04,n09,n14)).T

# com = c[:,0]
# ind = c[:,1]
# res = c[:,2]
# year = ['2004','2009','2014']
# plt.plot(year,com ,label='com')
# plt.plot(year,ind, label='ind')
# plt.plot(year,res, label='res')
# plt.show()

iris = pd.read_csv('data/iris.txt')
print(iris.head(5))
iris.info()


data = iris[['SepalWidth', 'SepalLength']].to_numpy()
mean_col = np.mean(data, 0)
plt.scatter(data[:, 0], data[:,1])
plt.scatter(mean_col[0],mean_col[1], s =200, c = 'blue', marker = 'X', alpha=.5)
plt.title('IRIS MF-ers')
plt.xlabel('SepalWidth')
plt.ylabel('SepalLength')
plt.show()



# ''' Given two column vectors : 
# # A = 
# # ([ 1
# # 2
# # 3
# # ])
# # B = 
# # ([ 2
# #4
# # 5
# # ])
# The euclidean distance will be (A[i] - B[i])^2 ... then all added and squarerooted
# '''


def euclidean_dists(x, y):
  d = np.sum(np.square(x-y))
  return d

def cosin_sim(vec1, vec2):

    u = np.sum(np.square(vec1))
    v = np.sum(np.square(vec2))
    
    y = np.dot(vec1, vec2)/((u**.5)*(v**.5))
    
    return y

# def dist_mean(array, dist()):
#     mean = np.mean(array, 0)
#     shape = np.shape(array)
#     out = np.zeros(shape(0))
#     for i in range(shape(0)):
#       out[i] += dist(array[i], mean)
      

