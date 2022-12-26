from typing import *
from dataclasses import dataclass

@dataclass
class Person:
    name:str
    phone_number: int
    address: str
    age: int

@dataclass(_cls)
class Professor:
    person : Person
    



p = Person('kanja',487848,'kimathi street',30)
print(p)