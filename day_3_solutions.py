from base_aoc_day_solutions import *

# https://adventofcode.com/2025/day/3

class Day3Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 3)

    def get_bank_joltage(self, bank, target):
        out = [-1] * target # tracks indices of each number we want to keep

        full_number = ''
        for out_index in range(0, len(out)):
            temp_biggest_val = -1
            start_pos = 0 if out_index == 0 else out[out_index - 1] + 1
            end_pos = len(bank) - target + out_index + 1
            
            for index in range(start_pos, end_pos):
                current = int(bank[index])
                if current > temp_biggest_val:
                    temp_biggest_val = current
                    out[out_index] = index

            full_number += str(bank[out[out_index]])
        
        return int(full_number)

    def part_1(self):
        joltages = []
        with open(self.input_file, 'r') as f:
            for bank in f:
                bank = bank.strip()
                joltage_value = self.get_bank_joltage(bank, 2)
                joltages.append(joltage_value)
                
        return sum(joltages)

    def part_2(self):
        joltages = []
        with open(self.input_file, 'r') as f:
            for bank in f:
                bank = bank.strip()
                joltage_value = self.get_bank_joltage(bank, 12)
                joltages.append(joltage_value)

        return sum(joltages)
    
Day3Solutions().run_solutions()