import sys

# A helper file to create a new day_#_solutions.py file from the stub
# Usage example (where 1 is the day number to create): py ./create_day_solution_file.py 1

YEAR = 2025
DAY = 1

# receive day # as input arg
if len(sys.argv) > 1:
    DAY = int(sys.argv[1])

with open('day_solutions_stub.py', 'r') as stub_file:
    stub_contents = stub_file.read()
    stub_contents = stub_contents.replace('9999', str(YEAR))
    stub_contents = stub_contents.replace('-1', str(DAY))
    stub_contents = stub_contents.replace('Stub', str(DAY))

    with open(f'day_{str(DAY)}_solutions.py', 'w+') as solutions_file:
        solutions_file.write(stub_contents)