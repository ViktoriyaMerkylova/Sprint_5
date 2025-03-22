import random
import string

class AuthGenerator:
    def generate_email (self, number, domain):
        name = "viktoriya"
        surname = "merkylova"
        number = 17
        random_digits = random.randint(100, 999)
        email = f"{surname}_{name}_{number}_{random_digits}@{domain.lower()}"
        return email

    def generate_password(self, length=6):
        if length < 6:
            raise ValueError("Минимальная длина пароля - 6 символов")

        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special = string.punctuation

        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(special)
        ]

        all_chars = lowercase + uppercase + digits + special
        password += random.choices(all_chars, k=length - 4)

        random.shuffle(password)

        return ''.join(password)

