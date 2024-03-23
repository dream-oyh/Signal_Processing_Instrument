import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
from scipy.fftpack import fft, fftfreq

N = 1000
t = np.linspace(0, 10, N)
y = signal.square(2 * np.pi * 1 * t)
y_f = fft(y)
freqs = fftfreq(N, 1 / 80)
# plt.plot(times, y)
_, axes = plt.subplots(2, 1)
axes[0].plot(t, y)
# axes[1].plot(freqs[freqs > 0], np.angle(y_f[freqs > 0] / N), label="Noised")
axes[1].plot(t, np.angle(y_f / N), label="Noised")
plt.legend()
plt.show()
