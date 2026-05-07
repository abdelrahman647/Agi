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
            process = subprocess.Popen(
                ['piper', '--model', self.model_path, '--output_raw'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            # This would normally stream to an audio device like 'aplay' or 'pw-play'
            stdout, stderr = process.communicate(input=text.encode('utf-8'))
        except Exception as e:
            self.logger.error(f"TTS Error: {e}")
