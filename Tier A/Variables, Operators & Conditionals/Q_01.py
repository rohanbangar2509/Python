# 1. Parse a string containing a number and safely determine whether it is an integer or decimal.

num = input("Enter Number: ")

def check_num_type(num):
    try:
        int(num)
        return f"{num} is Integer"
    except ValueError:
        try:
            float(num)
            return f"{num} is Decimal"
        except ValueError:
            return f"{num} is invalid"

print(check_num_type(num))