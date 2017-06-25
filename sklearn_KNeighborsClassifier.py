# https://www.youtube.com/watch?v=EvV99YhSsJU
import numpy as np

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
iris_X = iris.data
iris_Y = iris.target
#print(iris_X[:])
print(iris_X[:2,:])
print(iris_Y)

x_train, x_test, y_train, y_test = train_test_split(
    iris_X, iris_Y, test_size=0.3
)

print(y_train)

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
print(knn.predict(x_test))
print(y_test)