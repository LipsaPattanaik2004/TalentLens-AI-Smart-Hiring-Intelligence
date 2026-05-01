import librosa

def analyze_audio(file):
    y, sr = librosa.load(file)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

    return {"speech_rate": tempo}
