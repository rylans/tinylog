import datetime

class tinylog:
  def __init__(self, filename):
    self.filename = open(filename, "a+")

  def write(self, level, msg):
    t = str(datetime.datetime.utcnow()).split('.')[0]
    self.filename.write(t + " " + level + " " + msg + "\n")

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

log = tinylog("out.log")
log.info("Here is an info message")
log.warn("There's a problem")
log.debug("This is a debug message")
log.error("An error is happening")
log.critical("Something bad is happening")
