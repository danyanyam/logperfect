
import logging
import os
import sys
import datetime as dt
from logperfect.logging.formatters import StreamFormatter, FileFormatter
from logperfect.logging.handlers import TraceBackHandler


class Logger:
    _loggers = {}

    def __init__(
        self, name=None, level=logging.DEBUG, output=f'{__name__}.log',
        fmt="%(asctime)s.%(msecs)03d [%(levelname).1s] - %(name)s:%(filename).10s(%(lineno)d): %(message)s"
    ):
        self.fmt = fmt
        self.level = level
        self.output = output or f'{dt.datetime.now()}.log'
        self.last_frame = sys._getframe().f_back
        self.name = name or self.last_frame.f_globals['__file__']

        if self.name in self._loggers:
            return

        logger = logging.getLogger(os.path.basename(self.name))
        logger = self._configure_stream_handler(logger)
        logger = self._configure_fstream_handler(logger)
        logger.setLevel(self.level)
        self._loggers[self.name] = logger

    def _configure_stream_handler(self, logger):
        std_handler = logging.StreamHandler()
        std_handler.setLevel(self.level)
        std_handler.setFormatter(StreamFormatter(self.fmt))
        logger.addHandler(std_handler)
        return logger

    def _configure_fstream_handler(self, logger):
        file_handler = TraceBackHandler(f'{self.output}', 'a+')
        file_handler.setFormatter(FileFormatter(self.fmt))
        file_handler.setLevel(self.level)
        logger.addHandler(file_handler)
        return logger

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
        self._log(logging.INFO, msg, args, exc_info)

    def error(self, msg: str, *args, exc_info=None) -> None:
        self._log(logging.ERROR, msg, args, exc_info)

    def critical(self, msg: str, *args, exc_info=None) -> None:
        self._log(logging.CRITICAL, msg, args, exc_info)

    def debug(self, msg: str, *args, exc_info=None) -> None:
        self._log(logging.DEBUG, msg, args, exc_info)

    def warning(self, msg: str, *args, exc_info=None) -> None:
        self._log(logging.WARNING, msg, args, exc_info)
