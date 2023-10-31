import pyxel
from bubble_line import BubbleLine

class Screensaver:
  def __init__(self):
    self.bubble_line = BubbleLine(-2, 32)

  def update(self):
    self.bubble_line.update()

  def draw(self):
    self.bubble_line.draw()

"""
Wave
  |
  v
Line
  |
  v
Bubble - Use circle with white highlights

"""
