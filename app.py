import os, sys
import pyxel
from .screensaver import Screensaver

WINDOW_WIDTH = 128
WINDOW_HEIGHT= WINDOW_WIDTH

class App:
  def __init__(self):
    pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT)

    self.screensaver = Screensaver()

    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btn(pyxel.KEY_GUI) and pyxel.btn(pyxel.KEY_R):
      print("RESTARTING")
      os.execv(sys.executable, ['pyxel'] + sys.argv)

    self.screensaver.update()

  def draw(self):
    self.screensaver.draw()
