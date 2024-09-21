# utils/error_handler.py

from PyQt5.QtWidgets import QMessageBox

class ErrorHandler:
    @staticmethod
    def show_error(message):
        """Display an error dialog to the user."""
        error_box = QMessageBox()
        error_box.setWindowTitle("Oops! Something went wrong.")
        error_box.setText(f"{message}\n\nDon't worry, it's just a little hiccup. We'll get it sorted in no time! 💡")
        error_box.setIcon(QMessageBox.Critical)
        error_box.setStandardButtons(QMessageBox.Ok)
        error_box.exec_()

    @staticmethod
    def log_and_show_error(message, technical_details=None):
        """Log error details and display a simplified message to the user."""
        if technical_details:
            print(f"DEBUG: {technical_details}")  # Log to console or file
        ErrorHandler.show_error(message)
