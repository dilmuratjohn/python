from sklearn.model_selection import GridSearchCV
import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
train = pd.read_excel('stats.xls', sheet_name='train')
test = pd.read_excel('stats.xls', sheet_name='test')


array_train = train.values
array_test = test.values

X = array_train[0:, 1:11]
y = np.asarray(train['状态'], dtype="|S6")
X_test = array_test[0:, 1:11]

# Set the parameters by cross-validation
# MLPClassifier(hidden_layer_sizes=(100,), activation='identity', solver='adam', alpha=0.01,
#               batch_size='auto', learning_rate='adaptive', learning_rate_init=0.0001,
#               power_t=0.5, max_iter=200000, shuffle=True, random_state=None, tol=0.0001,
#               verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
#               early_stopping=False, validation_fraction=0.2, beta_1=0.9, beta_2=0.99, epsilon=1e-08),

tuned_parameters = [{'learning_rate_init': [0.001, 0.002, 0.003],
                     'alpha': [0.01, 0.05,  0.1, 0.5],
                     'power_t': [0.2, 0.3, 0.4, 0.5],
                     'momentum':[0.5, 0.6, 0.7, 0.8, 0.9],
                     'validation_fraction':[0.1, 0.2, 0.3, 0.4, 0.5]
                      }]

scores = ['precision', 'recall']

for score in scores:
    print("# Tuning hyper-parameters for %s" % score)
    print()

    clf = GridSearchCV(MLPClassifier(), tuned_parameters, cv=5,
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

