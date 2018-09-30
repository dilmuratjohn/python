import numpy as np
from sklearn.model_selection import validation_curve
from sklearn.linear_model import Ridge
import pandas as pd

train = pd.read_excel('stats.xls', sheet_name='train')
test = pd.read_excel('stats.xls', sheet_name='test')


array_train = train.values
array_test = test.values

X = array_train[0:, 1:11]
y = np.asarray(train['状态'], dtype="|S6")
X_test = array_test[0:, 1:11]

indices = np.arange(y.shape[0])
np.random.shuffle(indices)
X, y = X[indices], y[indices]

train_scores, valid_scores = validation_curve(Ridge(), X, y, "alpha")



