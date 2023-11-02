import pyxel
import random
from constants import *
from collections import deque
from bubble_line import BubbleLine

class Screensaver:
  def __init__(self):
    self.dx = 0
    self.dy = 0

    self.current_spacing = BUBBLE_SPACING

    self.bubble_lines = [
      BubbleLine(
        SCREENSAVER_ORIGIN_X * i,
        SCREENSAVER_ORIGIN_Y + (i * BUBBLE_SPACING ),
        BUBBLE_LINE_LENGTH,
        i
      ) for i in range(BUBBLE_LINE_COUNT)
    ]

    self.instruction_queue = deque([[] for l in range(BUBBLE_LINE_COUNT)], BUBBLE_LINE_COUNT)

  def update(self):
    if pyxel.frame_count % SCREENSAVER_SPEED != 0:
      return
    
    self.update_bubble_lines()
    self.instruction_queue.appendleft(self.generate_new_instructions())

  def draw(self):
    for line in self.bubble_lines:
      line.draw()

  #################################

  def update_bubble_lines(self):
    for index, instructions in enumerate(self.instruction_queue):
      self.bubble_lines[index].update(instructions)

  def generate_new_instructions(self):
    new_instructions = []

    if random_chance(12):
      new_instructions.append('color')
    if random_chance(1):
      new_instructions.append('bigger')
    if random_chance(1):
      new_instructions.append('smaller')
    if random_chance(1) and self.dy >= SCREENSAVER_DY_MIN:
      new_instructions.append('up')
      self.dy -= 1
    if random_chance(1) and self.dy <= SCREENSAVER_DY_MAX:
      new_instructions.append('down')
      self.dy += 1
    if random_chance(5) and self.dx >= SCREENSAVER_DX_MIN:
      new_instructions.append('left')
      self.dx -= 1
    if random_chance(5) and self.dx <= SCREENSAVER_DX_MAX:
      new_instructions.append('right')
      self.dx += 1
    if random_chance(12) and self.current_spacing <= BUBBLE_SPACING_MAX:
      new_instructions.append('wide')
      self.current_spacing += 1
    if random_chance(12) and self.current_spacing >= BUBBLE_SPACING_MIN:
      new_instructions.append('narrow')
      self.current_spacing -= 1

    return new_instructions

def random_chance(odds_damper):
  chances = [True] + [False for i in range(odds_damper)]
  return random.choice(chances)
