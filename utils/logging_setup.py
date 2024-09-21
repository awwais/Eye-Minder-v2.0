# utils/logging_setup.py

import logging

def setup_logging():
    """Set up logging to a file with permission fallback."""
    try:
        logging.basicConfig(filename='EyeMinder.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
    except PermissionError:
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        print("Warning: Unable to write to log file. Logging to console instead.")
