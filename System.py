import sys

from setup_logger import logging


class System:
    def __init__(self):
        super().__init__()

    def shutdown(self):
        logging.info("Shutting down...")
        sys.exit()
