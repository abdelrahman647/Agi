import sys
import asyncio
import threading
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QLineEdit, QWidget, QLabel
from PySide6.QtCore import Qt, Signal, QObject
from core.orchestrator import Orchestrator

class WorkerSignals(QObject):
    response_received = Signal(str)
    status_changed = Signal(str)

class TaherGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.orchestrator = Orchestrator()
        self.signals = WorkerSignals()
        self.signals.response_received.connect(self.on_response)
        self.signals.status_changed.connect(self.on_status_change)

        # Start orchestrator in a background thread
        self.loop = asyncio.new_event_loop()
        threading.Thread(target=self.run_async_loop, daemon=True).start()
        self.setWindowTitle("TAHER - AGI Assistant")
        self.resize(1000, 700)

        # Central Widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layout
        self.layout = QVBoxLayout(self.central_widget)

        # Log/Chat Display
        self.display = QTextEdit()
        self.display.setReadOnly(True)
        self.display.setPlaceholderText("TAHER is ready...")
        self.layout.addWidget(self.display)

        # Input Field
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Command TAHER...")
        self.input_field.returnPressed.connect(self.send_command)
        self.layout.addWidget(self.input_field)

        # Status Label
        self.status = QLabel("Status: Idle")
        self.layout.addWidget(self.status)

        self.apply_styles()

    def apply_styles(self):
        self.setStyleSheet("""
            QMainWindow { background-color: #121212; }
            QTextEdit { background-color: #1e1e1e; color: #e0e0e0; border: none; font-family: 'Segoe UI'; font-size: 14px; padding: 10px; }
            QLineEdit { background-color: #2c2c2c; color: #ffffff; border: 1px solid #3f3f3f; padding: 8px; border-radius: 4px; }
            QLabel { color: #888888; font-size: 11px; }
        """)

    def run_async_loop(self):
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self.orchestrator.start())
        self.loop.run_forever()

    def send_command(self):
        cmd = self.input_field.text()
        if cmd:
            self.display.append(f"<b>You:</b> {cmd}")
            self.input_field.clear()
            self.status.setText("Status: Thinking...")
            asyncio.run_coroutine_threadsafe(self.process_instruction(cmd), self.loop)

    async def process_instruction(self, instruction: str):
        # This is a bridge between GUI thread and Orchestrator
        # In a full implementation, the orchestrator would emit events
        # which the GUI listens to.
        await self.orchestrator.handle_instruction(instruction)
        self.signals.response_received.emit("Task completed.")
        self.signals.status_changed.emit("Status: Idle")

    def on_response(self, text: str):
        self.display.append(f"<b>TAHER:</b> {text}")

    def on_status_change(self, status: str):
        self.status.setText(status)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaherGUI()
    window.show()
    sys.exit(app.exec())
