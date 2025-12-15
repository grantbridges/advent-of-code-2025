from base_aoc_day_solutions import *
import pyperclip

# https://adventofcode.com/2025/day/4

class Grid():
    def __init__(self):
        self.rows = []
    
    def init_from_input_file(self, input_file):
        self.rows = []
        with open(input_file, 'r') as f:
            for row in f.readlines():
                row = row.strip()
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
        if x <= self.row_length(y) - 2 and y > 0:
            return self.rows[y-1][x+1]
        return None
    
    def get_left(self, x, y):
        if x > 0:
            return self.rows[y][x-1]
        return None
    
    def get_right(self, x, y):
        if x <= self.row_length(y) - 2:
            return self.rows[y][x+1]
        return None
    
    def get_bottom_left(self, x, y):
        if x > 0 and y <= self.col_height() - 2:
            return self.rows[y+1][x-1]
        return None

    def get_bottom(self, x, y):
        if y <= self.col_height() - 2:
            return self.rows[y+1][x]
        return None
    
    def get_bottom_right(self, x, y):
        if x <= self.row_length(y) - 2 and y <= self.col_height() - 2:
            return self.rows[y+1][x+1]
        return None
    
    # For a given x/y point, get all adjacent values
    def get_all_adj(self, x, y):
        return [
            self.get_top_left(x, y),
            self.get_top(x, y),
            self.get_top_right(x, y),
            self.get_left(x, y),
            self.get_right(x, y),
            self.get_bottom_left(x, y),
            self.get_bottom(x, y),
            self.get_bottom_right(x, y),
        ]
    
    # For a given x/y, see if this entry can be safely removed
    # (Fewer than 4 rolls in adjacent spots)
    def can_be_removed(self, x, y):
        adj = self.get_all_adj(x, y)
        return adj.count('@') < 4
    
    # Manipulates self to remove all elgible rolls, then returns number removed
    def remove_all_eligible_rolls(self):
        removed_count = 0
        new_rows = []
        for y in range(0, len(self.rows)):
            new_row = []
            for x in range(0, len(self.rows[y])):
                curr = self.rows[y][x]
                if curr == '@':
                    if self.can_be_removed(x, y):
                        removed_count += 1
                        new_row.append('.')
                    else:
                        new_row.append(curr)
                else:
                    new_row.append(curr)
            new_rows.append(new_row)

        # replace old rows with new ones
        self.rows = new_rows
        log_debug(f'Removed {removed_count} rolls')
        return removed_count

class Day4Solutions(BaseAoCDaySolutions):
    def __init__(self):
        BaseAoCDaySolutions.__init__(self, 4)

    def part_1(self):
        grid = Grid()
        grid.init_from_input_file(self.input_file)

        rolls_count = 0
        adjusted_ouput = ""
        for y in range(0, len(grid.rows)):
            for x in range(0, len(grid.rows[y])):
                if grid.rows[y][x] == '@':
                    if grid.can_be_removed(x, y):
                        rolls_count += 1
                        adjusted_ouput += 'x'
                    else:
                        adjusted_ouput += '@'
                else:
                    adjusted_ouput += grid.rows[y][x]
            
            adjusted_ouput += '\n'

        pyperclip.copy(adjusted_ouput)
        print(adjusted_ouput)
        return rolls_count

    def part_2(self):
        grid = Grid()
        grid.init_from_input_file(self.input_file)

        remove_count = grid.remove_all_eligible_rolls()
        total_remove_count = remove_count
        while (remove_count > 0):
            remove_count = grid.remove_all_eligible_rolls()
            total_remove_count += remove_count
        
        return total_remove_count


    
Day4Solutions().run_solutions()