"""Verifies user input."""

import re


def __re_date(a):
    date = re.compile(r"""(\d?\d) # month
                      [-/] # separator (- or /)
                      (\d?\d) # day
                      [-/] # separator (- or /)
                      (\d\d\d\d)""", # year
                      re.VERBOSE)
    match = date.search(a)
    return match


def input_date(prompt: str, err=""):
    """Get user input and make sure that it is a date.
        prompt - question to display to user
        err - optional, what to display if the input is invalid"""
    
    while True:
        answer = input(prompt)
        match = __re_date(answer)

        if match:
            month = match[1]
            day = match[2]
            year = match[3]
            return month, day, year
        
        print(err)