import os
import subprocess
import logging

class PiperTTS:
    def __init__(self, model_path: str = "models/tts/en_US-lessac-medium.onnx"):
        self.model_path = model_path
        self.logger = logging.getLogger("TAHER.TTS")

    def speak(self, text: str):
        self.logger.info(f"Speaking: {text}")
        # Simplified Piper call via subprocess
        # Assumes piper executable is in PATH
        try:
            import sounddevice as sd
            import numpy as np

            process = subprocess.Popen(
                ['piper', '--model', self.model_path, '--output_raw'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            # Pipe output to sounddevice for real-time playback
            stdout, stderr = process.communicate(input=text.encode('utf-8'))

            # Assume 22050Hz (Piper default) mono 16-bit
            audio_array = np.frombuffer(stdout, dtype=np.int16)
            sd.play(audio_array, samplerate=22050)
            sd.wait()

        except Exception as e:
            self.logger.error(f"TTS Error: {e}")
