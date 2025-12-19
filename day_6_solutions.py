from typing import List
import math
from base_aoc_day_solutions import *

# https://adventofcode.com/2025/day/6

class MathProblem():
    digits: List[int]
    sign: str # + or *

    def __init__(self, digits, sign):
        self.digits = digits
        self.sign = sign

    def solve(self):
        if self.sign == '+':
            return sum(self.digits)
        elif self.sign == '*':
            return math.prod(self.digits)

class SignToken():
    sign: str
    start_index: int
    width: int

    def __init__(self):
        self.sign = ''
        self.start_index = -1
        self.width = 1
        
class Util():
    @staticmethod
    def read_problems_from_file_pt_1(input_file) -> List[MathProblem]:
        problems: List[MathProblem] = []
        with open (input_file, 'r') as f:
            lines = f.readlines()

            rows = []
            for i in range(0, len(lines)):
                rows.append(lines[i].split())

            sign_row_index = len(lines) - 1

            problems_count = len(rows[0]) # all rows are same length

            for i in range(0, problems_count):
                value_rows = rows[:sign_row_index]
                digits = []
                for v in value_rows:
                    digits.append(int(v[i]))
                sign = rows[sign_row_index][i]
                
                problems.append(MathProblem(digits, sign))
        return problems
    
    def read_problems_from_file_pt_2(input_file) -> List[MathProblem]:
        problems: List[MathProblem] = []
        with open (input_file, 'r') as f:
            lines = f.readlines()

            sign_row_index = len(lines) - 1
            digits_count = len(lines) - 1

            # 1) Tokenize the last row to get each sign and the problem width
            sign_tokens: List[SignToken] = []
            temp_token = SignToken()
            sign_row = lines[sign_row_index]
            i = 0
            while i < len(sign_row):
                c = sign_row[i]
                if c in ['*', '+']:
                    if temp_token.sign == '':
                        # store sign for current token
                        temp_token.sign = c
                        temp_token.start_index = i
                    else:
                        # we've hit the next sign - this is the end of our problem section
                        # remove one from the width to account for padding to next section
                        temp_token.width -= 1
                        sign_tokens.append(temp_token)
                        # start a new temp_token
                        temp_token = SignToken()
                        # decrement index so we can capture this sign
                        i -= 1
                else:
                    # whitespace - iterate width
                    temp_token.width += 1
                
                i += 1
            
            # store the last temp_token we were building
            sign_tokens.append(temp_token)

            # 2) Build problems by iterating over sign tokens
            for token in sign_tokens:
                digits = []
                for x in range(0, token.width):
                    temp_digit = ''
                    for i in range(0, digits_count):
                        temp_digit += lines[i][token.start_index + x]
                    digits.append(int(temp_digit))

                problems.append(MathProblem(digits, token.sign))
        
        return problems

class Day6Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 6)

    def part_1(self):
        problems = Util.read_problems_from_file_pt_1(self.input_file)

        total = 0
        for p in problems:
            total += p.solve()

        return total

    def part_2(self):
        problems = Util.read_problems_from_file_pt_2(self.input_file)

        total = 0
        for p in problems:
            total += p.solve()

        return total
    
Day6Solutions().run_solutions()