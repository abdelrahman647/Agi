import subprocess
import logging

class SandboxBridge:
    def __init__(self, vm_ip: str, user: str):
        self.vm_ip = vm_ip
        self.user = user
        self.logger = logging.getLogger("TAHER.Sandbox")

    def run_remote_test(self, script_path: str):
        self.logger.info(f"Transferring and running {script_path} on VM {self.vm_ip}")
        # Simplified SCP and SSH call
        try:
            # scp script_path user@vm_ip:/tmp/
            # ssh user@vm_ip "python3 /tmp/test_script.py"
            cmd = f"ssh {self.user}@{self.vm_ip} 'python3 -m pytest /app/tests'"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            return result.stdout, result.returncode == 0
        except Exception as e:
            self.logger.error(f"Sandbox Error: {e}")
            return str(e), False
