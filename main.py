'''
The Elves have good news and bad news.

The good news is that they've discovered project management! This has given them the tools 
they need to prevent their usual Christmas emergency. For example, they now know that the 
North Pole decorations need to be finished soon so that other critical tasks can start on time.

The bad news is that they've realized they have a different emergency: according to their resource 
planning, none of them have any time left to decorate the North Pole!

To save Christmas, the Elves need you to finish decorating the North Pole by December 12th.

Collect stars by solving puzzles. Two puzzles will be made available on each day; 
the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
'''

import time

start_time = time.perf_counter()

# run all solutions - each day file automatically runs its own solutions,
# so simply importing them here will trigger running
from day_1_solutions import *
from day_2_solutions import *
from day_3_solutions import *
from day_4_solutions import *
from day_5_solutions import *
from day_6_solutions import *
from day_7_solutions import *
# add more solutions here as desired

end_time = time.perf_counter()
elapsed_time = (end_time - start_time) * 1000
log_info(f"-- Total Time: {elapsed_time:.3f}ms")