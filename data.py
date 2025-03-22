import random

def generate_email (number, domain):
    name = "viktoriya"
    surname = "merkylova"
    random_digits = random.randint(100, 999)
    email = f"{surname}_{name}_{number}_{random_digits}@{domain.lower()}"
    return email

