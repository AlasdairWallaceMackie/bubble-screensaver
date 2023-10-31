import pyxel
import random
from collections import deque
from bubble_line import BubbleLine

SCREENSAVER_SPEED = 4 # Higher is slower
BUBBLE_LINE_LENGTH = 16
BUBBLE_LINE_COUNT = 1

class Screensaver:
  def __init__(self):
    self.bubble_lines = [BubbleLine(-2, 32, BUBBLE_LINE_LENGTH)]
    self.instruction_queue = deque([[] for l in range(BUBBLE_LINE_COUNT)], BUBBLE_LINE_COUNT)

  def update(self):
    if pyxel.frame_count % SCREENSAVER_SPEED != 0:
      return

    new_instructions = []
    if random_chance(6):
      new_instructions.append('color')
    if random_chance(1):
      new_instructions.append('bigger')
    if random_chance(1):
      new_instructions.append('smaller')
    if random_chance(1):
      new_instructions.append('up')
    if random_chance(1):
      new_instructions.append('down')

    for index, instructions in enumerate(self.instruction_queue):
      self.bubble_lines[index].update(instructions)

    self.instruction_queue.appendleft(new_instructions)

  def draw(self):
    for line in self.bubble_lines:
      line.draw()

  #################################

def frame_count_last_digit():
  return int(str(pyxel.frame_count)[-1])

def coin_flip():
  return random.choice([True, False])

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
