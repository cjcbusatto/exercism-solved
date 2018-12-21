import random
import string


class Robot(object):
    def __init__(self):
        self.name = self.generate_random_name()

    def generate_random_name(self):
        random.seed()
        prefix = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
        suffix = str(random.randint(100, 999))
        return prefix + suffix

    def reset(self):
        self.name = self.generate_random_name()
