from base_aoc_day_solutions import *
import textwrap

# https://adventofcode.com/2025/day/2

class ProductRange():
    start: int
    end: int

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def get_invalid_ids_part_1(self):
        invalid_ids = []
        for id in range(self.start, self.end + 1):
            # Check for repeating pattern
            id_str = str(id)
            id_length = len(id_str)
            if id_length % 2 == 0:
                midpoint = int(id_length / 2)
                left = id_str[:midpoint]
                right = id_str[midpoint:]

                if left == right:
                    invalid_ids.append(id)
        return invalid_ids
    
    def get_invalid_ids_part_2(self):
        invalid_ids = []
        for id in range(self.start, self.end + 1):
            id_str = str(id)
            id_length = len(id_str)
            
            # get each number that the total length is evenly divisible by
            lens_to_check = []
            for i in range(1, id_length // 2 + 1):
                if id_length % i == 0:
                    lens_to_check.append(i)
            
            # for each of these lengths, divide up the string
            for length in lens_to_check:
                splits = textwrap.wrap(id_str, length)

                # now we've divided up the string into equal parts
                # see if all these parts equal the first in this split
                all_match = all(x == splits[0] for x in splits)
                if all_match:
                    #log_debug(f'Invalid Id: {id}')
                    invalid_ids.append(id)
                    # we found a match so no need to check the other lengths
                    break 

        return invalid_ids
    
    @staticmethod
    def from_string(value):
        vals = value.split('-')
        return ProductRange(int(vals[0]), int(vals[1]))

class Day2Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 2)

    def part_1(self):
        with open(self.input_file, 'r') as f:
            data = f.readline()
            
            invalid_ids = []
            for range_string in data.split(','):
                range = ProductRange.from_string(range_string)

                invalid_ids.extend(range.get_invalid_ids_part_1())

        return sum(invalid_ids)

    def part_2(self):
        with open(self.input_file, 'r') as f:
            data = f.readline()
            
            invalid_ids = []
            for range_string in data.split(','):
                range = ProductRange.from_string(range_string)

                invalid_ids.extend(range.get_invalid_ids_part_2())

        return sum(invalid_ids)

    
Day2Solutions().run_solutions()