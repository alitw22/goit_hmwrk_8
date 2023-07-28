from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # current date and date for the next week
    today = datetime.now().date()
    next_week = today + timedelta(days=7)

    
    days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday"}
    weekdays = {day: [] for day in days}

    # Go through users and put them regarding their birthdays 
    for user in users:
        name = user['name']
        birthday = user['birthday'].date()
        diff = (birthday - today).days

        if 0 <= diff < 7:
            index = (today.weekday() + diff) % 7
            if index == 5 or index == 6:
                # If the birthday on current Saturday or Sunday, move it to next Monday
                index = 0
            weekdays[index].append(name)
        elif 0 <= (birthday - next_week).days < 7:
            index = (next_week.weekday() + (birthday - next_week).days) % 7
            weekdays[index].append(name)

    # Final list of users regarding their birthdays
    for day in days:
        if weekdays[day]:
            print(f"{days[day]}: {', '.join(weekdays[day])}")


users = [
         {"name": "Maria, Ivan, Oleg", "birthday": datetime(2023, 7, 29)},  # Saturday
         {"name": "Olga, Oscar, Nina", "birthday": datetime(2023, 7, 30)},  # Sunday
         {"name": "Georgiy", "birthday": datetime(2023, 7, 31)},  # Monday
         {"name": "Peter, Hanna", "birthday": datetime(2023, 8, 1)},    # Tuesday
         {"name": "Elena", "birthday": datetime(2023, 8, 2)},  # Wednesday
         {"name": "Volodimir, Oksana", "birthday": datetime(2023, 8, 3)},  # Thursday
         {"name": "Hugo, Valeria, Lidia", "birthday": datetime(2023, 8, 4)},   # Friday    
        ]


get_birthdays_per_week(users)
