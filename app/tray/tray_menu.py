# app/tray_menu.py

from PyQt5.QtWidgets import QMenu, QAction
from app.tray.tray_dialogs import TrayDialogs
import logging

class TrayMenu:
    def __init__(self, tray_icon, reminder):
        self.tray_icon = tray_icon
        self.reminder = reminder

    def create_tray_menu(self):
        """Create and return the tray icon menu."""
        tray_menu = QMenu()

        # Add existing menu items
        why_action = QAction("Why Take Breaks", self.tray_icon)
        why_action.triggered.connect(TrayDialogs.show_why_take_breaks)
        tray_menu.addAction(why_action)

        time_action = QAction("Show Time Remaining", self.tray_icon)
        time_action.triggered.connect(self.show_remaining_time)
        tray_menu.addAction(time_action)

        restart_timer_action = QAction("Restart Timer", self.tray_icon)
        restart_timer_action.triggered.connect(self.restart_timer)
        tray_menu.addAction(restart_timer_action)  # New "Restart Timer" action

        about_action = QAction("About EyeMinder", self.tray_icon)
        about_action.triggered.connect(TrayDialogs.show_about_dialog)
        tray_menu.addAction(about_action)

        help_action = QAction("Help", self.tray_icon)
        help_action.triggered.connect(TrayDialogs.show_help_dialog)
        tray_menu.addAction(help_action)

        exit_action = QAction("Quit", self.tray_icon)
        exit_action.triggered.connect(self.exit_app)
        tray_menu.addAction(exit_action)

        return tray_menu

    def show_remaining_time(self):
        """Fetch the remaining time and show the dialog."""
        remaining_ms = self.reminder.timer.remainingTime()
        remaining_minutes, remaining_seconds = divmod(remaining_ms // 1000, 60)
        TrayDialogs.show_remaining_time(remaining_minutes, remaining_seconds)

    def restart_timer(self):
        """Restart the reminder timer."""
        self.reminder.timer.stop()  # Stop the current timer
        self.reminder.start_reminder()  # Restart the timer
        self.tray_icon.setToolTip("Timer restarted!")
        logging.info("Timer restarted by the user.")

    def exit_app(self):
        """Exit the application."""
        self.tray_icon.quit()
