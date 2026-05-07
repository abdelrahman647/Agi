import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QLineEdit, QWidget, QLabel
from PySide6.QtCore import Qt

class TaherGUI(QMainWindow):
    def __init__(self):
        super().__init__()
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

    def send_command(self):
        cmd = self.input_field.text()
        if cmd:
            self.display.append(f"<b>You:</b> {cmd}")
            self.input_field.clear()
            self.status.setText("Status: Thinking...")
            # Here we would call orchestrator.handle_instruction(cmd)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaherGUI()
    window.show()
    sys.exit(app.exec())
