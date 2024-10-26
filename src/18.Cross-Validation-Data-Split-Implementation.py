"""
Cross-Validation Data Split Implementation (medium)

Write a Python function that performs k-fold cross-validation data splitting from scratch. The function should take a 
dataset (as a 2D NumPy array where each row represents a data sample and each column represents a feature) and an 
integer k representing the number of folds. The function should split the dataset into k parts, systematically use one 
part as the test set and the remaining as the training set, and return a list where each element is a tuple containing 
the training set and test set for each fold.

Example:
        input: data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]), k = 5
        output: [[[[3, 4], [5, 6], [7, 8], [9, 10]], [[1, 2]]],
                [[[1, 2], [5, 6], [7, 8], [9, 10]], [[3, 4]]],
                [[[1, 2], [3, 4], [7, 8], [9, 10]], [[5, 6]]], 
                [[[1, 2], [3, 4], [5, 6], [9, 10]], [[7, 8]]], 
                [[[1, 2], [3, 4], [5, 6], [7, 8]], [[9, 10]]]]
        reasoning: The dataset is divided into 5 parts, each being used once as a test set while the remaining parts 
        serve as the training set.
"""

import numpy as np


def cross_validation_split(data, k, seed=42):
    np.random.seed(seed)
    np.random.shuffle(data)
    fold_size = int(np.ceil(len(data) / k))
    idx_start = np.arange(0, len(data), fold_size)
    idx_end = idx_start + fold_size
    idx_end[-1] = len(data) if idx_end[-1] >= len(data) else idx_end[-1]
    folds = [
        [np.concatenate((data[:i], data[j:]), axis=0).tolist(), data[i:j].tolist()] for i, j in zip(idx_start, idx_end)
    ]
    return folds


if __name__ == "__main__":
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    k = 5
    print(cross_validation_split(data, k))
