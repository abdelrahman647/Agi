import pytest
from core.state import StateManager
from core.events import EventBus

def test_state_manager():
    sm = StateManager()
    sm.add_to_history("user", "hello")
    assert len(sm.history) == 1
    assert sm.history[0]["content"] == "hello"

@pytest.mark.asyncio
async def test_event_bus():
    eb = EventBus()
    received = []
    async def callback(data):
        received.append(data)

    eb.subscribe("test_event", callback)
    await eb.emit("test_event", "payload")
    assert "payload" in received
