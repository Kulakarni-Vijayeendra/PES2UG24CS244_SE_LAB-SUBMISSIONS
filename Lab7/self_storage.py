
import math


def parse_rental(text):
    try:
        if not isinstance(text, str):
            return "Unknown", 0.0

        if text.count(':') != 1:
            return "Unknown", 0.0

        unit, months = text.split(':')
        unit = unit.strip()

        if not unit:
            return "Unknown", 0.0

        months = float(months.strip())

        if not math.isfinite(months) or months < 0:
            return "Unknown", 0.0

        return unit.title(), months

    except (ValueError, TypeError, OverflowError):
        return "Unknown", 0.0


def duration_average(months_csv):
    try:
        if not isinstance(months_csv, str) or not months_csv.strip():
            return 0

        values = [int(r.strip()) for r in months_csv.split(',')]

        if not values or any(value < 0 for value in values):
            return 0

        return sum(values) // len(values)

    except (ValueError, TypeError, OverflowError):
        return 0


def payable_rent(text):
    try:
        if not isinstance(text, str) or text.count('|') != 1:
            return 0.0

        rent, discount = text.split('|')

        rent = float(rent.strip())
        discount = float(discount.strip())

        if not math.isfinite(rent) or not math.isfinite(discount):
            return 0.0

        if rent < 0 or discount < 0:
            return 0.0

        total = rent * 1.18 - discount

        if not math.isfinite(total):
            return 0.0

        return max(total, 0.0)

    except (ValueError, TypeError, OverflowError):
        return 0.0


def main():
    print("==== Running parse_rental ====")
    user_input = input("Enter unit:months (e.g. medium:6): ")
    result = parse_rental(user_input)
    print("Unit and Months:", result)

    print("\n==== Running duration_average ====")
    user_input = input("Enter rental months as CSV (e.g. 3,6,12): ")
    result = duration_average(user_input)
    print("Average Duration:", result)

    print("\n==== Running payable_rent ====")
    user_input = input("Enter rent|discount (e.g. 2400|200): ")
    result = payable_rent(user_input)
    print("Payable Rent:", result)


if __name__ == "__main__":
    main()
