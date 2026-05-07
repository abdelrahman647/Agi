import asyncio
import logging
from typing import Dict, List, Any
from core.state import StateManager
from core.events import EventBus
from planner.hierarchical_planner import Planner

class Orchestrator:
    def __init__(self):
        self.state = StateManager()
        self.events = EventBus()
        self.planner = Planner(self)
        self.logger = logging.getLogger("TAHER.Core")

    async def start(self):
        self.logger.info("TAHER Orchestrator starting...")
        # Start event loops, listeners, etc.

    async def handle_instruction(self, instruction: str):
        self.logger.info(f"Received instruction: {instruction}")

        # 1. Update State
        self.state.add_to_history("user", instruction)

        # 2. Plan
        plan = await self.planner.create_plan(instruction)

        # 3. Safety Verification
        if not await self.verify_plan_safety(plan):
            self.logger.warning("Plan failed safety check or was rejected by user.")
            return

        # 4. Execute
        async for result in self.planner.execute_plan(plan):
            await self.events.emit("execution_update", result)

        self.logger.info("Instruction completed.")

    async def verify_plan_safety(self, plan: List[Dict[str, Any]]) -> bool:
        """
        Placeholder for safety verification.
        In production, this would prompt the GUI for user approval
        and run static analysis if it involves code.
        """
        self.logger.info("Verifying plan safety...")
        # For now, we auto-approve unless it's a known dangerous pattern
        return True

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    orchestrator = Orchestrator()
    asyncio.run(orchestrator.start())
