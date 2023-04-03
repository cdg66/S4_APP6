import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from Format_Q2_13 import*

def H7_simul(H_transfert,N,fe):
    #H_transfert_congugate =fct_format_revert_Q2_13(H_transfert)
    H_transfert_congugate = np.conjugate(H_transfert)
    t = np.arange(0,N,1)
    fsinus = 100

    #gen input signal
    signal = np.sin(2*np.pi*fsinus*t/fe)

    #gen Xm
    FFT_sig = np.fft.fft(signal)

    #Y*=(HX)*
    YX = np.conjugate(FFT_sig)*H_transfert_congugate
    #gen Y(t)
    yt = np.fft.fft(YX)
    for i in range(len(yt)):
        yt[i] = yt[i]
    #plot all this shit
    plt.subplots(2, 2)
    #plot X and x
    plt.subplot(221)
    plt.plot(t,signal)
    plt.plot(t, FFT_sig)
    plt.title("x(blue) an X(orange)")
    #plot H
    plt.subplot(222)
    plt.plot(t,np.abs(H_transfert))
    plt.plot(t, np.abs(H_transfert_congugate))
    plt.title("H")
    #plot Y
    plt.subplot(223)
    plt.plot(t,YX)
    plt.title("Y")

    # plot y
    halfbuf = int(N / 2)
    signal_low_descrambeled = []
    signal_low_descrambeled[0:halfbuf] = yt[halfbuf:N]
    signal_low_descrambeled[halfbuf:N] = yt[0:halfbuf]
    plt.subplot(224)
    plt.plot(t,signal_low_descrambeled)
    plt.title("y[t]")
    plt.show()
    #
    # signal_low_descrambeled = []
    # halfbuf = int(N/2)
    # signal_low_descrambeled[0:halfbuf] = yt_low[halfbuf:N]
    # signal_low_descrambeled[halfbuf:N] = yt_low[0:halfbuf]
    # plt.plot(signal_low)
    # plt.plot(signal_low_descrambeled)
    #
    # plt.show()
    # signal_high_descrambeled = []
    # signal_high_descrambeled[0:halfbuf] = yt_high[halfbuf:N]
    # signal_high_descrambeled[halfbuf:N] = yt_high[0:halfbuf]
    # plt.plot(signal_high)
    # plt.plot(signal_high_descrambeled)
    # plt.show()
