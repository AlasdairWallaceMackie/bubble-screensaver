import pyxel
from itertools import cycle

BUBBLE_RADIUS_MIN = 5
BUBBLE_RADIUS_MAX = 8

class Bubble:
  def __init__(self, x, y, radius, color_offset):
    self.BUBBLE_COLOR_CYCLE = cycle([
      pyxel.COLOR_RED,
      pyxel.COLOR_ORANGE,
      pyxel.COLOR_YELLOW,
      pyxel.COLOR_GREEN,
      pyxel.COLOR_CYAN,
      pyxel.COLOR_PINK,
    ])

    self.x = x
    self.y = y
    self.radius = radius

    self.color = next(self.BUBBLE_COLOR_CYCLE)
    for i in range(color_offset):
      self.color = next(self.BUBBLE_COLOR_CYCLE)

    assert self.color

  def update(self, instructions: [str]):
    for instruction in instructions:
      match instruction:
        case 'color': self.color = next(self.BUBBLE_COLOR_CYCLE)
        case 'bigger': self.increment(1)
        case 'smaller': self.increment(-1)
        case 'up': self.y -= 1
        case 'down': self.y += 1
        case _: raise Exception(f'Invalid instruction: {instruction}')

  def draw(self):
    self.draw_circle()
    self.draw_highlight(
      self.x + pyxel.floor(self.radius / 2) - 1,
      self.y - pyxel.floor(self.radius / 2) - 1,
    )

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

  def draw_highlight(self, x, y):
    pyxel.rect(x, y, 2, 2, pyxel.COLOR_WHITE)
    pyxel.rect(x + 1, y + 1, 2, 2, pyxel.COLOR_WHITE)
