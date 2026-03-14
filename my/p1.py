# import statsmodels.api as sm
# import pandas as pd
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# df = pd.DataFrame({'x':x, 'y':y})

# X = df['x']
# y = df['y']

# X = sm.add_constant(X)

# model = sm.OLS(y,X).fit()

# print(f'기울기: {model.params['x']}')
# print(f'절편: {model.params['const']}')


# import statsmodels.api as sm
# import matplotlib.pyplot as plt
# import pandas as pd

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# df = pd.DataFrame({'x':x, 'y':y})

# X = df['x']
# y = df['y']

# X_pred = sm.add_constant(X)

# model = sm.OLS(y,X).fit()

# y_pred = model.predict(X)

# plt.title('Linear Regression')
# plt.scatter(X, y)
# plt.plot(X,y_pred,color='red')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# from sklearn.linear_model import LogisticRegression

# X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
# y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]

# model = LogisticRegression()

# model.fit(X, y)

# new_data = [[4.5],[6.5]]

# pred = model.predict(new_data)

# print('예측 결과:',pred)


# from scipy.optimize import root

# def f(x):
#     return (x-3)**2

# sol = root(f,0)

# print(f"근: {sol.x}")

# from scipy.stats import describe

# A = [80, 85, 90, 75, 95]

# stats = describe(A)

# print("데이터 개수:", stats.nobs)
# print("최솟값:", stats.minmax[0])
# print("최댓값:", stats.minmax[1])
# print("평균:", stats.mean)
# print("분산:", stats.variance)
# print("왜도:", stats.skewness)
# print("첨도:", stats.kurtosis)

# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# data = np.random.normal(loc=50, scale=10, size=1000)

# sns.histplot(data, bins=30)

# plt.title("Histogram of Normal Distribution")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()


# import seaborn as sns
# import matplotlib.pyplot as plt

# data = sns.load_dataset('tips')

# sns.boxplot(data,x='day', y='total_bill')
# plt.title("Total Bill by Day")
# plt.xlabel("Day")
# plt.ylabel("Total Bill")
# plt.show()

import cv2

path = r"my\sample.jpg"

image = cv2.imread(path)

print(image.)
# cv2.cvtColor(image, )


# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows