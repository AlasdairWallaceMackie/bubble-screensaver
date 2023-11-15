import os, sys
import pyxel
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, RECURSION_LIMIT
from screensaver import Screensaver

class App:
  def __init__(self):
    pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT)
    pyxel.load("sprites.pyxres")

    self.screensaver = Screensaver()

    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btn(pyxel.KEY_GUI) and pyxel.btn(pyxel.KEY_R):
      print("RESTARTING")
      os.execv(sys.executable, ['pyxel'] + sys.argv)

    self.screensaver.update()

  def draw(self):
    pyxel.cls(pyxel.COLOR_BLACK)
    self.screensaver.draw()

sys.setrecursionlimit(RECURSION_LIMIT)
App()
