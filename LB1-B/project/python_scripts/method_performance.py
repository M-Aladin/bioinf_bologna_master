import sys
import numpy as np


def mat_print(mat):
    """prints the confusion matrix in the TP-FP/FN-TN format"""
    mat = reversed(mat)
    for i in mat:
        print(i[1], i[0])


def confusion_mat(filename, threshold):
    """File format must be, for each line, <e-value> <class label>"""
    f = open(filename)
    mat = [[0 for i in range(2)] for i in range(2)]
    for line in f:
        line = line.rstrip()
        fields = line.split()
        e_val = float(fields[0])
        actual = int(fields[1])
        if e_val > threshold:
            detected = 0  # the entry is detected as negative
        else:
            detected = 1  # the entry is detected as positive

        mat[detected][actual] += 1
    f.close()
    # [0,0] true negatives
    # [0,1] false negatives
    # [1,0] false positives
    # [1,1] true positives
    return mat


def print_performance(cm):
    """
    :param cm: confusion matrix
    :return: accuracy, correlation coefficient
    """
    acc = (cm[0][0] + cm[1][1]) / (cm[0][0] + cm[1][1] + cm[0][1] + cm[1][0])

    d = np.sqrt((cm[1][1] + cm[1][0]) * (cm[1][1] + cm[0][1]) * (cm[0][0] + cm[1][0]) * (cm[0][0] + cm[0][1]))
    mc = (cm[1][1] * cm[0][0] - cm[0][1] * cm[1][0]) / d
    print("Q2 =", acc, "MCC =", mc)
    # tpr = cm[1][1]/(cm[1][1]+cm[0][1])
    # fpr = cm[1][0]/([0][0]+[1][0])
    # print("TPR =", tpr, "FPR =", fpr)


if __name__ == "__main__":
    """Usage: python3 method_performance.py <datafile> <threshold>"""
    test_set = sys.argv[1]
    thresh = float(sys.argv[2])
    matrix = confusion_mat(test_set, thresh)
    print(thresh)
    mat_print(matrix)
    print_performance(matrix)
