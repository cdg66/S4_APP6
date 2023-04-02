from filtre_elliptique import fct_filtre_elliptique
import matplotlib.pyplot as plt
import numpy as np
from window import*
from C_header import PY2C
from creation_Filtrage_FIR import *
#from format_QX.Y import *
# plt.ion()  # Comment out if using scientific mode!
fe = 20000
coupe_bande_Q2_5 = fct_filtre_elliptique(fe)

PB_Q2_13,PH_Q2_13,Passe_bande_1k_Q2_13,Passe_bande_2k_Q2_13,Passe_bande_3500_Q2_13 = filtre_FIR()

# H7 low_passe
# H6 Bandpass filter 1000HZ
# H5 Bandpass filter 2000HZ
# H4 Bandpass filter 3500HZ
# H3 hight_pass
PY2C(PB_Q2_13,'H7.h',PYtype=int,Ctype='int32c',includesanddef=['#include "dsplib_dsp.h"'],varname='H7', gard='FIR_LOW_PASS_H', static=1)
PY2C(PH_Q2_13,'H3.h',PYtype=int,Ctype='int32c',includesanddef=['#include "dsplib_dsp.h"'],varname='H3', gard='FIR_HIGH_PASS_H', static=1)
PY2C(Passe_bande_1k_Q2_13,'H6.h',PYtype=int,Ctype='int32c',includesanddef=['#include "dsplib_dsp.h"'],varname='H6', gard='FIR_PASSE_BANDE_1K_H', static=1)
PY2C(Passe_bande_2k_Q2_13,'H5.h',PYtype=int,Ctype='int32c',includesanddef=['#include "dsplib_dsp.h"'],varname='H5', gard='FIR_PASSE_BANDE_1K_H', static=1)
PY2C(Passe_bande_3500_Q2_13,'H4.h',PYtype=int,Ctype='int32c',includesanddef=['#include "dsplib_dsp.h"'],varname='H4', gard='FIR_PASSE_BANDE_3500_H', static=1)
PY2C(coupe_bande_Q2_5,'Coupe_bande_FIR_coeffs.h',PYtype=int,Ctype='int32c',includesanddef=['#include "dsplib_dsp.h"'],varname='Coefficient_IIR_Coupe_bande', gard='FIR_COUPE_BANDE_H', static=1)
hanning_header()




