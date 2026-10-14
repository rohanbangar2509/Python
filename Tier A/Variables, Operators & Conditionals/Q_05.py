# Write a function that safely converts a value to int and returns a default for invalid input.

# ====================================
# input
# ====================================
n = input("Enter n: ")


# ====================================
# Function : Try to convert n to int
# ====================================
def convert_value_int(n,default = 0):
    try:
        n = int(n)
    except ValueError:
        return default

    return n


# ====================================
# Call function (convert_value_int())
# ====================================
print(convert_value_int(n))