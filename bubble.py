import pyxel
from itertools import cycle
from copy import copy
from constants import BUBBLE_RADIUS_MIN, BUBBLE_RADIUS_MAX, BUBBLE_COLOR_CYCLE

class Bubble:
  def __init__(self, x, y, radius, index):
    self.x = x
    self.y = y
    self.radius = radius
    self.index = index

    self.BUBBLE_COLOR_CYCLE = copy(BUBBLE_COLOR_CYCLE)
    self.color = next(self.BUBBLE_COLOR_CYCLE)
    for i in range(self.index):
      self.color = next(self.BUBBLE_COLOR_CYCLE)

    self.visible = False

  def update(self, instructions: [str]):
    if instructions:
      self.visible = True

    for instruction in instructions:
      match instruction:
        case 'color': self.color = next(self.BUBBLE_COLOR_CYCLE)
        case 'bigger': self.increment(1)
        case 'smaller': self.increment(-1)
        case 'up': self.y -= 1
        case 'down': self.y += 1
        case 'left': self.x -= 1
        case 'right': self.x += 1
        case 'wide': pass
        case 'narrow': pass
        case _: raise Exception(f'Invalid instruction: {instruction}')

  def draw(self):
    if not self.visible:
      return

    self.draw_circle()
    self.draw_highlight()
    self.draw_border()

  ############################

  def increment(self, amount: int):
    if self.radius + amount in range(BUBBLE_RADIUS_MIN, BUBBLE_RADIUS_MAX + 1):
      self.radius += amount

  ############################

  def draw_circle(self):
    pyxel.circ(
      self.x,
      self.y,
      self.radius,
      self.color,
    )

  def draw_highlight(self):
    pyxel.blt(
      self.x, self.y - pyxel.floor(self.radius * 0.75) - 1,
      0,
      0, 8,
      8, 8,
      pyxel.COLOR_BLACK
    )

  def draw_border(self):
    pyxel.circb(self.x, self.y, self.radius + 1, pyxel.COLOR_NAVY)
