import math
from typing import List
from base_aoc_day_solutions import *

# https://adventofcode.com/2025/day/8

class Box():
    x: int
    y: int
    z: int

    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def dist(self, other: Box):
        return math.sqrt(
            math.pow(other.x - self.x, 2) + 
            math.pow(other.y - self.y, 2) + 
            math.pow(other.z - self.z, 2)
        )

    @staticmethod
    def get_boxes_from_file(input_file):
        boxes = List[Box]
        with open (input_file, 'r') as f:
            for line in f:
                boxes.append(Box.create_from_text(line))
        return boxes

    @staticmethod
    def create_from_text(text):
        box = Box()
        vals = text.split(',')
        box.x = vals[0]
        box.y = vals[1]
        box.z = vals[2]
        return box

class Day8Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 8)

    def part_1(self):
        boxes = Box.get_boxes_from_file(self.input_sample_file)
        return 0

    def part_2(self):
        return 0
    
Day8Solutions().run_solutions()