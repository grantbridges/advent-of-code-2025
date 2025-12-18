from typing import List
from base_aoc_day_solutions import *

# https://adventofcode.com/2025/day/5

class IdRange():
    first_id: int
    last_id: int
    def __init__(self, first_id, last_id):
        self.first_id = first_id
        self.last_id = last_id

    def contains(self, id):
        return self.first_id <= id and self.last_id >= id

class Day5Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 5)

    def part_1(self):
        fresh_ranges: List[IdRange] = []
        available_ids = []
        with open(self.input_file, 'r') as f:
            reading_ranges = True
            for line in f.readlines():
                line = line.strip()
                if reading_ranges and line == '':
                    # transition to reading available ingredient Ids
                    reading_ranges = False
                    continue

                if reading_ranges:
                    ids = line.split('-')
                    fresh_ranges.append(IdRange(int(ids[0]), int(ids[1])))
                else:
                    available_ids.append(int(line))

        log_debug(f'Finished parsing {len(fresh_ranges)} ranges of fresh ingredients')

        fresh_avail_count = 0
        for id in available_ids:
            # found = False
            for fresh_range in fresh_ranges:
                if fresh_range.contains(id):
                    fresh_avail_count += 1
                    # found = True
                    # log_debug(f'Id {id} found in range {fresh_range.first_id}-{fresh_range.last_id}')
                    break
            # if not found:
                # log_debug(f'Id {id} was not found in any given range')

        return fresh_avail_count


    def part_2(self):
        return 0
    
Day5Solutions().run_solutions()