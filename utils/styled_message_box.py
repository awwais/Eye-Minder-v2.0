
from PyQt5.QtWidgets import QMessageBox, QPushButton, QVBoxLayout, QLabel, QWidget
from PyQt5.QtGui import QPalette, QColor, QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve

class StyledMessageBox(QMessageBox):
    """Utility class to create and style modern, engaging message boxes."""

    ICON_PATH = "icons/MsgIcon.png"  # Update the path for the message box icon

    def __init__(self, title, message, icon_type=None, button_text="OK"):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(message)

        # Set the custom icon for the message box
        icon = self.get_icon(icon_type)
        if isinstance(icon, QPixmap):  # If it's a QPixmap, use it for the message box
            self.setIconPixmap(icon.scaled(48, 48, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            self.setIcon(icon)  # Otherwise, set the QMessageBox.Icon directly

        self.apply_modern_style()

        self.setStandardButtons(QMessageBox.Ok)
        ok_button = self.button(QMessageBox.Ok)
        ok_button.setText(button_text)
        self.style_button(ok_button)

        self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        
        # Add fade-in animation
        self.setWindowOpacity(0)
        self.fade_in_animation = QPropertyAnimation(self, b"windowOpacity")
        self.fade_in_animation.setDuration(300)
        self.fade_in_animation.setStartValue(0)
        self.fade_in_animation.setEndValue(1)
        self.fade_in_animation.setEasingCurve(QEasingCurve.InOutQuad)

    def showEvent(self, event):
        super().showEvent(event)
        self.fade_in_animation.start()

    def get_icon(self, icon_type):
        """Set the custom icon for the message box."""
        if self.ICON_PATH and not QPixmap(self.ICON_PATH).isNull():
            pixmap = QPixmap(self.ICON_PATH)
            if not pixmap.isNull():
                return pixmap  # Return pixmap to be used in setIconPixmap

        # Fallback to default icon type if custom icon is not available
        if icon_type:
            return icon_type
        return QMessageBox.Information  # Default icon

    def apply_modern_style(self):
        self.setStyleSheet("""
            QMessageBox {
                background-color: #FAFAFA;
                border-radius: 15px;
                padding: 20px;
            }
            QLabel {
                color: #333333;
                font-size: 16px;
                font-family: 'Segoe UI', sans-serif;
                margin-bottom: 15px;
            }
            QPushButton {
                background-color: #4285F4;
                color: white;
                padding: 10px 20px;
                font-size: 16px;
                font-family: 'Segoe UI', sans-serif;
                border-radius: 8px;
                border: none;
                min-width: 120px;
            }
            QPushButton:hover {
                background-color: #357AE8;
            }
            QPushButton:pressed {
                background-color: #2C6BDC;
            }
        """)
        self.setFont(QFont("Segoe UI", 12))

    def style_button(self, button):
        button.setCursor(Qt.PointingHandCursor)

    @classmethod
    def show_message(cls, title, message, icon_type=None, button_text="OK"):
        msg_box = cls(title, message, icon_type, button_text)
        return msg_box.exec_()

    @classmethod
    def create_error_message(cls, title, message, button_text="Got it"):
        return cls.show_message(title, message, QMessageBox.Critical, button_text)

    @classmethod
    def create_info_message(cls, title, message, button_text="OK"):
        return cls.show_message(title, message, QMessageBox.Information, button_text)

    @classmethod
    def create_warning_message(cls, title, message, button_text="Understood"):
        return cls.show_message(title, message, QMessageBox.Warning, button_text)

# Usage in TrayDialogs remains the same
