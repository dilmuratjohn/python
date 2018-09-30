import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn import metrics


train = pd.read_excel('stats.xls', sheet_name='train')
test = pd.read_excel('stats.xls', sheet_name='test')


array_train = train.values
array_test = test.values

X = array_train[0:, 1:11]
y = np.asarray(train['状态'], dtype="|S6")
X_test = array_test[0:, 1:11]

# ----------------------------------------------------------------------------------------------------------------------

names = [
    "RBF SVM",
    "Neural Net",
    "Naive Bayes",
    "Random Forest"
]

classifiers = [
    # SVC(C=1.0, kernel='rbf', degree=4, gamma=1, tol=0.001),
    # MLPClassifier(hidden_layer_sizes=(10000,), activation='identity', solver='adam', alpha=0.01,
    #               batch_size='auto', learning_rate='adaptive', learning_rate_init=0.0001,
    #               power_t=0.5, max_iter=200000, shuffle=True, random_state=None, tol=0.0001,
    #               verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
    #               early_stopping=False, validation_fraction=0.2, beta_1=0.9, beta_2=0.99, epsilon=1e-08),
    # GaussianNB(),
    RandomForestClassifier(n_estimators=10, criterion='gini', max_depth=None, min_samples_split=2,
                           min_samples_leaf=1, min_weight_fraction_leaf=0.2, max_features='auto',
                           max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None,
                           bootstrap=True, oob_score=False, n_jobs=1, random_state=None, verbose=0,
                           warm_start=False, class_weight=None),
]

for clf, names in zip(classifiers, names):
    clf.fit(X, y)
    print(y, clf.predict(X_test))
    scores = cross_val_score(clf, X, y, cv=5)
    predicted = metrics.accuracy_score(y, cross_val_predict(clf, X, y, cv=5))
    print(names, '-- score:', clf.score(X_test, np.asarray(test['状态'], dtype="|S6")), scores, predicted, "Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

