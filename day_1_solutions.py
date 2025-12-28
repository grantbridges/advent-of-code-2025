from base_aoc_day_solutions import *

# https://adventofcode.com/2025/day/1

class Day1Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 1)

    def part_1(self):
        current_pos = 50
        zeros_count = 0
        with open(self.input_file, 'r') as f:
            for line in f:
                dir = str(line[0]) # L or R
                dist = int(line[1:]) # number after direction

                delta = 1 if dir == 'R' else -1
                for i in range(0, dist):
                    # handle wrapping
                    if delta == 1 and current_pos == 99:
                        current_pos = 0
                    elif delta == -1 and current_pos == 0:
                        current_pos = 99
                    else:
                        current_pos += delta
                
                # track if we ended at 0 after this rotation
                if current_pos == 0:
                    zeros_count += 1
        return zeros_count

    def part_2(self):
        current_pos = 50
        zeros_count = 0
        with open(self.input_file, 'r') as f:
            for line in f:
                dir = str(line[0]) # L or R
                dist = int(line[1:]) # number after direction

                delta = 1 if dir == 'R' else -1
                for i in range(0, dist):
                    # handle wrapping
                    if delta == 1 and current_pos == 99:
                        current_pos = 0
                    elif delta == -1 and current_pos == 0:
                        current_pos = 99
                    else:
                        current_pos += delta
                
                    # track if we ended at 0 after this incremental rotation
                    if current_pos == 0:
                        zeros_count += 1

        return zeros_count
    
Day1Solutions().run_solutions()