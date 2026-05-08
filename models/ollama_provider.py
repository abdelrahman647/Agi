from ollama import AsyncClient
import logging
from typing import List, Dict

class OllamaProvider:
    def __init__(self, model_name: str = "qwen3:8b"):
        self.model_name = model_name
        self.client = AsyncClient()
        self.logger = logging.getLogger("TAHER.Ollama")

    async def chat(self, messages: List[Dict[str, str]], stream: bool = False):
        try:
            response = await self.client.chat(
                model=self.model_name,
                messages=messages,
                stream=stream
            )
            return response
        except Exception as e:
            self.logger.error(f"Ollama chat error: {e}")
            return None

    async def generate(self, prompt: str):
        try:
            response = await self.client.generate(model=self.model_name, prompt=prompt)
            return response['response']
        except Exception as e:
            error_msg = str(e)
            if "out of memory" in error_msg.lower() or "500" in error_msg:
                self.logger.error(f"Ollama Out of Memory or Server Error: {error_msg}")
                return "ERROR: TAHER's brain (Ollama) ran out of memory. Try closing other apps or using a smaller model."
            self.logger.error(f"Ollama generate error: {e}")
            return f"Ollama Error: {error_msg}"
