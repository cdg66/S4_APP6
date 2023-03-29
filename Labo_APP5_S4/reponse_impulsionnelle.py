import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
def fct_reponse_impulsionnelle(a,b):

    # Création de l'impulsion unité de longueur 1000
    N = 1000
    impulse = np.zeros(N)
    impulse[0] = 1

    # Calcul de la réponse impulsionnelle tronquée
    h = signal.lfilter(b, a, impulse)

    # Affichage de la réponse impulsionnelle tronquée
    plt.figure()
    plt.plot(np.arange(N), h)
    plt.title("Réponse impulsionnelle")
    plt.xlabel("Indice")
    plt.ylabel("Amplitude")
    plt.show()
