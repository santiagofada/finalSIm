import string
import random

class Trabajo():

    def __init__(self,semana):
        self.__nombre = random.choice(string.ascii_letters.upper()) + str(random.randint(1, 100)) + random.choice(string.ascii_letters.upper())
        self.__semana = semana

    def __str__(self):
        return f"{self.__nombre}, {self.__semana}"

    def get_semana(self):
        return self.__semana
    def get_nombre(self):
        return self.__nombre
