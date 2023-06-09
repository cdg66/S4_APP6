import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def fct_format_Q2_13(H_transfert):

    H_transfert = H_transfert * np.power(2, 13)
    H_QX = np.round(H_transfert)
    #H_QX = H_transfert / np.power(2, 13)
    return H_QX

def fct_format_revert_Q2_13(H_transfert):

    H_QX = H_transfert / np.power(2, 13)
    return H_QX