import chromadb
from chromadb.config import Settings
import logging

class MemoryManager:
    def __init__(self, persist_directory: str = "./memory/db"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.logger = logging.getLogger("TAHER.Memory")

        # Initialize collections
        self.semantic = self.client.get_or_create_collection("semantic")
        self.episodic = self.client.get_or_create_collection("episodic")
        self.lifestyle = self.client.get_or_create_collection("lifestyle")

    async def store_episodic(self, task: str, result: str, metadata: dict = None):
        self.episodic.add(
            documents=[f"Task: {task}\nResult: {result}"],
            metadatas=[metadata] if metadata else [{"type": "task_history"}],
            ids=[f"task_{self.episodic.count()}"]
        )

    async def query_memory(self, query: str, collection_name: str = "semantic", n_results: int = 5):
        collection = self.client.get_collection(collection_name)
        results = collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results
