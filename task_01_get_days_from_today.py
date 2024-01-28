from datetime import datetime
def get_days_from_today(date):
    try:
        entered_date = datetime.strptime(date, "%Y-%m-%d")

    except Exception:
        return 'You entered wrong date'

    current_day = datetime.today()
    days_difference = current_day - entered_date
    return days_difference.days



print(get_days_from_today("2023-12-31"))
print(get_days_from_today("2024-01-01"))
print(get_days_from_today("2024-01-31"))
print(get_days_from_today("2024-01-42"))
print(get_days_from_today("2024-15-31"))
print(get_days_from_today("2024.01.01"))
print(get_days_from_today("hlk"))