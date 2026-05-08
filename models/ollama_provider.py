from ollama import AsyncClient
import logging
from typing import List, Dict

class OllamaProvider:
    def __init__(self, model_name: str = "qwen2.5:7b"):
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
            self.logger.error(f"Ollama generate error: {e}")
            return str(e)
