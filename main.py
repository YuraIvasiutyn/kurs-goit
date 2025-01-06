import re

from datetime import datetime
from random import sample
from typing import List



def get_days_from_today(date: str) -> int:

    try:
        date_now = datetime.now().date()
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError as e:
        print("Status Code 400: Передано неправилильний формат дати. Формат повинен бути YYYY-MM-DD")
        print(f"devMsg (внутрішній комунікат): {e}")
        return None

    timedelta_obj = date_now - date_obj
    return timedelta_obj.days

print(get_days_from_today("2025-12-31"))
print(get_days_from_today("2024-11-12"))


def get_numbers_ticket(min: int, max: int, quantity: int) -> List[int]:
    if min < 0 or max > 1_000:
        return []
    
    if quantity < 1 or quantity > (max - min + 1):
        return []

    elements = [i for i in range(min, max+1)]

    result = sample(elements, k=quantity)
    result.sort() # без створення нового об'єкту

    return result


print(get_numbers_ticket(5, 10, 2))


def normalize_phone(phone_number: str) -> str:

    new_obj = phone_number.strip()

    pattern = "-().?! \\t\\n"
    trantab = str.maketrans('', '', pattern)
    format_number = new_obj.translate(trantab)

    if format_number.startswith("+38"):
        format_number = format_number[3:]
    elif format_number.startswith("38"):
        format_number = format_number[2:]
    
    if not format_number.isdigit():
        print(f"Формат номеру складається не тільки з цифр {format_number}")

    return "+38" + format_number
    


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
