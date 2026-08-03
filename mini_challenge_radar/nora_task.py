import numpy as np
import matplotlib.pyplot as plt
sampling_rate = 1000
T = 1/ sampling_rate
N = 1000
t = np.linspace(0.0, N*T , N , endpoint=False)
clean_signal=np.sin(2 * np.pi * 50 * t) 
noise = np.random.normal(0 , 1.5 , N)
nosiy_signal = clean_signal + noise
fft_value = np.fft.fft(nosiy_signal)
freq = np.fft.fftfreq(N,T)
mag = np.abs(fft_value)
mask = freq >=0
freq_pos = freq[mask]
mag_pos = mag[mask] * 2/N
peak_freq = freq_pos [mag_pos>0.2]
plt.figure(figsize=(10,5))
plt.subplot(2,1,1)
plt.plot(t[:200],nosiy_signal[:200], label="Nosiy Signal", color='gray', alpha= 0.5)
plt.plot(t[:200],clean_signal[:200], label="Clean Signal(50Hz)", color='blue')
plt.ylim(-3,3)
plt.title("Time Domain Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.subplot(2,1,2)
plt.plot(freq_pos, mag_pos, label="Magnitude Spectrum", color='red')
plt.title("Frequency Domain Signal")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.xlim(0, 200)
plt.grid(True)
plt.tight_layout()
plt.show()