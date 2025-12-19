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
    
    def overlaps(self, other: IdRange) -> bool:
        return not (self.last_id < other.first_id or self.first_id > other.last_id)
    
    def merge(self, other: IdRange) -> IdRange:
        # (only call this if you've already checked that they overlap)
        self.first_id = min(self.first_id, other.first_id)
        self.last_id = max(self.last_id, other.last_id)
    
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
    
    @staticmethod
    def read_available_ids_from_file(input_file) -> List[int]:
        ids: List[int] = []
        with open(input_file, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                if line != '' and '-' not in line:
                    ids.append(int(line))
        return ids

    # Returns a copy of the provided list of IdRanges that's been sorted
    # and all overlapping ranges have been merged together
    @staticmethod
    def merge_ranges(ranges: List[IdRange]):
        # sort ranges on first id
        ranges = sorted(ranges, key=lambda r: r.first_id)

        pos = 0
        a = ranges[pos]
        b = ranges[pos+1]

        while True:
            while a.overlaps(b):
                a.merge(b)
                ranges.remove(b) # delete b after merging into a

                if pos + 1 < len(ranges):
                    # grab new next entry to check against a again
                    b = ranges[pos+1]
                else:
                    break # at end of comparisons
            
            if pos + 2 < len(ranges):
                pos += 1
                a = ranges[pos]
                b = ranges[pos+1]
            else:
                break # nothing left to compare

        return ranges


class Day5Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 5)

    def part_1(self):
        fresh_ranges: List[IdRange] = Util.read_id_ranges_from_file(self.input_file)
        available_ids = Util.read_available_ids_from_file(self.input_file)

        fresh_avail_count = 0
        for id in available_ids:
            for fresh_range in fresh_ranges:
                if fresh_range.contains(id):
                    fresh_avail_count += 1
                    break

        return fresh_avail_count

    def part_2(self):
        ranges: List[IdRange] = Util.read_id_ranges_from_file(self.input_file)

        ranges = Util.merge_ranges(ranges)

        total_ids = 0
        for r in ranges:
            first_id = r.first_id
            last_id = r.last_id
            num_ids = last_id - first_id + 1 # inclusive
            total_ids += num_ids

        return total_ids
    
Day5Solutions().run_solutions()