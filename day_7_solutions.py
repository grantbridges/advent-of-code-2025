from typing import List
from base_aoc_day_solutions import *

# https://adventofcode.com/2025/day/7

class Day2Solver():
    lines: List[str] = []
    lines_count: int
    line_length: int

    # computed output
    paths_count: int

    def __init__(self):
        self.lines = []
        self.lines_count = 0
        self.line_length = 0
        self.path_count = 0

    def init_from_file(self, input_file: str):
        self.lines = []
        self.path_count = 0

        with open (input_file, 'r') as f:
            for line in f.readlines():
                self.lines.append(line.strip())

            # store out some lookup properties for ease of access later
            self.lines_count = len(self.lines)
            self.line_length = len(self.lines[0]) # all line lengths are the same

    def calculate_all_paths(self):
        # Starting x is on the "S" value of first line
        x = self.lines[0].find('S')
        self._move_to(1, x)

    def _move_to(self, row_index: int, x: int):
        if row_index < self.lines_count:
            line = self.lines[row_index]

            if line[x] == '^':
                # Found a split! Move to left and right
                # (test data doesn't have ^ ever show up on the far edges, so not
                # worrying about the literal edge cases here of x being out of bounds)
                self._move_to(row_index + 1, x - 1)
                self._move_to(row_index + 1, x + 1)
            else:
                # Keep heading down same direction
                self._move_to(row_index + 1, x)
        else:
            # Reached bottom! Add this path to our list of finished paths
            self.path_count += 1

class Day7Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 7)

    def part_1(self):
        split_count = 0
        with open(self.input_file, 'r') as f:
            lines = f.readlines()

            first_line = lines[0].strip()
            start_x = first_line.find('S')

            # track index of each beam
            previous_line_beams = [start_x]

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

        return split_count

    def part_2(self):
        solver = Day2Solver()
        solver.init_from_file(self.input_file)
        solver.calculate_all_paths()
        return solver.path_count
    
#Day7Solutions().run_solutions()
Day7Solutions().run_solution_part(2)