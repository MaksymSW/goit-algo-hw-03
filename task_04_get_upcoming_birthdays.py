
import datetime
from datetime import datetime, timedelta
def get_upcoming_birthdays(users):
    upcoming_birthdays=[]
    for user in users:

        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        today = datetime.today().date()
        birthday_this_year = datetime(today.year, birthday.month, birthday.day).date()
        print(birthday_this_year)

        diffrence = birthday_this_year - today

        if diffrence <= timedelta(days=6) and diffrence>= timedelta(days=0):
            if birthday_this_year.weekday() == 5:
                birthday_this_year = birthday_this_year + timedelta(days=2)
            if birthday_this_year.weekday() == 6:
                birthday_this_year = birthday_this_year + timedelta(days=1)

            congrat_date = birthday_this_year.strftime("%Y.%m.%d")

            to_congratulate = {"name": user["name"], "congratulation_date": congrat_date}
            upcoming_birthdays.append(to_congratulate.copy())

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.05.25"},
    {"name": "Roy Smith", "birthday": "1985.01.28"},
    {"name": "Jane Smith", "birthday": "1990.01.30"},
    {"name": "Shay Robertson", "birthday": "1985.05.01"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні: ", upcoming_birthdays)

