# Classify a transaction as valid, refunded, cancelled, or invalid using multiple conditions.

# Transaction Record Contains
# transaction ID, amount, and status

# Use these validation rules:
# - transaction_id: positive integer
# - amount: positive number
# - status: a non-empty string matching one of the accepted statuses: completed, refunded, cancelled

# ======================================
# User Input
# ======================================

while True:
    try:
        transaction_id = int(input("Enter transaction_id : "))
        break
    except ValueError as error:
        print(f"Invalid Error, {error}")

while True:
    try:
        amount = float(input("Enter amount : "))
        break
    except ValueError as error:
        print(f"Invalid Error, {error}")
    
status = input("Enter status : ")

# ======================================
# Creating Dictionary
# ======================================

transaction_record = {
    'transaction_id' : transaction_id,
    'amount' : amount,
    'status' : status
}

# ======================================
# Validation Record
# ======================================

def validate_record(transaction_record):
    if not isinstance(transaction_record['transaction_id'],int):
        return 'invalid'

    if transaction_record['transaction_id'] > 0 and transaction_record['amount'] > 0 and ((transaction_record['status']).strip()).lower() in ['completed','refunded','cancelled']:

        if ((transaction_record['status']).strip()).lower() == 'completed':
            return 'valid'
        elif ((transaction_record['status']).strip()).lower() == 'refunded':
            return 'refunded'
        elif ((transaction_record['status']).strip()).lower() == 'cancelled':
            return 'cancelled'
        else:
            return 'invalid'

    return 'invalid'

# ======================================
# Call Function 
# ======================================

print(validate_record(transaction_record))