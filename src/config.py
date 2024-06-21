config = {
    "voice_detection": {
        "model_name": "pyannote/speaker-diarization-3.0",
        "auth_token": <ENTER YOUR TOKEN>,
    },

    "speech_recognition": {
        "model_id": "openai/whisper-large-v3",
    },
    
    "text_summarization": {
        "api_key": <ENTER YOUR CHATGPT API SECRET KEY>,
    },
}


class Config():
    def __init__(self):
        self._config = config

    def get_property(self, property_name):
        if property_name not in self._config.keys():
            return None
        return self._config[property_name]
