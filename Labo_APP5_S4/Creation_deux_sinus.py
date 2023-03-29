import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def sinus():
    fc = 2000
    fe = 20000
    N = 512
    n1 = np.arange(0, 4*N)
    n2 = np.arange(0, 4*N)
    A1 = 1
    A2 = 1
    f1 = 200
    f2 = 2000
    x1 = A1*np.sin(2*np.pi*f1*n1/fe)
    x2 = A2*np.sin(2*np.pi*f2*n2/fe)

    fig, axs = plt.subplots(2, 1)

    axs[0].plot(n1,x1)
    axs[0].set_title('Sinus à 200Hz')
    axs[0].set_xlabel('n')
    axs[0].set_ylabel('x[n]')
    #axs[1].plot(n2[0:500],x2[0:500])
    axs[1].plot(n2, x2)
    axs[1].set_title('Sinus à 2KHz')
    axs[1].set_xlabel('n')
    axs[1].set_ylabel('x[n]')
    plt.tight_layout()
    plt.show()

    Grand_X1 = np.fft.fft(x1)
    '''
    code bin pratique pour trouver la fréquence de la fondamentale pour debuger 
    k1 = Grand_X1[Grand_X1 >= 0].argmax()
    delta_f = fe/(4*N)
    fondamental_x1 = k1*delta_f
    print(fondamental_x1)
     '''
    Grand_X1_db = 20 * np.log10(Grand_X1)
    freq_x1 = np.fft.fftfreq(2048, d=1 / fe)
    positive_freq_x1 = freq_x1[freq_x1 >= 0]
    Grand_X1_positive = Grand_X1_db[freq_x1 >= 0]
    '''
    code bin pratique pour trouver la fréquence de la fondamentale pour debuger
    k2 = Grand_X2.argmax()
    delta_f = fe / (4 * N)
    fondamental_x2 = k2 * delta_f
    print(fondamental_x1)
     '''
    Grand_X2 = np.fft.fft(x2)
    Grand_X2_db = 20 * np.log10(Grand_X2)
    freq_x2 = np.fft.fftfreq(2048, d=1 / fe)
    positive_freq_x2 = freq_x2[freq_x2 >= 0]
    Grand_X2_positive = Grand_X2_db[freq_x2 >= 0]

    fig1, axs1 = plt.subplots(2, 1)
    axs1[0].plot(positive_freq_x1, np.abs(Grand_X1_positive))
    axs1[0].set_title('Spectre du sinus a 200Hz')
    axs1[0].set_xlabel('Amplitude en dB')
    axs1[0].set_ylabel('Fréquence en Hz')
    axs1[0].set_xscale('log')
    axs1[0].set_yscale('log')
    axs1[1].plot(positive_freq_x2, np.abs(Grand_X2_positive))
    axs1[1].set_title('Spectre du sinus a 2000Hz')
    axs1[1].set_xlabel('Amplitude en dB')
    axs1[1].set_ylabel('Fréquence en Hz')
    axs1[1].set_xscale('log')
    axs1[1].set_yscale('log')
    plt.tight_layout()
    plt.show()
    return Grand_X1,Grand_X2