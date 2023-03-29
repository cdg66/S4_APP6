import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from QXY import *

def fct_coefficient_sos(fech, a,b):
    normal = [a,b]
    # Filter specifications
    fc_low: float = 900
    fc_high: float = 1100
    filter_order: int = 2
    pass_band_ripple_db: float = 1
    stop_band_attn_db: float = 40
    X = 2
    Y =13
    aq = convert_to_QXY(a,X,Y)
    bq = convert_to_QXY(b, X, Y)
    aq = convert_from_QXY(aq, X, Y)
    bq = convert_from_QXY(bq, X, Y)
    # Filter coefficients
    sos = signal.ellip(
        N=filter_order,
        rp=pass_band_ripple_db,
        rs=stop_band_attn_db,
        Wn=[fc_low, fc_high],
        fs=fech,
        btype="bandpass",
        output="sos",
    )
    print(sos)
    sosq = sos
    sosq = convert_to_QXY(sos, X, Y)

    print(sosq)
    sosq = convert_from_QXY(sosq, X, Y)

    print(sosq)
    # Frequency response
    [w_sos, h_sos] = signal.sosfreqz(sosq, worN=10000, fs=fech)
    [w_dft, h_dft] = signal.freqz(b, a, worN=10000, fs=fech)
    [w_dft_q, h_dft_q] = signal.freqz(bq, aq, worN=10000, fs=fech)
    #plot
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

