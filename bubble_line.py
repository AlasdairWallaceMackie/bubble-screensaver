import pyxel
import constants
from collections import deque
from bubble import Bubble

class BubbleLine:
  def __init__(self, x, y, bubble_count, index):
    self.x = x
    self.y = y
    self.index = index

    self.instruction_queue = deque([[] for b in range(bubble_count)], bubble_count)

    self.bubbles = [
      Bubble(
        self.x + (i * constants.BUBBLE_SPACING), self.y,
        5,
        i
      ) for i in range(bubble_count)
    ]

  def update(self, new_instructions: [str]):
    for index, instructions in enumerate(self.instruction_queue):
      self.bubbles[index].update(instructions)

    self.instruction_queue.appendleft(new_instructions)

  def draw(self):
    for bubble in self.bubbles[::-1]:
      bubble.draw()

  #########################

  def translate_position(self, dx, dy):
    self.x += dx 
    self.y += dy
    for bubble in self.bubbles:
      bubble.x += dx 
      bubble.y += dy

