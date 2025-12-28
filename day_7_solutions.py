from typing import List
from collections import defaultdict
from base_aoc_day_solutions import *

# https://adventofcode.com/2025/day/7

class Day2RecursiveSolver():
    # (!) Abandoned using this approach - it'd work, but would take ~32 days of computing to finish solving
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
            for line in f:
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
                # Found a splitter! Move to left and right
                # (test data doesn't have ^ ever show up on the far edges, so not
                # worrying about the literal edge cases here of x being out of bounds)
                self._move_to(row_index + 1, x - 1)
                self._move_to(row_index + 1, x + 1)
            else:
                # Keep heading down same direction
                self._move_to(row_index + 1, x)
        else:
            # Reached bottom! Increment found paths
            self.path_count += 1

class Day7Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 7)

    def part_1(self):
        split_count = 0
        with open(self.input_file, 'r') as f:
            # track column indices where beams existed on previous line
            prev_line_beams: List[int] = []

            for row_index, line in enumerate(f):
                line = line.strip()

                curr_line_beams = set()
                curr_line_splitters = set()

                if row_index == 0:
                    # first line - starting column is at 'S'
                    start_col_index = line.find('S')
                    curr_line_beams.add(start_col_index)
                else:
                    for col_index in prev_line_beams:
                        if line[col_index] == '^':
                            # split!
                            split_count += 1
                            curr_line_splitters.add(col_index)
                            curr_line_beams.add(col_index-1)
                            curr_line_beams.add(col_index+1)
                        else:
                            # no collision - extend straight down
                            curr_line_beams.add(col_index)

                # can't have a beam on a splitter - filter out before reassigning current line beams to previous
                prev_line_beams[:] = [beam for beam in curr_line_beams if beam not in curr_line_splitters]

        return split_count

    def part_2(self):
        total_paths_count = 0
        with open(self.input_file, 'r') as f:
            # use a dictionary to track number of paths currently following 
            # each column downward on previous line
            # key: column index; value: # of paths currently following it
            prev_line_paths = defaultdict(int)

            for row_index, line in enumerate(f):
                line = line.strip()

                curr_line_paths = defaultdict(int)

                if row_index == 0:
                    # first line - starting column is at 'S'
                    start_col_index = line.find('S')
                    curr_line_paths[start_col_index] = 1
                else:
                    # iterate over each entry in prev line's paths to build new paths
                    for (col_index, paths_count) in prev_line_paths.items():
                        if line[col_index] == '^':
                            # split!
                            curr_line_paths[col_index - 1] += paths_count
                            curr_line_paths[col_index + 1] += paths_count
                        else:
                            # no collision - extend straight down
                            curr_line_paths[col_index] += paths_count
                        
                # reassign current line paths to previous and keep iterating
                prev_line_paths = curr_line_paths

            total_paths_count = sum(prev_line_paths.values())

        return total_paths_count
    
Day7Solutions().run_solutions()