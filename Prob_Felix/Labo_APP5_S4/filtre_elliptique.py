import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from Format_Q2_5 import*
def fct_filtre_elliptique(fe: float):
    """
    Problème 1: Filtre IIR elliptique
    """
    # Filter specifications
    fc_low: float = 950
    fc_high: float = 1050
    filter_order: int = 4
    pass_band_ripple_db: float = 1
    stop_band_attn_db: float = 75

    # Filter coefficients
    [b, a] = signal.ellip(
        N=filter_order,
        rp=pass_band_ripple_db,
        rs=stop_band_attn_db,
        Wn=[fc_low, fc_high],
        fs=fe,
        btype="bandstop",
        output="ba",
    )

    # Frequency response
    [w, h_dft] = signal.freqz(b, a, worN=10000, fs=fe)
    plt.figure()
    plt.semilogx(w, 20 * np.log10(np.abs(h_dft)), label="Unscaled coeffs")

    # Filter coefficients
    H_transfert = signal.ellip(
        N=filter_order,
        rp=pass_band_ripple_db,
        rs=stop_band_attn_db,
        Wn=[fc_low, fc_high],
        fs=fe,
        btype="bandstop",
        output="sos",
    )
    coupe_bande_fft = np.fft.fft(H_transfert)
    coupe_bande_Q2_5 = fct_format_Q2_5(coupe_bande_fft)



    H_transfert = H_transfert * np.power(2, 5)
    H_transfert = np.round(H_transfert)
    H_QX = H_transfert / np.power(2, 5)
    # Frequency response
    [w_Q25, h_dft_Q25] = signal.sosfreqz(H_QX, worN=100000, fs=fe)
    plt.semilogx(w_Q25, 20 * np.log10(np.abs(h_dft_Q25)), '--', label="Q2.5 coeffs")

    plt.title(f"Réponse en fréquence du filtre elliptique (ordre {filter_order})")
    plt.xlabel("Fréquence [Hz]")
    plt.ylabel("Gain [dB]")
    plt.grid(which="both", axis="both")
    plt.tight_layout()
    plt.legend()
    plt.show()
    coupe_bande_Q2_5 = coupe_bande_Q2_5.ravel()
    return coupe_bande_Q2_5
#
# def fct_filtre_elliptique(fe: float):
#     """
#     ProblÃ¨me 1: Filtre IIR elliptique
#     """
#     # Filter specifications
#     fc_low: float = 950
#     fc_high: float = 1050
#     filter_order: int = 4
#     pass_band_ripple_db: float = 1
#     stop_band_attn_db: float = 75
#
#     # Filter coefficients
#     [b, a] = signal.ellip(
#         N=filter_order,
#         rp=pass_band_ripple_db,
#         rs=stop_band_attn_db,
#         Wn=[fc_low, fc_high],
#         fs=fe,
#         btype="bandstop",
#         output="ba",
#     )
#
#     # Frequency response
#     [w, h_dft] = signal.freqz(b, a, worN=10000, fs=fe)
#     plt.figure()
#     plt.semilogx(w, 20 * np.log10(np.abs(h_dft)))
#     plt.title(f"Réponse en fréquence du filtre elliptique (ordre {filter_order})")
#     plt.xlabel("Fréquence [Hz]")
#     plt.ylabel("Gain [dB]")
#     plt.grid(which="both", axis="both")
#     plt.tight_layout()
#     plt.show()
#
#     # Filter coefficients
#     H_transfert = signal.ellip(
#         N=filter_order,
#         rp=pass_band_ripple_db,
#         rs=stop_band_attn_db,
#         Wn=[fc_low, fc_high],
#         fs=fe,
#         btype="bandstop",
#         output="sos",
#     )
#     H_transfert = H_transfert * np.power(2, 5)
#     H_transfert = np.round(H_transfert)
#     H_QX = H_transfert / np.power(2, 5)
#     # Frequency response
#     [w_Q25, h_dft_Q25] = signal.sosfreqz(H_QX, worN=100000, fs=fe)
#     plt.figure()
#     plt.semilogx(w_Q25, 20 * np.log10(np.abs(h_dft_Q25)))
#     plt.title(f"Réponse en fréquence du filtre elliptique (ordre {filter_order})")
#     plt.xlabel("Fréquence [Hz]")
#     plt.ylabel("Gain [dB]")
#     plt.grid(which="both", axis="both")
#     plt.tight_layout()
#     plt.show()
#     return a,b,h_dft,w