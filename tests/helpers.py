import random

class Data:
    email = "zontovich_39@yandex.ru"
    password = "123456"

def generate_email():
    name = "zontovich"
    number = random.randint(1000, 9999)
    return f"{name}{number}@yandex.ru"

def generate_password():
    return str(random.randint(100000, 999999))


