import pandas as pd
from pyannote.audio import Pipeline
from io import StringIO

class VoiceDetectionInference:
    def __init__(self, args):
        model_name = args['model_name']
        auth_token = args['auth_token']
        self.pipeline = Pipeline.from_pretrained(model_name, use_auth_token=auth_token)
    
    def predict(self, filename, max_speakers=2):
        # Run the diarization pipeline on the audio file
        diarization = self.pipeline(filename, max_speakers=max_speakers)
        
        # Inference speaker diarization
        output = StringIO()
        diarization.write_rttm(output)
        output.seek(0)  
        
        # Read the RTTM formatted results
        lines = output.readlines()
        
        starts = []
        durations = []
        speaker_ids = []
        
        for line in lines:
            _, _, _, start, duration, _, _, speaker, _, _ = line.split()
            start = float(start)
            duration = float(duration)
            speaker_id = int(speaker.split('_')[-1])
            starts.append(start)
            durations.append(duration)
            speaker_ids.append(speaker_id)
        
        # Create a DataFrame with the voice activity detection results
        vad_results = pd.DataFrame({'start': starts, 'duration': durations, 'speaker_id': speaker_ids})
        
        return vad_results
