import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def fct_format_Q2_5(H_transfert):

    H_transfert = H_transfert * np.power(2, 5)
    H_QX = np.round(H_transfert)
    return H_QX