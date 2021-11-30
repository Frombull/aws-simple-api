import logging


class ColorLog:
    def __init__(self):
        logging.basicConfig(level=logging.INFO,
                            format='[%(levelname)s] (%(asctime)s) - %(message)s',
                            datefmt='%H:%M:%S'
                            )

    @staticmethod
    def info(message: str):
        logging.info(message)

    @staticmethod
    def warning(message: str):
        logging.warning(message)

    @staticmethod
    def error(message: str):
        logging.error(message)

    @staticmethod
    def critical(message: str):
        logging.critical(message)
