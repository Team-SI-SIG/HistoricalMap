#! /usr/bin/python3

"""!@brief Accuracy index by Mathieu Fauvel
"""
from __future__ import annotations

import numpy as np


class CONFUSION_MATRIX:
    def __init__(self):
        self.confusion_matrix = None
        self.OA = None
        self.Kappa = None

    def compute_confusion_matrix(self, yp, yr):
        """
        Compute the confusion matrix
        """
        # Initialization
        n = yp.size
        C = int(yr.max())
        self.confusion_matrix = np.zeros((C, C))

        # Compute confusion matrix
        for i in range(n):
            self.confusion_matrix[yp[i].astype(int) - 1, yr[i].astype(int) - 1] += 1

        # Compute overall accuracy
        self.OA = np.sum(np.diag(self.confusion_matrix)) / n

        # Compute Kappa
        nl = np.sum(self.confusion_matrix, axis=1)
        nc = np.sum(self.confusion_matrix, axis=0)
        self.Kappa = ((n**2) * self.OA - np.sum(nc * nl)) / (n**2 - np.sum(nc * nl))

        # TBD Variance du Kappa
