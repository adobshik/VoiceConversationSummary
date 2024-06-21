import torch
import pandas as pd
import librosa
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor

class SpeechRecognitionInference:
    def __init__(self, args, device="cpu", torch_dtype=torch.float32):
        model_id = args['model_id']
        self.device = device
        self.model = AutoModelForSpeechSeq2Seq.from_pretrained(
            model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
        )
        self.model.to(device)
        self.processor = AutoProcessor.from_pretrained(model_id)
        self.gen_kwargs = {
            "max_new_tokens": 128,
            "num_beams": 1,
            "return_timestamps": False,
            "language": "english",
        }
    
    def predict(self, audio, vad_results, sample_rate=16000):        
        texts = []
        for _, row in vad_results.iterrows():
            start = row.start
            duration = row.duration
            speaker_id = int(row.speaker_id)
            
            start_sample = int(start * sample_rate)
            end_sample = start_sample + int(duration * sample_rate)

            # Get a short clip from audio
            sample = {'array': audio[start_sample:end_sample], 'sampling_rate': sample_rate}

            # Create input features from audio
            input_features = self.processor(
                sample["array"], sampling_rate=sample["sampling_rate"], return_tensors="pt"
            ).input_features
            input_features = input_features.to(self.device)

            # Run the speech recognition model  
            pred_ids = self.model.generate(input_features, **self.gen_kwargs)
            pred_text = self.processor.batch_decode(pred_ids, skip_special_tokens=True)
            texts.append(pred_text[0].strip())

        # Create a DataFrame with recognized speech
        df_speech = pd.DataFrame({
            'speaker_id': vad_results.speaker_id.tolist(),
            'start': vad_results.start.tolist(),
            'duration': vad_results.duration.tolist(),
            'text': texts
        })
        
        return df_speech
