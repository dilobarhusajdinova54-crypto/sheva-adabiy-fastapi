import wave
import json
from vosk import Model, KaldiRecognizer

MODEL_PATH = "vosk-model-small-uz-0.22"
model = Model(MODEL_PATH)

def recognize_speech(wav_file):
    wf = wave.open(wav_file, "rb")

    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    result_text = ""

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            part = json.loads(rec.Result())
            result_text += " " + part.get("text", "")

    final = json.loads(rec.FinalResult())
    result_text += " " + final.get("text", "")

    return result_text.strip()
