import string
import random

class GenerationData:
    @staticmethod
    def generate_password():
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(6))
        return password

    @staticmethod
    def generate_email():
        return ''.join(random.choice(string.ascii_letters) for _ in range(3))
        email = (random_char(3) + "@gmail.com")
        return email

    @staticmethod
    def generate_name():
        characters = string.ascii_letters + string.digits + string.punctuation
        name = ''.join(random.choice(characters) for _ in range(3))
        return name
