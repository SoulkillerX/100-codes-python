def calculate_electricity_bill(units):
    if units <= 0:
        return "No bill. No electricity consumed."
    elif units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + (units - 100) * 7
    else:
        bill = (100 * 5) + (100 * 7) + (units - 200) * 10
    return f"Total Electricity Bill: ₹{bill}"  