# app/icon_manager.py

import os
import logging
import platform
from PyQt5.QtGui import QIcon
from utils.error_handler import ErrorHandler

# For Windows dark mode detection
if platform.system() == "Windows":
    import winreg

# For macOS dark mode detection
# if platform.system() == "Darwin":
#     from AppKit import NSAppearance, NSAppearanceNameAqua, NSAppearanceNameDarkAqua

class IconManager:
    def __init__(self, tray_icon):
        self.tray_icon = tray_icon
        self.icon_light_path = os.path.join(os.path.dirname(__file__), "../..", "icons", "AppIcon1.png")
        self.icon_dark_path = os.path.join(os.path.dirname(__file__), "../..", "icons", "AppIcon1.png")

    def set_app_icon(self):
        """Set the tray icon dynamically based on system theme (light/dark)."""
        try:
            if self.is_dark_theme():
                self.tray_icon.setIcon(QIcon(self.icon_dark_path))
                logging.info("Using dark theme icon.")
            else:
                self.tray_icon.setIcon(QIcon(self.icon_light_path))
                logging.info("Using light theme icon.")
        except Exception as e:
            logging.error(f"Failed to set tray icon: {e}")
            ErrorHandler.log_and_show_error(
                "Could not load the application icon. A default icon will be used.",
                technical_details=str(e)
            )
            # Fallback to a default system icon
            self.tray_icon.setIcon(QIcon.fromTheme("application-default-icon"))

    def is_dark_theme(self):
        """Detect if the system is using a dark theme based on the OS."""
        system = platform.system()

        if system == "Windows":
            return self.is_windows_dark_mode()
        elif system == "Darwin":
            return self.is_macos_dark_mode()
        else:
            # Fallback: assume light theme for unsupported platforms
            logging.info("Unsupported platform, assuming light theme.")
            return False

    def is_windows_dark_mode(self):
        """Check if Windows is using dark mode via the registry."""
        try:
            registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
            value, regtype = winreg.QueryValueEx(key, "AppsUseLightTheme")
            winreg.CloseKey(key)
            return value == 0  # 0 means dark mode, 1 means light mode
        except Exception as e:
            logging.error(f"Failed to detect Windows theme: {e}")
            return False  # Assume light mode in case of failure

    # def is_macos_dark_mode(self):
    #     """Check if macOS is using dark mode using NSAppearance."""
    #     appearance = NSAppearance.currentAppearance()
    #     appearance_name = appearance.name() if appearance else NSAppearanceNameAqua
    #     return appearance_name == NSAppearanceNameDarkAqua
