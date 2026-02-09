import librosa
import numpy as np

y, sr = librosa.load("sheva1.wav", sr=None)

print("Sample rate:", sr)
print("Signal length:", len(y))
print("Duration (sec):", len(y) / sr)
print("First 10 samples:", y[:10])
