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

                #joltage_value = self.get_bank_joltage_v0(bank)
                joltage_value = self.get_bank_joltage_v3(bank, 2)
                # log_debug(f'{line_count}: {joltage_value}')
                joltages.append(joltage_value)
        return sum(joltages)
    
    def get_bank_joltage_v0(self, bank):
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
        
        return int(f'{bank[largest_val_1_index]}{bank[largest_val_2_index]}')
    
    def get_bank_joltage_v1(self, bank, battery_count):
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
    
    def get_bank_joltage_v2(self, bank, target):
        out = []
        for b in bank[::-1]: # reverse iterate
            curr = int(b)

            if len(out) < target:
                out.insert(0, curr) # prepend
            else:
                if curr >= out[0]:
                    out.insert(0, curr) # prepend
                    out.pop() # remove last


        return int(''.join(map(str, out))) # merge output array into a single number
    
    def get_bank_joltage_v3(self, bank, target):
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


    def part_2(self):
        joltages = []
        battery_count = 12
        with open(self.input_file, 'r') as f:
            line_count = 0
            for bank in f.readlines():
                bank = bank.strip()
                line_count += 1

                #joltage_value = self.get_bank_joltage_v0(bank)
                joltage_value = self.get_bank_joltage_v3(bank, 12)
                # log_debug(f'{line_count}: {joltage_value}')
                joltages.append(joltage_value)

        return sum(joltages)
    
Day3Solutions().run_solutions()