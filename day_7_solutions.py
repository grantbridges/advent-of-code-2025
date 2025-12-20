import math
from typing import List
from base_aoc_day_solutions import *

# https://adventofcode.com/2025/day/7

class Day2Solver():
    lines: List[str] = []
    paths: List[List[int]] = [] # each path is an array of x indices - all paths should be same length

    lines_count: int
    line_length: int

    def __init__(self):
        self.lines = []
        self.paths = []

    def init_from_file(self, input_file: str):
        self.lines = []
        self.paths = []

        with open (input_file, 'r') as f:
            for line in f.readlines():
                self.lines.append(line.strip())

            # store out some lookup properties for ease of access later
            self.lines_count = len(self.lines)
            self.line_length = len(self.lines[0]) # all line lengths are the same

    def calculate_all_paths(self):
        # Starting x is on the "S" value of first line
        x = self.lines[0].find('S')

        path = [x]
        self._move_to(1, x, path)

    def _move_to(self, row_index: int, x: int, path: List[int]):
        if row_index < self.lines_count:
            line = self.lines[row_index]

            if line[x] == '^':
                # Found a split! Move to left and right
                left_x = x - 1
                right_x = x + 1
                # (test data doesn't have ^ ever show up on the far edges, so not
                # worrying about the literal edge cases here of x being out of bounds)

                # Keep passing current path on down left route, but make a copy for right
                left_path = path
                right_path = path[:]

                left_path.append(left_x)
                right_path.append(right_x)

                self._move_to(row_index + 1, left_x, left_path)
                self._move_to(row_index + 1, right_x, right_path)
            else:
                # Keep heading down same direction
                path.append(x)
                self._move_to(row_index + 1, x, path)
        else:
            # Reached bottom! Add this path to our list of finished paths
            self.paths.append(path)

class Day7Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 7)

    def part_1(self):
        split_count = 0
        with open(self.input_file, 'r') as f:
            lines = f.readlines()

            first_line = lines[0].strip()
            line_length = len(first_line) # all line lengths are the same
            start_x = first_line.find('S')

            # track index of each beam
            previous_line_beams = [start_x]

            debug_line = ''
            for j in range(0, line_length):
                if j == start_x:
                    debug_line += 'S'
                else:
                    debug_line += '.'
            print(debug_line)

            for i in range(1, len(lines)):
                line = lines[i].strip()
                new_beams = set()
                splitters = set()
                for b in previous_line_beams:
                    if line[b] == '^':
                        # split!
                        split_count += 1
                        splitters.add(b)
                        if b > 0:
                            new_beams.add(b-1)
                        if b < len(line) - 1:
                            new_beams.add(b+1)
                    else:
                        # no collision - extend straight down
                        new_beams.add(b)
                previous_line_beams = list(new_beams)

                # can't have a beam on a splitter
                previous_line_beams[:] = [beam for beam in previous_line_beams if beam not in splitters]

                # print out for testing
                debug_line = ''
                for j in range(0, line_length):
                    if j in splitters:
                        debug_line += '^'
                    elif j in previous_line_beams:
                        debug_line += '|'
                    else:
                        debug_line += '.'
                print(debug_line)

        return split_count

    def part_2(self):
        solver = Day2Solver()
        solver.init_from_file(self.input_file)
        solver.calculate_all_paths()

        return len(solver.paths)
    
Day7Solutions().run_solutions()