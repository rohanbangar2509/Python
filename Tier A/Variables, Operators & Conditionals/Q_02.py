# Validate a record only when required fields are present and values satisfy basic rules.

# | Field   | Rule                       |
# | ------- | -------------------------- |
# | `id`    | Must be a positive integer |
# | `name`  | Must be a non-empty string |
# | `age`   | Must be between 18 and 100 |
# | `email` | Must contain `@`           |

import string

record_1 = {
    "id" : 101,
    "name" : "  Rohan",
    "age" : 21,
    "email" : "rohan123@gmail.com"
}

record_2 = {
    "id" : 101,
    "name" : "  Rohan",
    "age" : 21,
    "email" : "rohan123gmail.com"
}

record_3 = {
    "id" : 101,
    "name" : "   ",
    "age" : 21,
    "email" : "rohan123@gmail.com"
}

def validate_record(record):
    # checking all fields are present
    required_fields = ["id","name","age","email"]
    field_check = all (field in record for field in required_fields)

    # checking values
    value_check = (
        isinstance(record['id'],int) and record['id'] > 0 and 
        isinstance(record['name'],str) and len(record['name'].strip()) > 0 and 
        isinstance(record['age'],int) and record['age'] >= 18 and record['age'] <= 100 and isinstance(record['email'],str) and '@' in record['email']
    )

    return field_check and value_check


if validate_record(record_1):
    print("Valid record (record_1)")
else:
    print("Invalid record (record_1)")

if validate_record(record_2):
    print("Valid record (record_2)")
else:
    print("Invalid record (record_2)")

if validate_record(record_3):
    print("Valid record (record_3)")
else:
    print("Invalid record (record_3)")