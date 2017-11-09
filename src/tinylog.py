import datetime

CRITICAL = 5
ERROR = 4
WARN = 3
INFO = 2
DEBUG = 1
ALL = 0

class tinylog:
  def __init__(self, filename, level=ALL):
    """
    Initialize the logger, open the output file and set the logging level.
    """
    self.filehandle = open(filename, "a+")
    self.level = level

  def setLevel(self, level):
    """
    Set the logging level. Log messages of a lower message will be ignored.
    """
    self.level = level

  def write(self, levelstring, lvl, msg):
    """
    Write the log message to the file if the logging level allows it.
    """
    if (lvl >= self.level):
      t = str(datetime.datetime.utcnow()).split('.')[0]
      output_message = t + " " + levelstring + " " + msg
      self.filehandle.write(output_message + "\n")

  def debug(self, msg):
    """
    Write a debug message to the output file.
    """
    self.write("DEBUG", 1,  msg)

  def info(self, msg):
    """
    Write an info message to the output file.
    """
    self.write("INFO", 2,  msg)

  def warn(self, msg):
    """
    Write a warning message to the output file.
    """
    self.write("WARN", 3, msg)

  def error(self, msg):
    """
    Write an error message to the output file.
    """
    self.write("ERROR", 4, msg)

  def critical(self, msg):
    """
    Write a critical message to the output file
    """
    self.write("CRITICAL", 5, msg)

if __name__ == '__main__':
  log = tinylog("out.log", ALL)
  log.info("Info")
  log.warn("Warning")
  log.debug("Debug")
  log.error("Error")
  log.critical("Critical")
