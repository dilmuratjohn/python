import pandas as pd
import numpy as np
from time import time
import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesClassifier
train = pd.read_excel('stats.xls', sheet_name='train')
test = pd.read_excel('stats.xls', sheet_name='test')


array_train = train.values
array_test = test.values

X = array_train[0:, 1:11]
y = np.asarray(train['状态'], dtype="|S6")
X_test = array_test[0:, 1:11]



# Build a forest and compute the pixel importances
print("Fitting ExtraTreesClassifier on faces data with %d cores..." % n_jobs)
t0 = time()
forest = ExtraTreesClassifier(n_estimators=1000,
                              max_features=128,
                              random_state=0)

forest.fit(X, y)
print("done in %0.3fs" % (time() - t0))
importances = forest.feature_importances_
importances = importances.reshape(data.images[0].shape)

# Plot pixel importances
plt.matshow(importances, cmap=plt.cm.hot)
plt.title("Pixel importances with forests of trees")
plt.show()














#
# X_indices = np.arange(X.shape[-1])
#
# # #############################################################################
# # Univariate feature selection with F-test for feature scoring
# # We use the default selection function: the 10% most significant features
# selector = SelectPercentile(f_classif, percentile=10)
# selector.fit(X, y)
# scores = -np.log10(selector.pvalues_)
# scores /= scores.max()
# plt.bar(X_indices - .45, scores, width=.2,
#         label=r'Univariate score ($-Log(p_{value})$)', color='darkorange',
#         edgecolor='black')
#
# # #############################################################################
# # Compare to the weights of an SVM
# clf = svm.SVC(kernel='linear')
# clf.fit(X, y)
#
# svm_weights = (clf.coef_ ** 2).sum(axis=0)
# svm_weights /= svm_weights.max()
#
# plt.bar(X_indices - .25, svm_weights, width=.2, label='SVM weight',
#         color='navy', edgecolor='black')
#
# clf_selected = svm.SVC(kernel='linear')
# clf_selected.fit(selector.transform(X), y)
#
# svm_weights_selected = (clf_selected.coef_ ** 2).sum(axis=0)
# svm_weights_selected /= svm_weights_selected.max()
#
# plt.bar(X_indices[selector.get_support()] - .05, svm_weights_selected,
#         width=.2, label='SVM weights after selection', color='c',
#         edgecolor='black')
#
#
# plt.title("Comparing feature selection")
# plt.xlabel('Feature number')
# plt.yticks(())
# plt.axis('tight')
# plt.legend(loc='upper right')
# plt.show()