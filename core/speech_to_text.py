import os
import io
import wave
from faster_whisper import WhisperModel

class SpeechToText:
    def __init__(self, model_size="tiny.en"):
        # CPU initialization since macOS requires complex CoreML/MPS setup for FW
        print(f"[SpeechToText] Loading WhisperModel ({model_size})...")
        self.model = WhisperModel(model_size, device="cpu", compute_type="int8")

    def transcribe(self, audio_bytes: bytes) -> str:
        """
        Takes WAV bytes and transcribes them.
        """
        # Save bytes to a temporary wav format in memory for transcription
        temp_file = io.BytesIO(audio_bytes)
        
        # WhisperModel.transcribe can accept a file-like object
        segments, info = self.model.transcribe(temp_file, beam_size=5)
        
        transcription = []
        for segment in segments:
            transcription.append(segment.text)
            
        return " ".join(transcription).strip()
