import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from format_QX_Y import *

def fct_affiche_coeffcient(fonction_transfert_sos,a,b):
    QX_Yfct_fonction_transfert_sos = fct_format_QX_Y(fonction_transfert_sos)
    aq = fct_format_QX_Y(a)
    bq = fct_format_QX_Y(b)

    fe = 200000
    [w_sos, h_sos] = signal.sosfreqz(QX_Yfct_fonction_transfert_sos, worN=10000, fs=fe)
    [w_dft, h_dft] = signal.freqz(b, a, worN=10000, fs=fe)
    [w_dft_q, h_dft_q] = signal.freqz(bq, aq, worN=10000, fs=fe)
    plt.figure()

    plt.semilogx(w_dft, 20 * np.log10(np.abs(h_dft)))
    plt.semilogx(w_sos, 20 * np.log10(np.abs(h_sos)))
    plt.semilogx(w_dft_q, 20 * np.log10(np.abs(h_dft_q)))
    plt.title(f"Réponse en fréquence des filtre elliptique")
    plt.xlabel("Fr/uence [Hz]")
    plt.ylabel("Gain [dB]")
    plt.grid(which="both", axis="both")
    plt.tight_layout()
    plt.show()
