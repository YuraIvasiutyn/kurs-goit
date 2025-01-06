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
print(get_days_from_today("2024"))
print(get_days_from_today("2024.11.12"))


def get_numbers_ticket(min: int, max: int, qualtity: int) -> List[int]:
    if min < 0 or max > 1_000:
        raise ValueError("Числа не можуть бути менші від 0 і більші за 1.000")
    
    if qualtity > max or qualtity < min:
        raise ValueError("Кількість чисел повинна бути в заданому діапазоні {min}-{max}")

    elements = [i for i in range(min, max+1)]

    result = sample(elements, k=qualtity)
    result.sort() # без створення нового об'єкту

    return result


print(get_numbers_ticket(1, 10, 9))


def normalize_phone(phone_number: str) -> str:

    new_obj = phone_number.strip()

    pattern = "-().?! "
    trantab = str.maketrans('', '', pattern)
    format_number = new_obj.translate(trantab)

    if format_number.startswith("+38"):
        format_number = format_number[3:]
    elif format_number.startswith("38"):
        format_number = format_number[2:]
    
    if not format_number.isdigit():
        raise ValueError(f"Формат номеру складається не тільки з цифр")

    return "+38" + format_number
    



print(normalize_phone("    +38(050)123-32-34"))
print(normalize_phone("     0503451234"))
print(normalize_phone("(050)8889900"))
print(normalize_phone("38050-111-22-22"))
print(normalize_phone("38050 111 22 11   "))

