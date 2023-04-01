import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import numpy as np

def filtre_FIR():
    Fe = 20000
    N = 256
    n = N-1

    #passe-bas
    fcpb = 500
    filtre_p_b: np.ndarray = signal.firwin(
        numtaps=n, cutoff=fcpb, pass_zero="lowpass", window="blackman", fs=Fe
    )
    #passe-haut
    fcph = 4490
    filtre_p_h: np.ndarray = signal.firwin(
        numtaps=n, cutoff=fcph, pass_zero="highpass", window="blackman", fs=Fe
    )

    # Passe-bande 1 : 1000 ± 500 Hz
    fc1 = 1000
    bw1 = 500
    f_low1 = fc1 - bw1
    f_high1 = fc1 + bw1
    filtrer_pb_1000 = signal.firwin(
        numtaps=n, cutoff=[f_low1, f_high1], pass_zero=False, window="blackman", fs=Fe
    )

    # Passe-bande 2 : 2000 ± 500 Hz
    fc2 = 2000
    bw2 = 500
    f_low2 = fc2 - bw2
    f_high2 = fc2 + bw2
    filtrer_pb_2000 = signal.firwin(
        numtaps=n, cutoff=[f_low2, f_high2], pass_zero=False, window="blackman", fs=Fe
    )

    # Passe-bande 3 : 3500 ± 1000 Hz
    fc3 = 3500
    bw3 = 1000
    f_low3 = fc3 - bw3
    f_high3 = fc3 + bw3
    filtrer_pb_3500 = signal.firwin(
        numtaps=n, cutoff=[f_low3, f_high3], pass_zero=False, window="blackman", fs=Fe
    )

    fig, (ax2, ax3) = plt.subplots(2, 1, layout='constrained',sharey=True)
    #le zero padding
    pbFFT = np.fft.fft(filtre_p_b,n=4*N)
    phFFT = np.fft.fft(filtre_p_h,n=4*N)
    cbFFT_1000 = np.fft.fft(filtrer_pb_1000, n=4 * N)
    cbFFT_2000 = np.fft.fft(filtrer_pb_2000, n=4 * N)
    cbFFT_3500 = np.fft.fft(filtrer_pb_3500, n=4 * N)
    freq = np.fft.fftfreq(N * 4, d=1 / Fe)
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
    ax3.set_title('Sum of both filters')
    ax3.set_xlabel('Frequency [Hz]')
    ax3.set_ylabel('Amplitude [dB]')
    ax3.set_xscale('log')
    #ax3.set_yscale('log')
    plt.show()
    return pbFFT, phFFT, cbFFT_1000,cbFFT_2000, cbFFT_3500


