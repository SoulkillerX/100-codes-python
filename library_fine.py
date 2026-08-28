def calculate_fine(days_late):
    if days_late <= 0:
        return "No fine. Book returned on time."
    elif days_late > 30:
        return "Membership Cancelled."
    elif days_late <= 5:
        fine = days_late * 2
    elif days_late <= 10:
        fine = (5 * 2) + (days_late - 5) * 4
    else:
        fine = (5 * 2) + (5 * 4) + (days_late - 10) * 6
    return f"Total Fine: ₹{fine}"

if __name__ == "__main__":
    days = int(input("Enter number of days late: "))
    result = calculate_fine(days)
    print(result)