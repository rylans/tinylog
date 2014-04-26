from __future__ import print_function
import datetime

class tinylog:
  def __init__(self, filename, printout=False):
    self.filename = open(filename, "a+")

    if printout:
      self.print = print
    else:
      self.print = lambda x: None

  def write(self, level, msg):
    t = str(datetime.datetime.utcnow()).split('.')[0]
    output_message = t + " " + level + " " + msg
    self.filename.write(output_message + "\n")
    self.print(output_message)

  def warn(self, msg):
    self.write("WARN", msg)

  def debug(self, msg):
    self.write("DEBUG", msg)

  def info(self, msg):
    self.write("INFO", msg)

  def error(self, msg):
    self.write("ERROR", msg)

  def critical(self, msg):
    self.write("CRITICAL", msg)

if __name__ == '__main__':
  log = tinylog("out.log", True)
  log.info("Here is an info message")
  log.warn("There's a problem")
  log.debug("This is a debug message")
  log.error("An error is happening")
  log.critical("Something bad is happening")
