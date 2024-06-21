import torch
import pandas as pd
import librosa
from src.config import Config
from src.data.dataloader import load_audio
from src.models.voice_detection import VoiceDetectionInference
from src.models.speech_recognition import SpeechRecognitionInference
from src.models.text_summarization import SummarizationInference


class SOAPSummaryInference:
    def __init__(self, device, torch_dtype=torch.float32):
        self.config = Config()
        
        self.inference_voice_detection = VoiceDetectionInference(
            args=self.config.get_property('voice_detection')
        )
        self.inference_speech_recognition = SpeechRecognitionInference(
            args=self.config.get_property('speech_recognition'), 
            device=device, 
            torch_dtype=torch_dtype
        )
        self.inference_text_summarization = SummarizationInference(
            args=self.config.get_property('text_summarization')
        )

    def predict(self, audio_filename):
        audio = load_audio(audio_filename)

        vad_results = self.inference_voice_detection.predict(audio_filename)
        speech_results = self.inference_speech_recognition.predict(audio, vad_results)
        summary_results = self.inference_text_summarization.predict(speech_results)
        
        return summary_results
