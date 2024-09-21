
from PyQt5.QtWidgets import QMessageBox, QPushButton, QLabel
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve

class StyledReminderBox:
    """Utility class to create and style modern reminder message boxes."""

    @staticmethod
    def create_reminder_message(title, message, button_text="Got it!"):
        """Create and style a modern, psychologically-optimized reminder message box."""
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)

        # Apply custom material-inspired styles
        StyledReminderBox.apply_reminder_style(msg_box)

        # Set custom button and style it
        msg_box.setStandardButtons(QMessageBox.NoButton)
        ok_button = QPushButton(button_text)
        msg_box.addButton(ok_button, QMessageBox.AcceptRole)
        StyledReminderBox.style_button(ok_button)

        # Add progress indicator
        progress_label = QLabel("This message will close in 10 seconds")
        progress_label.setStyleSheet("color: #B0B0B0; font-size: 12px;")
        msg_box.layout().addWidget(progress_label, msg_box.layout().rowCount(), 0, 1, msg_box.layout().columnCount())

        # Set window flags for always on top and clean presentation
        msg_box.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        # Add fade-in animation
        msg_box.setWindowOpacity(0)
        fade_in_animation = QPropertyAnimation(msg_box, b"windowOpacity")
        fade_in_animation.setDuration(500)
        fade_in_animation.setStartValue(0)
        fade_in_animation.setEndValue(1)
        fade_in_animation.setEasingCurve(QEasingCurve.InOutQuad)
        fade_in_animation.start()

        # Add auto-close timer
        time_left = 10
        timer = QTimer(msg_box)

        def update_progress():
            nonlocal time_left
            time_left -= 1
            progress_label.setText(f"This message will close in {time_left} seconds")
            if time_left <= 0:
                msg_box.accept()

        timer.timeout.connect(update_progress)
        timer.start(1000)

        msg_box.exec_()

    @staticmethod
    def apply_reminder_style(msg_box):
        """Apply clean, modern design for the reminder message box."""
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(30, 30, 30))  # Dark background
        palette.setColor(QPalette.WindowText, QColor(240, 240, 240))  # Light text

        msg_box.setPalette(palette)

        # Add custom stylesheet for modern material look
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: #1E1E1E;
                border-radius: 15px;
                padding: 20px;
            }
            QLabel {
                color: #F0F0F0;
                font-size: 16px;
                font-family: 'Segoe UI', sans-serif;
                margin-bottom: 15px;
            }
        """)

        # Set custom font for the message box
        font = QFont("Segoe UI", 12)
        msg_box.setFont(font)

    @staticmethod
    def style_button(button):
        """Apply custom styles to buttons."""
        button.setStyleSheet("""
            QPushButton {
                background-color: #0078D4;
                color: white;
                padding: 12px 20px;
                font-size: 16px;
                font-family: 'Segoe UI', sans-serif;
                border-radius: 8px;
                border: none;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #106EBE;
            }
            QPushButton:pressed {
                background-color: #005A9E;
            }
        """)
        button.setFont(QFont("Segoe UI", 12))

# Usage example
if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    StyledReminderBox.create_reminder_message("Important Reminder", "Don't forget to take a break and stretch!")
    sys.exit(app.exec_())