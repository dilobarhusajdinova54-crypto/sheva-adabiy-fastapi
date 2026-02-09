import librosa
import numpy as np
import soundfile as sf

# Audio yuklash
y, sr = librosa.load("sheva1.wav", sr=None)

# FFT
Y = np.fft.rfft(y)
Y_mag = np.abs(Y)
Y_phase = np.angle(Y)

# Shovqin bahosi (past amplitudali qism)
noise_est = np.percentile(Y_mag, 20)

# Wiener (Kolmogorov) gain
H = (Y_mag**2) / (Y_mag**2 + noise_est**2)

# Filtrlash
Y_filtered = H * Y_mag * np.exp(1j * Y_phase)

# Orqaga signal (IFFT)
y_clean = np.fft.irfft(Y_filtered)

# Saqlash
sf.write("sheva1_clean.wav", y_clean, sr)

print("Filtrlash tugadi. Natija: sheva1_clean.wav")
