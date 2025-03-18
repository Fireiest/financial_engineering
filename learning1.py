import numpy as np
import matplotlib.pyplot as plt


# #### Exercise 1 ####
# mean = 0
# variance = 1
# std_dev = np.sqrt(variance)
#
# arry = np.random.normal(loc=mean, scale = std_dev, size=1000)
# arry2 = np.random.normal(loc=mean, scale = std_dev, size=1000)
# plt.plot(arry)
# plt.show()
# plt.hist(arry, bins=20, edgecolor='b')
# plt.show()
#
#
#
# #### Exercise 2 ####
# X = np.linspace(0,10,1000)
#
# m = 2
# c = 1
#
# noise = np.random.normal(0,2,1000)
# y = m * X + c + noise
#
# plt.scatter(X, y)
# plt.show()
#
#
#
# #### Exercise 3 ####
# plt.plot(arry.cumsum())
# plt.show()



#### Ecercise 4 ####

mean = [0,0]
cov_matrix = [
                [1, -0.5],
                [-0.5, 2]
             ]

samples = np.random.multivariate_normal(mean, cov_matrix, size= 1000)
# print(samples)

x, y = samples[:, 0], samples[:, 1]

plt.scatter(x, y)
plt.show()


#### Exercise 5 ####
N = len(x)

mean_x = sum(x) / N
mean_y = sum(y) / N

print(mean_x)
print(mean_y)


