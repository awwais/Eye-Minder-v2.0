import sys
import logging
from utils.logging_setup import setup_logging
from app.tray.tray_app import TrayApp

def main():
    setup_logging()  # Set up logging for the app
    logging.info("Starting EyeMinder application.")

    app = TrayApp(sys.argv)  # Create system tray app
    sys.exit(app.exec_())  # Start the app's event loop

if __name__ == "__main__":
    main()
