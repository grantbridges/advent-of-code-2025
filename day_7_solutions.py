from base_aoc_day_solutions import *

# https://adventofcode.com/2025/day/7

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
        return 0
    
Day7Solutions().run_solutions()