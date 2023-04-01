from filtre_elliptique import fct_filtre_elliptique
import matplotlib.pyplot as plt
import numpy as np
from creation_Filtrage_FIR import *
#from format_QX.Y import *
# plt.ion()  # Comment out if using scientific mode!
fe = 20000
a,b,h_dft,w = fct_filtre_elliptique(fe)

filtre_p_b,filtre_p_h = filtre_FIR()



