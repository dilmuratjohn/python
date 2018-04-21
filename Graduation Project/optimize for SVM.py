from sklearn.model_selection import GridSearchCV
import numpy as np
import pandas as pd
from sklearn.svm import SVC

train = pd.read_excel('stats.xls', sheet_name='train')
test = pd.read_excel('stats.xls', sheet_name='test')


array_train = train.values
array_test = test.values

X = array_train[0:, 1:11]
y = np.asarray(train['状态'], dtype="|S6")
X_test = array_test[0:, 1:11]

# Set the parameters by cross-validation
tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1, 0.1,  0.01, 0.001],
                     'C': [1, 10, 100, 1000], 'degree':[1, 2, 3, 4, 5], 'tol':[1, 0.1, 0.01, 0.001]}]

scores = ['precision', 'recall']

for score in scores:
    print("# Tuning hyper-parameters for %s" % score)
    print()

    clf = GridSearchCV(SVC(), tuned_parameters, cv=5,
                       scoring='%s_macro' % score)
    clf.fit(X, y)

    print("Best parameters set found on development set:")
    print()
    print(clf.best_params_)
    print()
    print("Grid scores on development set:")
    print()
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
        print("%0.3f (+/-%0.03f) for %r"
              % (mean, std * 2, params))
    print()

    print("Detailed classification report:")
    print()
    print("The model is trained on the full development set.")
    print("The scores are computed on the full evaluation set.")
    print()

