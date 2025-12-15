from base_aoc_day_solutions import *

# https://adventofcode.com/2025/day/4

class Grid():
    def __init__(self):
        self.rows = []
    
    def init_from_input_file(self, input_file):
        self.rows = []
        with open(input_file, 'r') as f:
            for row in f.readlines():
                row_data = []
                for entry in row:
                    row_data.append(entry)
                self.rows.append(row_data)
            
    def row_length(self, y):
        return len(self.rows[y])

    def col_height(self):
        return len(self.rows)
    
    def get_top_left(self, x, y):
        if x > 0 and y > 0:
            return self.rows[y-1][x-1]
        return None

    def get_top(self, x, y):
        if y > 0:
            return self.rows[y-1][x]
        return None
    
    def get_top_right(self, x, y):
        if x < self.row_length(y) - 2 and y > 0:
            return self.rows[y-1][x+1]
        return None
    
    def get_left(self, x, y):
        if x > 0:
            return self.rows[y][x-1]
        return None
    
    def get_right(self, x, y):
        if x < self.row_length(y) - 2:
            return self.rows[y][x+1]
        return None
    
    def get_bottom_left(self, x, y):
        if x > 0 and y < self.col_height() - 2:
            return self.rows[y+1][x-1]
        return None

    def get_bottom(self, x, y):
        if y < self.col_height() - 2:
            return self.rows[y+1][x]
        return None
    
    def get_bottom_right(self, x, y):
        if x < self.row_length(y) - 2 and y < self.col_height() - 2:
            return self.rows[y+1][x+1]
        return None

class Day4Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 4)

    def part_1(self):
        grid = Grid()
        grid.init_from_input_file(self.input_file)

        rolls_count = 0
        for y in range(0, len(grid.rows)):
            for x in range(0, len(grid.rows[y])):
                if grid.rows[y][x] == '@':
                    adj = [
                        grid.get_top_left(x, y),
                        grid.get_top(x, y),
                        grid.get_top_right(x, y),
                        grid.get_left(x, y),
                        grid.get_right(x, y),
                        grid.get_bottom_left(x, y),
                        grid.get_bottom(x, y),
                        grid.get_bottom_right(x, y),
                    ]

                    if adj.count('@') < 4:
                        rolls_count += 1

        return rolls_count

    def part_2(self):
        return 0
    
Day4Solutions().run_solutions()