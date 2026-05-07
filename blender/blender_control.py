import subprocess
import os
import logging

class BlenderControl:
    def __init__(self, blender_path: str = "blender"):
        self.blender_path = blender_path
        self.logger = logging.getLogger("TAHER.Blender")

    def execute_script(self, script_path: str):
        self.logger.info(f"Executing Blender script: {script_path}")
        try:
            result = subprocess.run(
                [self.blender_path, "--background", "--python", script_path],
                capture_output=True,
                text=True
            )
            return result.stdout
        except Exception as e:
            self.logger.error(f"Blender Execution Error: {e}")
            return str(e)

    def generate_and_run(self, python_code: str):
        temp_script = "blender/temp_script.py"
        with open(temp_script, "w") as f:
            f.write(python_code)
        return self.execute_script(temp_script)
