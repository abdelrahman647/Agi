import logging
from typing import List, Any, Dict
from models.ollama_provider import OllamaProvider
from models.airllm_provider import AirLLMProvider
import yaml

class Planner:
    def __init__(self, orchestrator):
        self.orchestrator = orchestrator
        self.logger = logging.getLogger("TAHER.Planner")

        # Determine which LLM provider to use from config
        try:
            with open("configs/config.yaml", "r") as f:
                config = yaml.safe_load(f)
                if config.get("airllm", {}).get("enabled", False):
                    self.llm = AirLLMProvider(config["airllm"]["model"])
                    self.logger.info("Planner initialized with AirLLM (Sequential Layer Loading).")
                else:
                    self.llm = OllamaProvider()
                    self.logger.info("Planner initialized with Ollama.")
        except Exception:
            self.llm = OllamaProvider()

    async def create_plan(self, instruction: str) -> List[Dict[str, Any]]:
        self.logger.info(f"Decomposing instruction into sub-tasks...")

        prompt = f"Decompose this instruction into a JSON list of tasks for an AGI: {instruction}"
        response = await self.llm.generate(prompt)
        self.logger.info(f"LLM Reasoning: {response}")

        # Simplified for now: just log the reasoning and return a default plan
        return [
            {"task": "llm_reasoning", "params": {"thought": response}},
            {"task": "analyze_request", "params": {"query": instruction}},
        ]

    async def execute_plan(self, plan: List[Dict[str, Any]]):
        for step in plan:
            self.logger.info(f"Executing step: {step['task']}")
            # Tool routing would happen here
            yield {"status": "success", "step": step['task']}
