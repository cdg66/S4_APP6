import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def fct_format_QX_Y(H_transfert):

    H_transfert = H_transfert * np.power(2, 13)
    H_transfert = np.round(H_transfert)
    H_QX = H_transfert / np.power(2, 13)
    return H_QX