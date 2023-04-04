import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import numpy as np
from Format_Q2_13 import*
from Format_Q2_5 import*

def filtre_FIR():
    Fe = 20000
    N = 1024
    n = N
    n2 = 255

    #passe-bas
    fcpb = 500
    filtre_p_b: np.ndarray = signal.firwin(
        numtaps=n, cutoff=fcpb, pass_zero="lowpass", window="blackman", fs=Fe
    )
    filtre_p_b_fft = np.fft.fft(filtre_p_b)
    PB_Q2_13 =fct_format_Q2_13(filtre_p_b_fft)

    #filtre passe-haut
    fcph = 4490
    filtre_p_h: np.ndarray = signal.firwin(
        numtaps=n2, cutoff=fcph, pass_zero="highpass", window="blackman", fs=Fe
    )
    filtre_p_h = np.fft.fft(filtre_p_h, n=1023)
    PH_Q2_13 = fct_format_Q2_13(filtre_p_h)


    # Passe-bande 1 : 1000 ± 500 Hz
    fc1 = 1000
    bw1 = 500
    f_low1 = fc1 - bw1
    f_high1 = fc1 + bw1
    passe_bande_1000_ori = signal.firwin(
        numtaps=n, cutoff=[f_low1, f_high1], pass_zero=False, window="blackman", fs=Fe
    )
    passe_bande_1000 = np.fft.fft(passe_bande_1000_ori)
    Passe_bande_1k_Q2_13 = fct_format_Q2_13(passe_bande_1000)

    # Passe-bande 2 : 2000 ± 500 Hz
    fc2 = 2000
    bw2 = 500
    f_low2 = fc2 - bw2
    f_high2 = fc2 + bw2
    passe_bande_2000_ori = signal.firwin(
        numtaps=n, cutoff=[f_low2, f_high2], pass_zero=False, window="blackman", fs=Fe
    )
    passe_bande_2000 = np.fft.fft(passe_bande_2000_ori)
    Passe_bande_2k_Q2_13 = fct_format_Q2_13(passe_bande_2000)

    # Passe-bande 3 : 3500 ± 1000 Hz
    fc3 = 3500
    bw3 = 1000
    f_low3 = fc3 - bw3
    f_high3 = fc3 + bw3
    passe_bande_3500_ori = signal.firwin(
        numtaps=n, cutoff=[f_low3, f_high3], pass_zero=False, window="blackman", fs=Fe
    )
    passe_bande_3500 = np.fft.fft(passe_bande_3500_ori)
    Passe_bande_3500_Q2_13 = fct_format_Q2_13(passe_bande_3500)
    fig, (ax2, ax3) = plt.subplots(2, 1, layout='constrained',sharey=True)
    #le zero padding
    pbFFT = np.fft.fft(filtre_p_b,n=4*N)
    phFFT = np.fft.fft(filtre_p_h,n=4*N)
    cbFFT_1000 = np.fft.fft(passe_bande_1000_ori, n=4 * N)
    cbFFT_2000 = np.fft.fft(passe_bande_2000_ori, n=4 * N)
    cbFFT_3500 = np.fft.fft(passe_bande_3500_ori, n=4 * N)
    freq = np.fft.fftfreq(N * 4, d=1 / Fe)
    ax2.set_ylim(-100, 20)
    ax2.grid(True)
    ax2.plot(freq[0:n], 20 * np.log10(np.abs(pbFFT[0:n])))
    ax2.plot(freq[0:n], 20 * np.log10(np.abs(phFFT[0:n])))
    ax2.plot(freq[0:n], 20 * np.log10(np.abs(cbFFT_1000[0:n])))
    ax2.plot(freq[0:n], 20 * np.log10(np.abs(cbFFT_2000[0:n])))
    ax2.plot(freq[0:n], 20 * np.log10(np.abs(cbFFT_3500[0:n])))
    ax2.set_title('Frequency response of both FIR filters')
    ax2.set_xlabel('Frequency [Hz]')
    ax2.set_ylabel('Amplitude [dB]')
    ax2.set_xscale('log')
    #ax2.set_yscale('log')

    # sum fft
    sumFFT = pbFFT + phFFT + cbFFT_1000 + cbFFT_2000 + cbFFT_3500
    ax3.plot(freq[0:n], 20 * np.log10(np.abs(sumFFT[0:n])))
    ax3.grid(True)
    ax3.set_title('Sum of both filters')
    ax3.set_xlabel('Frequency [Hz]')
    ax3.set_ylabel('Amplitude [dB]')
    ax3.set_xscale('log')
    #ax3.set_yscale('log')
    plt.show()
    return PB_Q2_13,PH_Q2_13,Passe_bande_1k_Q2_13,Passe_bande_2k_Q2_13,Passe_bande_3500_Q2_13



