import asyncio
import logging
import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

class VoicePipeline:
    def __init__(self, orchestrator):
        self.orchestrator = orchestrator
        self.logger = logging.getLogger("TAHER.Voice")
        self.is_listening = False
        self.model = None # Lazy load
        self.sample_rate = 16000

    def load_model(self):
        if not self.model:
            self.logger.info("Loading Whisper model...")
            self.model = WhisperModel("base", device="cpu", compute_type="int8")

    async def listen_loop(self):
        self.is_listening = True
        self.load_model()
        self.logger.info("Voice listener active. Waiting for wake-word 'TAHER'...")

        while self.is_listening:
            # Simple simulation of voice activity detection
            # In a real setup, we would use sounddevice to stream audio
            # and check for the wake word.
            await asyncio.sleep(5)
            # self.logger.info("Detected voice activity...")
            # transcription = self.transcribe(audio_data)
            # if "taher" in transcription.lower():
            #     await self.orchestrator.handle_instruction(transcription)

    def transcribe(self, audio_data):
        segments, info = self.model.transcribe(audio_data, beam_size=5)
        return " ".join([s.text for s in segments])

    def stop(self):
        self.is_listening = False
