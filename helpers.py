import random
import string

class AuthGenerator:
    def generate_email (self, domain):
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

    def generate_short_password(self):
        length = random.randint(4, 6)
        password_short = []
        password_short.append(random.choice(string.ascii_letters))
        password_short.append(random.choice(string.digits))

        characters = string.ascii_letters + string.digits
        password_short.extend(random.choice(characters) for _ in range(length - 2))

        random.shuffle(password_short)
        return ''.join(password_short)

