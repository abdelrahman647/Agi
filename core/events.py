import asyncio
from typing import Callable, Dict, List, Any

class EventBus:
    def __init__(self):
        self.listeners: Dict[str, List[Callable]] = {}

    def subscribe(self, event_type: str, callback: Callable):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(callback)

    async def emit(self, event_type: str, data: Any = None):
        if event_type in self.listeners:
            tasks = [asyncio.create_task(callback(data)) for callback in self.listeners[event_type]]
            if tasks:
                await asyncio.gather(*tasks)
