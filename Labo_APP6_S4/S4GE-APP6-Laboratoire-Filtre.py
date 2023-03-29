import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from filtre_elliptique import fct_filtre_elliptique
from reponse_impulsionnelle import fct_reponse_impulsionnelle
from coefficient_sos import fct_coefficient_sos
from zplane import zplane
from FIR import *


def probleme_1(fe: float):
    """
    ProblÃ¨me 1: Filtre IIR elliptique
    """

    # Filter specifications
    fc_low: float = 900
    fc_high: float = 1100
    filter_order: int = 2
    pass_band_ripple_db: float = 1
    stop_band_attn_db: float = 40

    # Filter coefficients
    [b, a] = signal.ellip(
        N=filter_order,
        rp=pass_band_ripple_db,
        rs=stop_band_attn_db,
        Wn=[fc_low, fc_high],
        fs=fe,
        btype="bandpass",
        output="ba",
    )

    # Frequency response
    [w, h_dft] = signal.freqz(b, a, worN=10000, fs=fe)
    plt.figure()
    plt.semilogx(w, 20 * np.log10(np.abs(h_dft)))
    plt.title(f"RÃ©ponse en frÃ©quence du filtre elliptique (ordre {filter_order})")
    plt.xlabel("FrÃ©quence [Hz]")
    plt.ylabel("Gain [dB]")
    plt.grid(which="both", axis="both")
    plt.tight_layout()
    plt.show()

    #Pole and zero map
    zplane(b,a)
    #impulse response
    fct_reponse_impulsionnelle(a, b)

    #SOS
    fct_coefficient_sos(fe,a,b)

    #FIR
    filtre_FIR()



def laboratoire():
    #plt.ion()  # Comment out if using scientific mode!

    fe = 20000
    probleme_1(fe)
    print("Done!")


if __name__ == "__main__":
    laboratoire()
