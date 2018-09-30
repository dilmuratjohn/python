import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesClassifier

train = pd.read_excel('stats.xls', sheet_name='train')
test = pd.read_excel('stats.xls', sheet_name='test')


array_train = train.values
array_test = test.values

X = array_train[0:, 1:11]
y = np.asarray(train['状态'], dtype="|S6")
X_test = array_test[0:, 1:11]

# Build a forest and compute the feature importance
forest = ExtraTreesClassifier(n_estimators=250,
                              random_state=0)

forest.fit(X, y)
importance = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
indices = np.argsort(importance)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in range(X.shape[1]):
    print("%d. feature %d (%f)" % (f + 1, indices[f], importance[indices[f]]))

# Plot the feature importance of the forest
plt.figure()
plt.title("Feature importance")
plt.bar(range(X.shape[1]), importance[indices], color="r", yerr=std[indices], align="center")
plt.xticks(range(X.shape[1]), indices)
plt.xlim([-1, X.shape[1]])
plt.show()
