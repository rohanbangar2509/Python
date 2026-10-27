# Validate that a numeric field falls within an inclusive range.

# Your task is to write a Python function that checks whether a numeric value falls between a minimum and maximum limit, including both boundaries.

# For example, suppose a Data Engineering pipeline validates an age field and accepts values from 18 to 60, inclusive.

def validate_range(value,minimum,maximum):

    if not isinstance(value,(int,float)) or isinstance(value,bool):
        raise TypeError("Value must be integer or float")

    if not minimum <= maximum:
        return "Invalid boundaries"

    if minimum <= value <= maximum:
        return True
    return False

try:
    print(validate_range(18,18,60))
    print(validate_range(60,18,60))
    print(validate_range('77',18,60))
except TypeError as error:
    print(f"Error : {error}")