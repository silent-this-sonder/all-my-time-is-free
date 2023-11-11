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


def valid_input(prompt):
    """Get user input and make sure it is not empty.
        prompt - question to display to user."""
    
    while True:
        answer = input(prompt).strip()

        if answer == "": # empty string
            print("Please enter a non-empty string.")
        else:
            return answer
        

def input_date(prompt: str, err=""):
    """Get user input and make sure that it is a date.
        prompt - question to display to user
        err - optional, what to display if the input is invalid"""
    
    while True:
        answer = valid_input(prompt)
        match = __re_date(answer)

        if match:
            month = match[1]
            day = match[2]
            year = match[3]
            return month, day, year
        
        if err != "": # make sure there actually is an error message
            print(err)


def input_yn(prompt: str, err=""):
    """Get user input for a yes/no question.
        prompt - question to display to user
        err - optional, displays if the input is invalid."""
    
    while True:
        answer = valid_input(prompt).lower()

        if answer == "yes" or answer == "y":
            return "yes"
        elif answer == "no" or answer == "n":
            return "no"
        
        if err != "": # make sure there actually is an error message
            print(err)