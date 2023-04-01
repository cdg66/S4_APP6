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


PY2C(PB_Q2_13,'High_pass_filterIIRcoeffs.h',PYtype=int,Ctype='int32c',includesanddef=['#include "dsplib_dsp.h"'],varname='Coefficient_Fir', gard='FIR_LOW_PASS_H', static=1)
PY2C(PH_Q2_13,'Low_pass_filterIIRcoeffs.h',PYtype=int,Ctype='int32c',includesanddef=['#include "dsplib_dsp.h"'],varname='Coefficient_Fir', gard='FIR_HIGH_PASS_H', static=1)
PY2C(Passe_bande_1k_Q2_13,'Bande_passe_1k_filterIIRcoeffs.h',PYtype=int,Ctype='int32c',includesanddef=['#include "dsplib_dsp.h"'],varname='Coefficient_Fir', gard='FIR_PASSE_BANDE_1K_H', static=1)
PY2C(Passe_bande_2k_Q2_13,'Bande_passe_2k_filterIIRcoeffs.h',PYtype=int,Ctype='int32c',includesanddef=['#include "dsplib_dsp.h"'],varname='Coefficient_Fir', gard='FIR_PASSE_BANDE_1K_H', static=1)
PY2C(Passe_bande_3500_Q2_13,'Bande_passe_3500_filterIIRcoeffs.h',PYtype=int,Ctype='int32c',includesanddef=['#include "dsplib_dsp.h"'],varname='Coefficient_Fir', gard='FIR_PASSE_BANDE_3500_H', static=1)
PY2C(coupe_bande_Q2_5,'Coupe_bande_filterIIRcoeffs.h',PYtype=int,Ctype='int32c',includesanddef=['#include "dsplib_dsp.h"'],varname='Coefficient_Fir', gard='FIR_COUPE_BANDE_H', static=1)
hanning_header()




