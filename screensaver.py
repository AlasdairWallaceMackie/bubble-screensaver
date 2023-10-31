import pyxel
import random
from constants import *
from collections import deque
from bubble_line import BubbleLine

class Screensaver:
  def __init__(self):
    self.bubble_lines = [
      BubbleLine(
        -2 * i,
        -32 + (i * BUBBLE_SPACING ),
        BUBBLE_LINE_LENGTH
      ) for i in range(BUBBLE_LINE_COUNT)
    ]
    self.instruction_queue = deque([[] for l in range(BUBBLE_LINE_COUNT)], BUBBLE_LINE_COUNT)

  def update(self):
    if pyxel.frame_count % SCREENSAVER_SPEED != 0:
      return

    new_instructions = []

    if random_chance(16):
      new_instructions.append('color')
    if random_chance(1):
      new_instructions.append('bigger')
    if random_chance(1):
      new_instructions.append('smaller')
    if random_chance(1):
      new_instructions.append('up')
    if random_chance(1):
      new_instructions.append('down')
    if random_chance(5):
      new_instructions.append('left')
    if random_chance(5):
      new_instructions.append('right')

    for index, instructions in enumerate(self.instruction_queue):
      self.bubble_lines[index].update(instructions)

    self.instruction_queue.appendleft(new_instructions)

  def draw(self):
    for line in self.bubble_lines:
      line.draw()

  #################################

def random_chance(odds_damper):
  chances = [True] + [False for i in range(odds_damper)]
  return random.choice(chances)

"""
Wave
  |
  v
Line
  |
  v
Bubble - Use circle with white highlights

"""

"""
Each bubble line has a stack of instructions
An instruction is sent and it is passed once to each bubble in the line
  There can be multiple instructions when a command is sent
After the last bubble has been updated, remove the instruction
"""
