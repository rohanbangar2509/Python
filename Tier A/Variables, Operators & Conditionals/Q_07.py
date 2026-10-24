# Calculate percentage change while safely handling a zero previous value

# Explaination 

# In Data Engineering and analytics, you often compare metrics across two time periods, such as daily sales, pipeline record counts, or monthly revenue.

# Your task is to write a function that calculates the percentage change from a previous value to a new value, while safely handling cases where the previous value is zero.


def calculate_percentage_change(privious_value,new_value):
    try:
        result = (new_value - privious_value) * 100 / privious_value 
        return result
    except ZeroDivisionError:
        return None


print(calculate_percentage_change(100,150))
print(calculate_percentage_change(0,150))