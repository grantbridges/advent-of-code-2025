from base_aoc_day_solutions import *

# https://adventofcode.com/2025/day/3

class Day3Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 3)

    def part_1(self):
        joltages = []
        with open(self.input_file, 'r') as f:
            line_count = 0
            for bank in f.readlines():
                bank = bank.strip()
                line_count += 1
                # track index of two biggest values
                largest_val_1_index = -1
                largest_val_2_index = -1

                # first pass to look for biggest number
                temp_biggest_val = -1
                for index in range(0, len(bank) - 1): # exclude last value from check
                    current = int(bank[index])
                    if current > temp_biggest_val:
                        temp_biggest_val = current
                        largest_val_1_index = index
                    
                # second pass to look for next biggest number
                temp_biggest_val = -1
                for index in range(largest_val_1_index + 1, len(bank)):
                    current = int(bank[index])
                    if current > temp_biggest_val:
                        temp_biggest_val = current
                        largest_val_2_index = index
                
                joltage_value = int(f'{bank[largest_val_1_index]}{bank[largest_val_2_index]}')
                joltages.append(joltage_value)
        return sum(joltages)
    
    def get_bank_joltage(self, bank, battery_count):
        out = []
        for b in bank:
            curr = int(b)
            if len(out) < battery_count:
                # simply add this value in
                out.append(curr)
            else:
                check_index = len(out) - 1
                check_value = out[check_index]
                while curr > check_value:
                    out[check_index] = curr
                    curr = check_value
                    check_index -= 1
                    if check_index >= 0:
                        check_value = out[check_index]
                    else:
                        break # passed start of our value - move on

        return int(''.join(map(str, out))) # merge output array into a single number


    def part_2(self):
        joltages = []
        battery_count = 12
        with open(self.input_file, 'r') as f:
            line_count = 0
            for bank in f.readlines():
                bank = bank.strip()
                line_count += 1

                joltage = self.get_bank_joltage(bank, battery_count)
                log_debug(f'Line {line_count}: {bank}')
                log_debug(f'\tValue: {joltage}')
                joltages.append(joltage)

        return sum(joltages)
    
Day3Solutions().run_solutions()