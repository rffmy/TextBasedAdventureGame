def calculate(amount, interest_rate, time):
    # your code here

    interest = (amount * interest_rate * time) / 100
    total_amount = amount + interest

    return interest, total_amount

def print_result(interest, total_amount):
    # your code here
    print("The interest is: %.1f" % interest)
    print("The total amount is: %.1f" % total_amount)