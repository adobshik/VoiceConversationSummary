import librosa
import torch

def load_audio(file_path, target_sample_rate=16000):
    waveform, sr = librosa.load(file_path, sr=target_sample_rate)

    return waveform
