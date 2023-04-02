from filtre_elliptique import fct_filtre_elliptique
import matplotlib.pyplot as plt
import numpy as np
from window import*
from C_header import PY2C
from creation_Filtrage_FIR import *
from Coupe_bande_header import*
import os
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
machine = os.name
rootdir = ""
if (machine == 'nt'):
    rootdir = 'C:/Users/Felix/Documents/GitHub/S4_APP6/APP6_Problematique.X/'
if (machine == 'posix'):
    rootdir = '../../APP6_Problematique.X/'
PY2C(PB_Q2_13,rootdir + 'H7.h',complex=1,PYtype=int,Ctype='int32c',includesanddef=['#include "dsplib_dsp.h"'],varname='H7', gard='FIR_LOW_PASS_H', static=1)
PY2C(PH_Q2_13,rootdir + 'H3.h',complex=1,PYtype=int,Ctype='int32c',includesanddef=['#include "dsplib_dsp.h"'],varname='H3', gard='FIR_HIGH_PASS_H', static=1)
PY2C(Passe_bande_1k_Q2_13,rootdir + 'H6.h',complex=1,PYtype=int,Ctype='int32c',includesanddef=['#include "dsplib_dsp.h"'],varname='H6', gard='FIR_PASSE_BANDE_1K_H', static=1)
PY2C(Passe_bande_2k_Q2_13,rootdir + 'H5.h',complex=1,PYtype=int,Ctype='int32c',includesanddef=['#include "dsplib_dsp.h"'],varname='H5', gard='FIR_PASSE_BANDE_1K_H', static=1)
PY2C(Passe_bande_3500_Q2_13,rootdir + 'H4.h',complex=1,PYtype=int,Ctype='int32c',includesanddef=['#include "dsplib_dsp.h"'],varname='H4', gard='FIR_PASSE_BANDE_3500_H', static=1)
header_coupe_bande(coupe_bande_Q2_5,rootdir+ 'filterIIRcoeffs_TEST.h')
#genrate hanning window
length = 768
hanning = np.hanning(length)
hanning = fct_format_Q2_13(hanning)
PY2C(hanning,rootdir + 'window_header.h',complex=0,PYtype=int,Ctype='int32_t',varname='window', gard='WINDOW_HEADER_H', static=0)
#hanning_header(rootdir + 'window_header.h')




