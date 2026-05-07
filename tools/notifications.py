import logging
import sys

class NotificationSystem:
    def __init__(self):
        self.logger = logging.getLogger("TAHER.Notifications")

    def notify(self, title: str, message: str):
        self.logger.info(f"NOTIFICATION: {title} - {message}")

        if sys_platform := sys.platform == "win32":
            try:
                from win10toast import ToastNotifier
                toaster = ToastNotifier()
                toaster.show_toast(title, message, duration=10, threaded=True)
            except ImportError:
                self.logger.warning("win10toast not installed. Falling back to log-only notifications.")
            except Exception as e:
                self.logger.error(f"Failed to send Windows notification: {e}")
        else:
            # Fallback for Linux/Sandbox
            print(f"\n[SYSTEM NOTIFICATION] {title}: {message}\n")

    def task_complete(self, task_name: str):
        self.notify("TAHER Task Complete", f"Finished: {task_name}")
