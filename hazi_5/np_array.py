import numpy as np

def filter(path):
    """
    This function uses the following filters:
    1st column: most common item
    2nd column: above the average of the column
    3rd column: less than the median of the column
    """
    arr = np.genfromtxt(path, delimiter=',', skip_header=1)

    mean_cond = arr[:,1] > np.mean(arr[:,1])
    med_cond = arr[:,2] < np.median(arr[:,2])
    count_max_cond = arr[:,0] == np.bincount(arr[:,0].astype(int)).argmax()

    all_filter = arr[mean_cond & med_cond & count_max_cond]

    print(f'{np.shape(all_filter)[0]} row(s) meet(s) the conditions.')

filter('/Users/roland.kovacs4ibm.com/Downloads/height_weight.xls')