from filtre_elliptique import fct_filtre_elliptique
from fct_zplane import fonction_zplane
from reponse_impulsionnelle import fct_reponse_impulsionnelle
from coefficient_sos import fct_coefficient_sos
#plt.ion()  # Comment out if using scientific mode!
fe = 20000
a, b = fct_filtre_elliptique(fe)
z, p, k = fonction_zplane(a, b)

fct_reponse_impulsionnelle(a,b)

fct_coefficient_sos(a,b)

