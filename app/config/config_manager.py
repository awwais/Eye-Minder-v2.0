# app/config_manager.py

class ConfigManager:
    _instance = None

    def __init__(self):
        if ConfigManager._instance is not None:
            raise Exception("This class is a singleton!")
        ConfigManager._instance = self
        self.config = self.load_default_config()

    @staticmethod
    def get_instance():
        if ConfigManager._instance is None:
            ConfigManager()
        return ConfigManager._instance

    def load_default_config(self):
        """Load the default configuration for the app."""
        return {
            "theme": "auto",  # Can be 'auto', 'light', or 'dark'
            "reminder_interval": 20 * 60 * 1000  # 20 minutes
        }

    def set_theme(self, theme):
        """Set the theme (light/dark/auto) for the application."""
        self.config['theme'] = theme

    def get_theme(self):
        """Get the current theme setting."""
        return self.config['theme']

    def set_reminder_interval(self, interval):
        """Set the reminder interval in milliseconds."""
        self.config['reminder_interval'] = interval

    def get_reminder_interval(self):
        """Get the reminder interval in milliseconds."""
        return self.config['reminder_interval']
