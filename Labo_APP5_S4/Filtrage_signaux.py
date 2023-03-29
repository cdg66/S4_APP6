import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def fct_filtrage_signaux(Grand_X1,Grand_X2,filtre_p_b,filtre_p_h):

    n = np.arange(512*4)


    #multiplication dans le domaine fréquenciel
    x1_p_b =Grand_X1*filtre_p_b
    x2_p_b = Grand_X2*filtre_p_b
    #ifft pour revenir dans le domaine temporel
    x1_p_b = np.fft.ifft(x1_p_b)
    x1_p_b = np.real(x1_p_b)

    x2_p_b = np.fft.ifft(x2_p_b)
    x2_p_b = np.real(x2_p_b)

    fig, axs = plt.subplots(2, 1)

    axs[0].plot(n,x1_p_b)
    axs[0].set_title('Sinus à 200Hz filtrer par le filtre passe-bas')
    axs[0].set_xlabel('n')
    axs[0].set_ylabel('x[n]')
    axs[1].plot(n,x2_p_b)
    axs[1].set_title('Sinus à 2KHz filtrer par le filtre passe-bas')
    axs[1].set_xlabel('n')
    axs[1].set_ylabel('x[n]')
    plt.tight_layout()
    plt.show()



    # pour le passe haut

    n = np.arange(512 * 4)

    # multiplication dans le domaine fréquenciel
    x1_p_h = Grand_X1 * filtre_p_h
    x2_p_h = Grand_X2 * filtre_p_h
    # ifft pour revenir dans le domaine temporel
    x1_p_h = np.fft.ifft(x1_p_h)
    x1_p_h = np.real(x1_p_h)

    x2_p_h = np.fft.ifft(x2_p_h)
    x2_p_h = np.real(x2_p_h)

    fig, axs = plt.subplots(2, 1)

    axs[0].plot(n, x1_p_h)
    axs[0].set_title('Sinus à 200Hz filtrer par le filtre passe-bas')
    axs[0].set_xlabel('n')
    axs[0].set_ylabel('x[n]')
    axs[1].plot(n, x2_p_h)
    axs[1].set_title('Sinus à 2KHz filtrer par le filtre passe-bas')
    axs[1].set_xlabel('n')
    axs[1].set_ylabel('x[n]')
    plt.tight_layout()
    plt.show()
