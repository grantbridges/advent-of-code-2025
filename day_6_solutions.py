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
        
class Util():
    @staticmethod
    def read_problems_from_file(input_file) -> List[MathProblem]:
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

class Day6Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 6)

    def part_1(self):
        problems = Util.read_problems_from_file(self.input_file)

        total = 0
        for p in problems:
            total += p.solve()

        return total

    def part_2(self):
        return 0
    
Day6Solutions().run_solutions()