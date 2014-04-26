class tinylog:
  def __init__(self, filename):
    self.filename = open(filename, "a+")

  def warn(self, msg):
    self.filename.write("WARN: " + msg + "\n")

log = tinylog("out.log")
log.warn("There's a problem")
