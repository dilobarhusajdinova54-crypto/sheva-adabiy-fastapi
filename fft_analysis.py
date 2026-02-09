import librosa
import numpy as np

y, sr = librosa.load("sheva1.wav", sr=None)

fft_vals = np.fft.rfft(y)
fft_mag = np.abs(fft_vals)

freqs = np.fft.rfftfreq(len(y), d=1/sr)

top_indices = np.argsort(fft_mag)[-10:][::-1]

print("Top 10 dominant frequencies (Hz):")
for i in top_indices:
    print(f"{freqs[i]:.2f} Hz  -> amplitude {fft_mag[i]:.2f}")
