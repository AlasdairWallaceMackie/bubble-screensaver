import pyxel
from itertools import cycle

BUBBLE_RADIUS_MIN = 5
BUBBLE_RADIUS_MAX = 8
BUBBLE_COLOR_CYCLE = cycle([
  pyxel.COLOR_RED,
  pyxel.COLOR_ORANGE,
  pyxel.COLOR_YELLOW,
  pyxel.COLOR_GREEN,
  pyxel.COLOR_CYAN,
  pyxel.COLOR_PINK,
])
BUBBLE_RADIUS_CYCLE = cycle(
  [r for r in range(BUBBLE_RADIUS_MIN, BUBBLE_RADIUS_MAX + 1)]
  + [r for r in range(BUBBLE_RADIUS_MIN, BUBBLE_RADIUS_MAX)][::-1]
)
BUBBLE_Y_POSITION_CYCLE = cycle([1,1,1,1,1,-1,-1,-1,-1])

class Bubble:
  def __init__(self, x, y, radius, color_offset):
    self.x = x
    self.y = y
    self.radius = next(BUBBLE_RADIUS_CYCLE)

    for i in range(color_offset):
      self.color = next(BUBBLE_COLOR_CYCLE)

  def update(self):
    self.color = next(BUBBLE_COLOR_CYCLE)
    self.radius = next(BUBBLE_RADIUS_CYCLE)
    self.y += next(BUBBLE_Y_POSITION_CYCLE)

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
