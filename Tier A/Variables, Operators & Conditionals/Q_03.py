# Determine whether a date-like string has a valid YYYY-MM-DD structure.

import string

# input
date_string = input("Enter Date: ")

# Validate Date Format {YYYY-MM-DD}
def valid_date_structure(date_string):

    if "-" not in date_string:
        return False
    date_string = str.split(date_string,'-')

    if not len(date_string) == 3:
        return False

    if not (len(date_string[0]) == 4 and len(date_string[1]) == 2 and len(date_string[2]) == 2):
        return False

    if not all(d.isdigit() for d in date_string):
        return False

    
    # Range of Month (MM)
    if int(date_string[1]) <= 0 or int(date_string[1]) > 12:
        return False

    # Range of Day (DD)
    if int(date_string[2]) <= 0 or int(date_string[2]) > 31:
        return False
        
    return True

if valid_date_structure(date_string):
    print(f"Valid date structure {date_string}")
else:
    print(f"Invalid date structure {date_string}")