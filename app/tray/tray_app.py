

import os
import sys
import logging
import psutil
from PyQt5.QtCore import QTimer, QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon
from PyQt5.QtGui import QIcon
from app.config.icon_manager import IconManager
from app.reminder.reminder import Reminder
from app.tray.tray_menu import TrayMenu
from utils.error_handler import ErrorHandler
from app.config.config_manager import ConfigManager

class TrayApp(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)

        self.replace_existing_instance()

        logging.info("EyeMinder started.")
        self.config = ConfigManager.get_instance()

        self.reminder = Reminder.get_instance()
        self.reminder.start_reminder()

        self.tray_icon = QSystemTrayIcon(self)
        self.icon_manager = IconManager(self.tray_icon)
        self.icon_manager.set_app_icon()

        self.tray_menu = TrayMenu(self.tray_icon, self.reminder)
        self.tray_icon.setContextMenu(self.tray_menu.create_tray_menu())

        self.initialize_tray()

        self.setQuitOnLastWindowClosed(False)

        self.tooltip_timer = QTimer(self)
        self.tooltip_timer.timeout.connect(self.update_tooltip)
        self.tooltip_timer.start(1000)

        # Add a subtle animation to grab attention periodically
        self.attention_timer = QTimer(self)
        self.attention_timer.timeout.connect(self.grab_attention)
        self.attention_timer.start(900000)  # Every 15 minutes

    def initialize_tray(self):
        try:
            self.tray_icon.show()
        except Exception as e:
            logging.error(f"Failed to initialize system tray: {e}")
            ErrorHandler.log_and_show_error(
                "System tray is not available on your system.",
                technical_details=str(e)
            )
            self.quit()

    def replace_existing_instance(self):
        current_pid = os.getpid()
        current_cmd = sys.argv

        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            if proc.info['pid'] != current_pid and proc.info['cmdline'] == current_cmd:
                logging.info(f"Found existing instance with PID {proc.info['pid']}, terminating it.")
                proc.terminate()

    def update_tooltip(self):
        remaining_ms = self.reminder.timer.remainingTime()
        remaining_minutes, remaining_seconds = divmod(remaining_ms // 1000, 60)
        emoji = "👀" if remaining_minutes < 5 else "⏳"
        self.tray_icon.setToolTip(f"{emoji} Next break in {remaining_minutes:02d}:{remaining_seconds:02d}")

    def grab_attention(self):
        icon = self.tray_icon.icon()
        animation = QPropertyAnimation(self.tray_icon, b"icon")
        animation.setDuration(1000)
        animation.setStartValue(icon)
        animation.setEndValue(QIcon("icons/MsgIcon.png"))
        animation.setEasingCurve(QEasingCurve.InOutQuad)
        animation.start()
        QTimer.singleShot(1000, lambda: self.tray_icon.setIcon(icon))