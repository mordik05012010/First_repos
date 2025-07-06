import datetime
from datetime import datetime

#1 завдання: 

def get_days_from_today(date: str) -> int:
    date_form = datetime.strptime(date, "%Y-%m-%d").date()
    date_today = datetime.today().date()
    delta = date_today - date_form
    return f"з цього дня пройшло: {delta.days} днів"

#print(get_days_from_today("2020-06-09"))

import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > (max - min +1):
        return []
    choices = random.sample(range(min, max + 1), quantity)
    return f"Відсортований список квитків: {sorted(choices)}"

#print(get_numbers_ticket(5, 20, 10))