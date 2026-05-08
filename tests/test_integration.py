import pytest
import asyncio
from unittest.mock import AsyncMock, patch
from models.ollama_provider import OllamaProvider
from planner.hierarchical_planner import Planner

@pytest.mark.asyncio
async def test_ollama_provider_mock():
    with patch('models.ollama_provider.AsyncClient') as mock_client_class:
        mock_client = mock_client_class.return_value
        mock_client.generate = AsyncMock(return_value={'response': 'mocked reasoning'})

        provider = OllamaProvider()
        response = await provider.generate("test prompt")

        assert response == "mocked reasoning"
        mock_client.generate.assert_called_once()

@pytest.mark.asyncio
async def test_planner_integration_mock():
    with patch('models.ollama_provider.AsyncClient') as mock_client_class:
        mock_client = mock_client_class.return_value
        mock_client.generate = AsyncMock(return_value={'response': 'JSON task list'})

        # We need a mock orchestrator
        mock_orch = AsyncMock()
        planner = Planner(mock_orch)

        plan = await planner.create_plan("do something")

        assert len(plan) == 2
        assert plan[0]['task'] == 'llm_reasoning'
        assert plan[0]['params']['thought'] == 'JSON task list'
