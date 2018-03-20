import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from sklearn.naive_bayes import GaussianNB
from sklearn.calibration import CalibratedClassifierCV
import get_data_from_excel


def main():
    file = 'train.xls'
    sheet1 = get_data_from_excel.GetData(file, 0)
    sheet2 = get_data_from_excel.GetData(file, 4)
    sheet3 = get_data_from_excel.GetData(file, 1)
    train_x = sheet1.get_data_by_columns(2)
    test_x = sheet2.get_data_by_columns(2)
    test_x2 = sheet3.get_data_by_columns(2)
    train_y = []
    test_y = []
    for i in range(0, 2880):
        train_y.append(1)
    for i in range(0, 168):
        test_y.append(0)

    x = np.append(train_x, test_x)
    y = np.append(train_y, test_y)
    print(x, y)
    x1 = np.asarray(x)
    y1 = np.asarray(y)
    print(x1, y1)
    clf = GaussianNB()
    clf.fit(np.array(x1), np.array(y1))

    #print(clf.predict(test_x2))


if __name__ == "__main__":
    main()


