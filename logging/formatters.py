from colorama import Fore, Style
import logging

class FileFormatter(logging.Formatter):
    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.datefmt = '%d-%m-%Y %H:%M:%S'

    def format(self, record):
        formatter = logging.Formatter(self.fmt, datefmt=self.datefmt)
        return formatter.format(record)


class StreamFormatter(logging.Formatter):

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.datefmt = '%d-%m-%Y %H:%M:%S'
        self.FORMATS = {
            logging.DEBUG: Fore.WHITE + self.fmt + Style.RESET_ALL,
            logging.INFO: Fore.BLUE + self.fmt + Style.RESET_ALL,
            logging.WARNING: Fore.YELLOW + self.fmt + Style.RESET_ALL,
            logging.ERROR: Fore.RED + self.fmt + Style.RESET_ALL,
            logging.CRITICAL: Style.BRIGHT + Fore.RED + self.fmt + Style.RESET_ALL
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt=self.datefmt)
        return formatter.format(record)
