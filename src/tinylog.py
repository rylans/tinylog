import datetime

CRITICAL = 5
ERROR = 4
WARN = 3
INFO = 2
DEBUG = 1
ALL = 0

class tinylog:
  def __init__(self, filename, level=ALL):
    self.filename = open(filename, "a+")
    self.level = level

  def setLevel(self, level):
    self.level = level

  def write(self, levelstring, lvl, msg):
    if (lvl >= self.level):
      t = str(datetime.datetime.utcnow()).split('.')[0]
      output_message = t + " " + levelstring + " " + msg
      self.filename.write(output_message + "\n")

  def debug(self, msg):
    self.write("DEBUG", 1,  msg)

  def info(self, msg):
    self.write("INFO", 2,  msg)

  def warn(self, msg):
    self.write("WARN", 3, msg)

  def error(self, msg):
    self.write("ERROR", 4, msg)

  def critical(self, msg):
    self.write("CRITICAL", 5, msg)

if __name__ == '__main__':
  log = tinylog("out.log", ALL)
  log.info("Info")
  log.warn("Warning")
  log.debug("Debug")
  log.error("Error")
  log.critical("Critical")
