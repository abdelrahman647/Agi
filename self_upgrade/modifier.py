import os
from git import Repo
import logging

class SelfModifier:
    def __init__(self, repo_path: str = "."):
        self.repo = Repo(repo_path)
        self.logger = logging.getLogger("TAHER.SelfUpgrade")

    def create_upgrade_branch(self, branch_name: str):
        new_branch = self.repo.create_head(branch_name)
        new_branch.checkout()
        self.logger.info(f"Switched to new branch: {branch_name}")

    def apply_diff(self, file_path: str, new_content: str):
        # In a real scenario, this would use patch or direct write
        with open(file_path, "w") as f:
            f.write(new_content)
        self.repo.index.add([file_path])
        self.logger.info(f"Applied changes to {file_path}")

    def commit_changes(self, message: str):
        self.repo.index.commit(message)
        self.logger.info(f"Committed: {message}")

    def rollback(self):
        self.repo.git.reset('--hard', 'HEAD~1')
        self.logger.warning("Rolled back last commit.")
