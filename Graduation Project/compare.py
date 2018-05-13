import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
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
    "RBF SVM",
    "Neural Net",
    "Naive Bayes",
    "Random Forest"
]

classifiers = [
    SVC(C=1000, degree=1, gamma=0.001, kernel='rbf', tol=0.001),
    MLPClassifier(alpha=0.01, learning_rate_init=0.001, momentum=0.6, power_t=0.2, validation_fraction=0.2),
    GaussianNB(),
    RandomForestClassifier(criterion='entropy', max_depth=5, min_samples_leaf=3, min_samples_split=5, n_estimators=1),
]

for clf, names in zip(classifiers, names):
    clf.fit(X, y)
    clf.predict(X_test)
    print('#', names, '-- score:', clf.score(X_test, np.asarray(test['状态'], dtype="|S6")))
