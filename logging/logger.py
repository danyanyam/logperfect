# import logging
# import colored_traceback
# import sys

# colored_traceback.add_hook()
# _log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
# BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
# RESET_SEQ = "\033[0m"
# COLOR_SEQ = "\033[1;%dm"
# BOLD_SEQ = "\033[1m"


# class Logger:
#     _log = None

#     def __init__(self, name: str) -> None:
#         self._log = self._log or self.get_logger(name)
#         self.info(f'{sys._getframe().f_back}')

#     def get_logger(self, name):
#         logger = logging.getLogger(name)
#         logger.setLevel(logging.INFO)
#         logger.addHandler(self.get_file_handler())
#         logger.addHandler(self.get_stream_handler())
#         return logger

#     def get_file_handler(self, fname="x.log"):
#         file_handler = logging.FileHandler(fname)
#         file_handler.setLevel(logging.WARNING)
#         file_handler.setFormatter(logging.Formatter(_log_format))
#         return file_handler

#     def get_stream_handler(self):
#         stream_handler = logging.StreamHandler()
#         stream_handler.setLevel(logging.INFO)
#         stream_handler.setFormatter(logging.Formatter(_log_format))
#         return stream_handler

#     def info(self, msg):
#         self._log.info(f'\033[34m{msg}{RESET_SEQ}')

# def info(msg):
#     Logger._log.info(msg)

# import argparse
# import logging
# import os
# import sys


# DEFAULT_LOGFILE_LEVEL = 'debug'
# DEFAULT_STDOUT_LEVEL = 'info'
# DEFAULT_LOG_FILE = './default.log'
# DEFAULT_LOG_FORMAT = '%(asctime)s %(levelname)-7s %(message)s'

# LOG_LEVEL_DICT = {
#     'debug': logging.DEBUG,
#     'info': logging.INFO,
#     'warning': logging.WARNING,
#     'error': logging.ERROR,
#     'critical': logging.CRITICAL
# }


# class Logger:
#     """
#     Args:
#       Log level: CRITICAL>ERROR>WARNING>INFO>DEBUG.
#       Log file: The file that stores the logging info.
#       rewrite: Clear the log file.
#       log format: The format of log messages.
#       stdout level: The log level to print on the screen.
#     """
#     logfile_level = None
#     log_file = None
#     log_format = None
#     rewrite = None
#     stdout_level = None
#     logger = None

#     @staticmethod
#     def init(logfile_level=DEFAULT_LOGFILE_LEVEL,
#              log_file=DEFAULT_LOG_FILE,
#              log_format=DEFAULT_LOG_FORMAT,
#              rewrite=False,
#              stdout_level=None):
#         assert Logger.logger is None
#         Logger.logfile_level = logfile_level
#         Logger.log_file = log_file
#         Logger.log_format = log_format
#         Logger.rewrite = rewrite
#         Logger.stdout_level = stdout_level

#         Logger.logger = logging.getLogger()
#         fmt = logging.Formatter(Logger.log_format)

#         if Logger.logfile_level is not None:
#             filemode = 'w'
#             if not Logger.rewrite:
#                 filemode = 'a'

#             dir_name = os.path.dirname(os.path.abspath(Logger.log_file))
#             if not os.path.exists(dir_name):
#                 os.makedirs(dir_name)

#             if Logger.logfile_level not in LOG_LEVEL_DICT:
#                 print('Invalid logging level: {}'.format(Logger.logfile_level))
#                 Logger.logfile_level = DEFAULT_LOGFILE_LEVEL

#             Logger.logger.setLevel(LOG_LEVEL_DICT[Logger.logfile_level])

#             fh = logging.FileHandler(Logger.log_file, mode=filemode)
#             fh.setFormatter(fmt)
#             fh.setLevel(LOG_LEVEL_DICT[Logger.logfile_level])

#             Logger.logger.addHandler(fh)

#         if stdout_level is not None:
#             if Logger.logfile_level is None:
#                 Logger.logger.setLevel(LOG_LEVEL_DICT[Logger.stdout_level])

#             console = logging.StreamHandler()
#             if Logger.stdout_level not in LOG_LEVEL_DICT:
#                 print('Invalid logging level: {}'.format(Logger.stdout_level))
#                 return
#             Logger.info('before level')
#             console.setLevel(LOG_LEVEL_DICT[Logger.stdout_level])
#             Logger.info('after level')
#             console.setFormatter(fmt)
#             Logger.info('after formattwer')
#             Logger.logger.addHandler(console)

#     @staticmethod
#     def check_logger():
#         if Logger.logger is None:
#             Logger.init(logfile_level=None, stdout_level=DEFAULT_STDOUT_LEVEL)

#     @staticmethod
#     def debug(message):
#         Logger.check_logger()
#         filename = os.path.basename(sys._getframe().f_back.f_code.co_filename)
#         lineno = sys._getframe().f_back.f_lineno
#         prefix = '[{}, {}]'.format(filename,lineno)
#         Logger.logger.debug('{} {}'.format(prefix, message))

#     @staticmethod
#     def info(message):
#         Logger.check_logger()
#         filename = os.path.basename(sys._getframe().f_back.f_code.co_filename)
#         lineno = sys._getframe().f_back.f_lineno
#         prefix = '[{}, {}]'.format(filename,lineno)
#         Logger.logger.info('{} {}'.format(prefix, message))

#     @staticmethod
#     def warn(message):
#         Logger.check_logger()
#         filename = os.path.basename(sys._getframe().f_back.f_code.co_filename)
#         lineno = sys._getframe().f_back.f_lineno
#         prefix = '[{}, {}]'.format(filename,lineno)
#         Logger.logger.warn('{} {}'.format(prefix, message))

#     @staticmethod
#     def error(message):
#         Logger.check_logger()
#         filename = os.path.basename(sys._getframe().f_back.f_code.co_filename)
#         lineno = sys._getframe().f_back.f_lineno
#         prefix = '[{}, {}]'.format(filename,lineno)
#         Logger.logger.error('{} {}'.format(prefix, message))

#     @staticmethod
#     def critical(message):
#         Logger.check_logger()
#         filename = os.path.basename(sys._getframe().f_back.f_code.co_filename)
#         lineno = sys._getframe().f_back.f_lineno
#         prefix = '[{}, {}]'.format(filename,lineno)
#         Logger.logger.critical('{} {}'.format(prefix, message))

# def info(msg):
#     return Logger.info(msg)

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--logfile_level', default="debug", type=str,
#                         dest='logfile_level', help='To set the log level to files.')
#     parser.add_argument('--stdout_level', default=None, type=str,
#                         dest='stdout_level', help='To set the level to print to screen.')
#     parser.add_argument('--log_file', default="./default.log", type=str,
#                         dest='log_file', help='The path of log files.')
#     parser.add_argument('--log_format', default="%(asctime)s %(levelname)-7s %(message)s",
#                         type=str, dest='log_format', help='The format of log messages.')
#     parser.add_argument('--rewrite', default=False, type=bool,
#                         dest='rewrite', help='Clear the log files existed.')

#     args = parser.parse_args()
#     Logger.init(logfile_level=args.logfile_level, stdout_level=args.stdout_level,
#                 log_file=args.log_file, log_format=args.log_format, rewrite=args.rewrite)

#     Logger.info("info test.")
#     Logger.debug("debug test.")
#     Logger.warn("warn test.")
#     Logger.error("error test.")
#     Logger.debug("debug test.")