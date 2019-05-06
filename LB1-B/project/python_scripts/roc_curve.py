import matplotlib.pyplot as plt
import sys
from sklearn.metrics import roc_curve, auc


def get_data(dataf):
    """Extract data and the respective labels from a file"""
    with open(dataf) as f:
        label = []
        e_val = []
        for line in f:
            label.append(float(line.split()[1]))
            e_val.append(-1 * float(line.split()[0]))
    return label, e_val


def roc2(fpr, tpr, roc_auc):
    """Print a ROC curve given lists of coordinates (fpr, tpr)"""
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=1, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic')
    plt.legend(loc="lower right")
    plt.show()


if __name__ == '__main__':
    ''' usage: python roc_curve.py labeled_data.txt
     labeled data comprises both pos and neg data, each with its label'''
    labeled_data = sys.argv[1]
    # The input data is split into labels and e-values
    label, e_val = get_data(labeled_data)
    # function below takes in input the labels and the "predictions" (aka e-val)
    # and returns a list of FPRs and TPRs
    fpr, tpr, thresholds = roc_curve(label, e_val, pos_label=1)
    roc_auc = auc(fpr, tpr)  # computation of area under ROC curve
    print(roc_auc, len(thresholds))
    roc2(fpr, tpr, roc_auc)
    # roc1(fpr, tpr, roc_auc)
