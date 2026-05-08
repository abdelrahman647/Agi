import logging
from typing import List, Any, Dict
from models.ollama_provider import OllamaProvider

class Planner:
    def __init__(self, orchestrator):
        self.orchestrator = orchestrator
        self.logger = logging.getLogger("TAHER.Planner")
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
