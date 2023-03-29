import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def fct_coefficient_sos():
    fe = 20000
    # Calcul des coefficients du filtre en format SOS
    [sos_a,sos_b] = signal.ellip(2, 1, 40, 1000, output="sos",fs=fe, btype='bandpass') # ordre, ripple, attenuation a fc, frequence, type de filtre,


    # Affichage du module (dB) de la réponse en fréquence
    w, h = signal.sosfreqz(sos_a,sos_b, fe, worN=100000)
    plt.figure()
    plt.semilogx(w, 20 * np.log10(np.abs(h)))
    plt.title("Réponse en fréquence (dB)")
    plt.xlabel("Fréquence (Hz)")
    plt.ylabel("Module (dB)")
    plt.grid(True, which="both", axis="both")
    plt.axvline(fe/2, color="green")
    plt.show()

    # Conversion des coefficients en format Q2.13
    sos_q2_13 = np.round(sos * 2**13) / 2**13
    a_q2_13, b_q2_13 = signal.sos2tf(sos_q2_13)

    # Affichage de la réponse en fréquence
    w, h = signal.freqz(b_q2_13, a_q2_13)
    plt.figure()
    plt.semilogx(w*fe/(2*np.pi), 20 * np.log10(np.abs(h)))
    plt.semilogx(w, 20 * np.log10(np.abs(h)))
    plt.title("Réponse en fréquence (dB)")
    plt.xlabel("Fréquence (Hz)")
    plt.ylabel("Module (dB)")
    plt.grid(True, which="both", axis="both")
    plt.axvline(fe/2, color="green")
    plt.show()
