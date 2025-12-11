import re

class utils:
    def __init__(self):
        pass

    @staticmethod
    def is_int(val):
        try:
            int(val)
            return True
        except:
            return False

    @staticmethod
    def first_int_in_list(numbers):
        for n in numbers:
            if utils.is_int(n):
                return n
        return None
    
    @staticmethod
    def last_int_in_list(numbers):
        for n in reversed(numbers):
            if utils.is_int(n):
                return n
        return None
    
    @staticmethod
    def find_all_substrings(original_string = "", substring = ""):
        # Finds all occurrences of a given substring in a given string
        # and returns a list of its indices
        indices = []
        i = original_string.find(substring)
        while i != -1:
            indices.append(i)
            i = original_string.find(substring, i+1)
        return indices
    
    @staticmethod
    def remove_multi_whitespace(original_string):
        # Replaces all multiple occurrences of whitespace with single
        # E.g. "Test    4   3   2 1 " becomes "Test 4 3 2 1"
        return re.sub(r'\s+', ' ', original_string)