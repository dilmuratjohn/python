import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

train = pd.read_excel('stats.xls', sheet_name='train')
test = pd.read_excel('stats.xls', sheet_name='test')
print(train.head())
print(test.head())

array_train = train.values
array_test = test.values

X = array_train[0:, 1:11]
y = np.asarray(train['状态'], dtype="|S6")
X_test = array_test[0:, 1:11]


names = [
    "Nearest Neighbors",
    "Linear SVM",
    "RBF SVM",
    "Neural Net",
    "Gaussian Process",
    "Decision Tree",
    "Naive Bayes",
    "Random Forest"
]

classifiers = [
    KNeighborsClassifier(),
    SVC(kernel="linear"),
    SVC(),
    MLPClassifier(),
    GaussianProcessClassifier(),
    DecisionTreeClassifier(),
    GaussianNB(),
    RandomForestClassifier(),
]

for clf, names in zip(classifiers, names):
    clf.fit(X, y)
    clf.predict(X_test)
    print('#', names, '-- score:', clf.score(X_test, np.asarray(test['状态'], dtype="|S6")))
