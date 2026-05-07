import asyncio
import logging

class VoicePipeline:
    def __init__(self, orchestrator):
        self.orchestrator = orchestrator
        self.logger = logging.getLogger("TAHER.Voice")
        self.is_listening = False

    async def listen_loop(self):
        self.is_listening = True
        self.logger.info("Voice listener active. Waiting for wake-word 'TAHER'...")
        while self.is_listening:
            # 1. Capture Audio
            # 2. VAD (Voice Activity Detection)
            # 3. Check for Wake-word
            # 4. Transcribe if active
            await asyncio.sleep(0.1)

    def stop(self):
        self.is_listening = False
