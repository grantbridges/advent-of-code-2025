from typing import List
from base_aoc_day_solutions import *

# https://adventofcode.com/2025/day/5

class IdRange():
    first_id: int
    last_id: int
    def __init__(self, first_id, last_id):
        self.first_id = first_id
        self.last_id = last_id

    def contains(self, id: int):
        return self.first_id <= id and self.last_id >= id
    
class Util():
    @staticmethod
    def read_id_ranges_from_file(input_file) -> List[IdRange]:
        ranges: List[IdRange] = []
        with open(input_file, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                if '-' in line:
                    ids = line.split('-')
                    ranges.append(IdRange(int(ids[0]), int(ids[1])))
        return ranges
    
    def read_available_ids_from_file(input_file) -> List[int]:
        ids: List[int] = []
        with open(input_file, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                if line != '' and '-' not in line:
                    ids.append(int(line))
        return ids

class Day5Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 5)

    def part_1(self):
        fresh_ranges: List[IdRange] = Util.read_id_ranges_from_file(self.input_file)
        available_ids = Util.read_available_ids_from_file(self.input_file)

        log_debug(f'Finished parsing {len(fresh_ranges)} ranges of fresh ingredients')

        fresh_avail_count = 0
        for id in available_ids:
            for fresh_range in fresh_ranges:
                if fresh_range.contains(id):
                    fresh_avail_count += 1
                    break

        return fresh_avail_count

    def part_2(self):
        return 0
    
Day5Solutions().run_solutions()