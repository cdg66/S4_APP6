import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

def filtre_FIR():
    Fe = 20000
    N = 512
    n = N-1
    fcpb = 1000
    fcph = 950

    #gen both flter
    firpb_h: np.ndarray = signal.firwin(
        numtaps=n, cutoff=fcpb, pass_zero="lowpass", window="hamming", fs=Fe
    )
    print(firpb_h)
    firph_h: np.ndarray = signal.firwin(
        numtaps=n, cutoff=fcph, pass_zero="highpass", window="hamming", fs=Fe
    )
    n_array = np.arange(0,n,1)
    fig, (ax1, ax2) = plt.subplots(2, 1, layout='constrained')
    ax1.plot(n_array, firpb_h)
    ax1.set_title('Inpulse response of a lowpass filter ')
    ax1.set_xlabel('time(samples)')
    ax1.set_ylabel('Amplitude')
    ax2.plot(n_array, firph_h)
    ax2.set_title("Inpulse response of a highpass filter ")
    ax2.set_ylabel('Amplitude')
    ax2.set_xlabel('time(samples)')
    plt.show()
    #zero padding
    #firph_h_p = np.append(firph_h,np.zeros(3 * N))
    #firpb_h_p = np.append(firpb_h, np.zeros(3 * N))
    #fft of both filter
    fig, (ax2, ax3) = plt.subplots(2, 1, layout='constrained',sharey=True)
    pbFFT = np.fft.fft(firpb_h,n=4*N)
    phFFT = np.fft.fft(firph_h,n=4*N)
    freq = np.fft.fftfreq(N*4,d=1/Fe)
    ax2.plot(freq[0:n], 20*np.log10(np.abs(pbFFT[0:n])))
    ax2.plot(freq[0:n], 20 * np.log10(np.abs(phFFT[0:n])))
    ax2.set_title('frequence response of both fir filter ')
    ax2.set_xlabel('frequence[Hz]')
    ax2.set_ylabel('Amplitude[dB]')

    #sum fft
    sumFFT = pbFFT + phFFT
    ax3.plot(freq[0:n], 20 * np.log10(np.abs(sumFFT[0:n])))
    ax3.set_title('Somme des deux filtres')
    ax3.set_xlabel('frequence[Hz]')
    ax3.set_ylabel('Amplitude[dB]')
    plt.show()



