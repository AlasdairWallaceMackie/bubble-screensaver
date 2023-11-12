import pyxel
from copy import copy
from constants import BUBBLE_RADIUS_MIN, BUBBLE_RADIUS_MAX, BUBBLE_COLOR_CYCLE, BUBBLE_BORDER_COLOR, SCREENSAVER_BACKGROUND_COLOR

class Bubble:
  def __init__(self, x, y, radius, index):
    self.x = x
    self.y = y
    self.radius = radius
    self.index = index

    self.COLOR_CYCLE = copy(BUBBLE_COLOR_CYCLE)
    self.current_color = self.init_color()
    self.next_color = next(self.COLOR_CYCLE)
    self.is_color_transitioning = False

    self.visible = False

  def update(self, instructions: [str]):
    if instructions:
      self.visible = True

    self.update_color()
    self.carry_out_instructions(instructions)

  def draw(self):
    if not self.visible:
      return

    self.draw_border()
    self.draw_circle()
    self.draw_dithering()
    self.draw_highlight()

  ############################

  def init_color(self):
    """ Offsetting the color by the instance index ensures neighbors don't have the same color """
    color = next(self.COLOR_CYCLE)
    for i in range(self.index):
      color = next(self.COLOR_CYCLE)

    return color

  def increment_radius(self, amount: int):
    """ Use negative integers to shrink radius """
    if self.radius + amount in range(BUBBLE_RADIUS_MIN, BUBBLE_RADIUS_MAX + 1):
      self.radius += amount

  def carry_out_instructions(self, instructions: [str]):
    for instruction in instructions:
      match instruction:
        case 'color':
          self.is_color_transitioning = True
        case 'bigger': self.increment_radius(1)
        case 'smaller': self.increment_radius(-1)
        case 'up': self.y -= 1
        case 'down': self.y += 1
        case 'left': self.x -= 1
        case 'right': self.x += 1
        case 'wide': pass
        case 'narrow': pass
        case _: raise Exception(f'Invalid instruction: {instruction}')

  def update_color(self):
    if not self.is_color_transitioning:
      return
    
    self.current_color = self.next_color
    self.next_color = next(self.COLOR_CYCLE)
    self.is_color_transitioning = False

  ############################

  def draw_circle(self):
    pyxel.circ(
      self.x,
      self.y,
      self.radius,
      self.current_color,
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
    pyxel.circ(self.x, self.y, self.radius + 1, BUBBLE_BORDER_COLOR)

  ######################
  # Dithering Functions
  ######################

  def draw_dithering(self):
    if not self.is_color_transitioning:
      return

    try:
      # We are offsetting the start point of the dithering algorithm. If it's initiated in the bubble's center, there will be an issue if the center is inside a neighbor bubble.
      self.recursive_dither(
        self.x + ((self.radius / 2) + 1),
        self.y - ((self.radius / 2) + 1),
      )
    except:
      # There is still a rare chance of a RecursionError, so we catch it here
      return

  def recursive_dither(self, x, y):
    location_color = pyxel.pget(x, y)

    if location_color in [BUBBLE_BORDER_COLOR, SCREENSAVER_BACKGROUND_COLOR]:
      return
    
    if location_color == self.current_color and not self.found_next_color_in_neighbor(x, y):
      pyxel.pset(x, y, self.next_color)

    self.color_neighbors(x, y)

  def found_next_color_in_neighbor(self, x, y) -> bool:
    for new_x, new_y in self.neighbor_coordinates(x, y):
      if pyxel.pget(new_x, new_y) == self.next_color:
        return True
      
    return False

  def color_neighbors(self, x, y):
    for new_x, new_y in self.neighbor_coordinates(x, y):
      if pyxel.pget(new_x, new_y) != self.next_color:
        self.recursive_dither(new_x, new_y)

  def neighbor_coordinates(self, x, y) -> [int, int]:
    return [
      (x + 1, y),
      (x - 1, y),
      (x, y + 1),
      (x, y - 1),
    ]
