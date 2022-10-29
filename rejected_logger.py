import datetime


class Logger(object):
    """ A file-based message logger with the following properties

    Attributes:
        file_name: a string representing the full path of the log file to which this logger will write its messages.
    """

    def __init__(self, file_name):
        """ Return a Logger object whose file_name is *file_name* """
        self.file_name = file_name

    def _write_log(self, level, msg):
        """ Writes a message to the file_name for a specific Logger instance """
        with open(self.file_name, 'a') as f:
            f.write('[{0}] - {1}\n  {2} \n'.format(datetime.datetime.now(), level, msg))

    def critical(self, level, msg):
        self._write_log('CRITICAL', msg)

    def error(self, level, msg):
        self._write_log('ERROR', msg)

    def warning(self, level, msg):
        self._write_log('WARNING', msg)

    def info(self, level, msg):
        self._write_log('INFO', msg)

    def debug(self, level, msg):
        self._write_log('DEBUG', msg)
