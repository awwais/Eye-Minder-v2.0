import random
import logging
from PyQt5.QtCore import QTimer
from utils.error_handler import ErrorHandler
from data.messages import eye_facts, humor_messages
from utils.styled_reminder_box import StyledReminderBox  # Import the reusable styled reminder box

class Reminder:
    _instance = None

    def __init__(self):
        if Reminder._instance is not None:
            raise Exception("This class is a singleton!")
        self.timer = QTimer()
        self.timer.setInterval(20 * 60 * 1000)  # 20 minutes
        self.timer.timeout.connect(self.send_reminder)
        Reminder._instance = self

    @staticmethod
    def get_instance():
        if Reminder._instance is None:
            Reminder()
        return Reminder._instance

    def start_reminder(self):
        """Start the reminder timer and restart if failed."""
        try:
            self.timer.start()
        except Exception as e:
            logging.error(f"Failed to start reminder timer: {e}")
            ErrorHandler.log_and_show_error(
                "Failed to start the reminder timer. Restarting...",
                technical_details=str(e)
            )
            self.restart_timer()

    def restart_timer(self):
        """Restart the reminder timer if it fails."""
        try:
            self.timer.stop()  # Stop any existing timers
            self.timer.start()
            logging.info("Reminder timer restarted.")
        except Exception as e:
            logging.error(f"Failed to restart timer: {e}")
            ErrorHandler.log_and_show_error(
                "Failed to restart the reminder timer.",
                technical_details=str(e)
            )

    def send_reminder(self):
        """Display a random reminder message."""
        try:
            message = random.choice(humor_messages + eye_facts)
            logging.info(f"Showing message: {message}")

            # Use the modern styled reminder box
            StyledReminderBox.create_reminder_message("👁️ EyeMinder", message, button_text="Got it!")

        except Exception as e:
            logging.error(f"Failed to display reminder: {e}")
            ErrorHandler.log_and_show_error(
                "An error occurred while displaying the reminder.",
                technical_details=str(e)
            )

        # Restart the timer for the next reminder
        self.timer.start()
