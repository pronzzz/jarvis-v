import speech_recognition as sr

class Listener:
    def __init__(self, wake_word="jarvis"):
        self.wake_word = wake_word.lower()
        self.recognizer = sr.Recognizer()
        # Adjust energy threshold proactively for microphone sensitivity
        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True

    def listen_for_audio(self) -> bytes:
        """
        Listens continuously via the microphone until speech is detected
        and returns the raw audio data bytes for robust transcription.
        """
        with sr.Microphone() as source:
            print("[Listener] Adjusting for ambient noise... Please wait.")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("[Listener] Listening...")
            audio = self.recognizer.listen(source, phrase_time_limit=10)
        
        return audio.get_wav_data()
