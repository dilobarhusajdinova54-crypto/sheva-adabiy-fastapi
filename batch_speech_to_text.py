import os
import wave
import json
from vosk import Model, KaldiRecognizer

MODEL_PATH = "vosk-model-small-uz-0.22"
AUDIO_DIR = "."

model = Model(MODEL_PATH)

results = []

for file in os.listdir(AUDIO_DIR):
    if file.endswith(".wav") and "_clean" not in file:
        print(f"Tanish бошланди: {file}")
        
        wf = wave.open(file, "rb")
        rec = KaldiRecognizer(model, wf.getframerate())
        rec.SetWords(True)

        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            rec.AcceptWaveform(data)

        result = json.loads(rec.FinalResult())
        text = result.get("text", "")

        results.append({
            "file": file,
            "recognized_text": text
        })

        print(f" → Natija: {text}")

print("\nYAKUNIY NATIJALAR:")
for r in results:
    print(r)
