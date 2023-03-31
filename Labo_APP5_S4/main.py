from filtre_elliptique import fct_filtre_elliptique
from fct_zplane import fonction_zplane
from reponse_impulsionnelle import fct_reponse_impulsionnelle
from coefficient_sos import fct_coefficient_sos
from Affiche_coefficient import fct_affiche_coeffcient
import matplotlib.pyplot as plt
import numpy as np
from creation_Filtrage_FIR import *
from Creation_deux_sinus import*
from Filtrage_signaux import*
#from format_QX.Y import *
# plt.ion()  # Comment out if using scientific mode!
fe = 20000
#a,b,h_dft,w = fct_filtre_elliptique(fe)
#z, p, k = fonction_zplane(a, b)

#fct_reponse_impulsionnelle(a,b)

#fonction_transfert_sos = fct_coefficient_sos(a,b)

#fct_affiche_coeffcient(fonction_transfert_sos,a,b)
filtre_p_b,filtre_p_h = filtre_FIR()
# Grand_X1,Grand_X2 = sinus()
# fct_filtrage_signaux(Grand_X1,Grand_X2,filtre_p_b,filtre_p_h)
#
# print('Done')



