from colorama import Fore, Style
import logging
import os
import sys


class Logger:
    _loggers = {}

    def __init__(
        self, name=None, colored=True,
        format="%(asctime)s %(filename)s(%(lineno)d): [%(levelname).1s] %(message)s"
    ) -> None:

        logging.basicConfig(level=logging.DEBUG, format=format)

        self.colored = colored
        self.last_frame = sys._getframe().f_back
        self.name = name or self.last_frame.f_globals['__file__']

        if self.name not in self._loggers:
            self._loggers[self.name] = logging.getLogger(os.path.basename(self.name))

    def _color(self, color: Fore, msg: str) -> str:
        return color + msg + Style.RESET_ALL if self.colored else msg

    def _log(self, level: int, msg: str, args, exc_info=None) -> None:
        logger = self._loggers[self.name]
        frame = self.last_frame
        record = logger.makeRecord(
            name=self.name,
            level=level,
            fn=frame.f_code.co_filename,
            lno=frame.f_lineno,
            msg=msg,
            args=args,
            exc_info=exc_info)
        logger.handle(record)

    def info(self, msg: str, *args, exc_info=None) -> None:
        colored = self._color(Fore.BLUE, msg)
        self._log(logging.INFO, colored, args, exc_info)

    def error(self, msg: str, *args, exc_info=None) -> None:
        colored = self._color(Fore.RED, msg)
        self._log(logging.ERROR, colored, args, exc_info)

    def critical(self, msg: str, *args, exc_info=None) -> None:
        colored = self._color(Fore.RED, msg)
        self._log(logging.CRITICAL, colored, args, exc_info)

    def debug(self, msg: str, *args, exc_info=None) -> None:
        self._log(logging.DEBUG, msg, args, exc_info)

    def warning(self, msg: str, *args, exc_info=None) -> None:
        colored = self._color(Fore.YELLOW, msg)
        self._log(logging.WARNING, colored, args, exc_info)
