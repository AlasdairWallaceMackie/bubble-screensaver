import pyxel
from itertools import cycle
from bubble import Bubble

BUBBLE_COUNT = 16
BUBBLE_LINE_SPEED = 4 # Higher is slower

class BubbleLine:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.current_index = 0

    self.bubbles = [
      Bubble(
        self.x + (i * 9), self.y,
        5,
        i
      )
      for i in range(BUBBLE_COUNT)
    ]

  def update(self):
    if pyxel.frame_count % BUBBLE_LINE_SPEED == 0:
      self.bubbles[self.current_index].update()
      self.current_index += 1
      if self.current_index >= len(self.bubbles):
        self.current_index = 0

  def draw(self):
    for bubble in self.bubbles:
      bubble.draw()

  #########################

  def translate_position(self, dx, dy):
    self.x += dx 
    self.y += dy
    for bubble in self.bubbles:
      bubble.x += dx 
      bubble.y += dy

