import asyncio
import logging
from typing import Dict, List, Any
from core.state import StateManager
from core.events import EventBus
from planner.hierarchical_planner import Planner
from agents.research_agent import ResearchAgent
from memory.memory_manager import MemoryManager
from tools.notifications import NotificationSystem

class Orchestrator:
    def __init__(self):
        self.state = StateManager()
        self.events = EventBus()
        self.memory = MemoryManager()
        self.planner = Planner(self)
        self.researcher = ResearchAgent(self.memory)
        self.notifier = NotificationSystem()
        self.is_running = False
        self.logger = logging.getLogger("TAHER.Core")

    async def start(self):
        self.logger.info("TAHER Orchestrator starting...")
        self.is_running = True
        asyncio.create_task(self.autonomous_loop())

    async def autonomous_loop(self):
        """
        Background loop that picks up research and learning tasks
        when the system is not actively engaged with the user.
        """
        while self.is_running:
            if not self.state.active_tasks and self.state.background_queue:
                task = self.state.background_queue.pop(0)
                self.logger.info(f"Picking up background task: {task['type']}")

                if task['type'] == 'research':
                    await self.researcher.research_topic(task['query'])
                    self.notifier.task_complete(f"Research on {task['query']}")
                elif task['type'] == 'learning':
                    await self.researcher.learn_skill(task['skill'])
                    self.notifier.task_complete(f"Learning {task['skill']}")

            await asyncio.sleep(60) # Check every minute

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

async def main():
    logging.basicConfig(level=logging.INFO)
    orchestrator = Orchestrator()
    await orchestrator.start()

    # Keep the orchestrator alive
    while orchestrator.is_running:
        await asyncio.sleep(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
