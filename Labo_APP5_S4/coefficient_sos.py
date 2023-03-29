import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def fct_coefficient_sos(a,b):
    fe = 20000
    # Filter specifications
    fc_low: float = 900
    fc_high: float = 1100
    filter_order: int = 2
    pass_band_ripple_db: float = 1
    stop_band_attn_db: float = 40
    # Calcul des coefficients du filtre en format SOS
    a_sos= signal.ellip(
        N=filter_order,
        rp=pass_band_ripple_db,
        rs=stop_band_attn_db,
        Wn=[fc_low, fc_high],
        fs=fe,
        btype="bandpass",
        output="sos",
    )
    # retourne les fréquence et la fonction de transfert
    return a_sos


