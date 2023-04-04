import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

def fenetre_signal_2k():
    fe = 20000
    f = 2000
    N = 1024
    n1 = np.arange(0, N, 1)
    x1 = np.sin((np.pi * f * n1)/fe)
    # X1 = np.fft.fftshift(np.fft.fft(x1))


    window = np.hanning(N)
    hanning_signal = x1 * window
    hanning_signal = np.fft.fft(hanning_signal)
    rectangle_signal = np.fft.fft(x1)

    freq = np.fft.fftshift(np.fft.fftfreq(N, 1/fe))
    # Afficher les signaux
    fig, ax = plt.subplots(figsize=(8, 6))

    ax.plot(n1, 20 * np.log10(np.abs(hanning_signal)), label='Hanning')
    ax.plot(n1, 20 * np.log10(np.abs(rectangle_signal)), label='Rectangular')
    ax.tick_params(axis='both', which='major', labelsize=16, width=2)
    ax.set_title('Comparaison des spectres du sinus de 2k avec différentes fenêtres', fontsize=16)
    # ax.set_xlim([10, fe/2])
    # ax.set_ylim([-80, 10])
    ax.set_xlabel('Fréquence k', fontsize=16)
    ax.set_ylabel('Amplitude (dB)', fontsize=16)
    ax.legend()
    ax.grid()

    plt.tight_layout()
    plt.show()

    # # Afficher les signaux
    # fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
    #
    # ax1.semilogx(freq, 20*np.log10(np.abs(hanning_signal)), label='Hanning')
    # ax1.tick_params(axis='both', which='major', labelsize=16, width=2)
    # ax1.set_title('Spectre du sinus de 2k avec fenêtre de hanning', fontsize=16)
    # # ax1.set_xlim([10, fe/2])
    # # ax1.set_ylim([-80, 10])
    # ax1.set_xlabel('Fréquence (Hz) en log', fontsize=16)
    # ax1.set_ylabel('Amplitude (dB)', fontsize=16)
    # ax1.legend()
    # ax1.grid()
    #
    # ax2.semilogx(freq, 20*np.log10(np.abs(rectangle_signal)), label='Rectangular')
    # ax2.tick_params(axis='both', which='major', labelsize=16, width=2)
    # # ax2.set_xlim([10, fe/2])
    # # ax2.set_ylim([-80, 10])
    # ax2.set_title('Spectre du sinus de 2k avec fenêtre rectangulaire', fontsize=16)
    # ax2.set_xlabel('Fréquence (Hz) en log', fontsize=16)
    # ax2.set_ylabel('Amplitude (dB)', fontsize=16)
    # ax2.legend()
    # ax2.grid()
    #
    # plt.tight_layout()
    # plt.show()
