from typing import List, Dict, Any

class StateManager:
    def __init__(self):
        self.current_context: Dict[str, Any] = {}
        self.history: List[Dict[str, str]] = []
        self.active_tasks: List[str] = []
        self.background_queue: List[Dict[str, Any]] = []

    def add_to_history(self, role: str, content: str):
        self.history.append({"role": role, "content": content})

    def update_context(self, key: str, value: Any):
        self.current_context[key] = value

    def get_context(self) -> Dict[str, Any]:
        return self.current_context
