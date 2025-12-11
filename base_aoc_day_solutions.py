from abc import *
from utils import utils
from log import *
import time

class BaseAoCDaySolutions:
    def __init__(self, day_number):
        self.day_number = day_number

        self.input_file = f'inputs/day_{self.day_number}.txt'

    def part_1(self):
        return -1
    
    def part_2(self):
        return -1
    
    def run_solution(self, part_method):
        start_time = time.perf_counter()
        solution = part_method()
        end_time = time.perf_counter()
        elapsed_time_ms = (end_time - start_time) * 1000
    
        return (solution, elapsed_time_ms)
    
    def log_solution_output(self, part_number, solution, elapsed_time):
        log_info(f"-- Day {self.day_number} Pt {part_number}: {solution} ({elapsed_time:.3f}ms)")
    
    def run_solution_part(self, part_number):
        part_method = None
        if part_number == 1:
            part_method = self.part_1
        elif part_number == 2:
            part_method = self.part_2
        
        if part_method is not None:
            (solution, elapsed_time) = self.run_solution(part_method)
            self.log_solution_output(part_number, solution, elapsed_time)
        else:
            log_error(f"Unknown solution part number: {part_number}")
    
    def run_solutions(self):
        self.run_solution_part(1)
        self.run_solution_part(2)
    
    