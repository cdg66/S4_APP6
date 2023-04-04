import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from Format_Q2_13 import*

def H7_simul(H_transfert,N,fe, title="filter",fsinus=4490):
    #H_transfert_congugate =fct_format_revert_Q2_13(H_transfert)
    H_transfert_congugate = np.conjugate(H_transfert)
    t = np.arange(0,N,1)


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
    fig, ax = plt.subplots(3, 2)
    #plt.subplots(3, 2)
    #plot X and x
    plt.subplot(321)
    plt.plot(t, np.abs(FFT_sig))
    plt.title("X[k]")
    #plot H
    plt.subplot(322)
    plt.plot(t,np.abs(H_transfert))
    plt.plot(t, np.abs(H_transfert_congugate))
    plt.title("H[k]")
    #plot Y
    #plt.subplot(323, colspan=2, rowspan=1)
    ax = plt.subplot2grid((3,2), (1, 0), colspan=2, rowspan=1)
    ax.plot(t,np.abs(YX))
    ax.set_title("Y[k]")

    # plot y
    halfbuf = int(N / 2)
    signal_low_descrambeled = []
    signal_low_descrambeled[0:halfbuf] = yt[halfbuf:N]
    signal_low_descrambeled[halfbuf:N] = yt[0:halfbuf]
    plt.subplot(326)
    plt.plot(t,signal_low_descrambeled)
    plt.title("y[t]")

    plt.subplot(325)
    plt.plot(t,signal)
    plt.title("x[t]")
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
