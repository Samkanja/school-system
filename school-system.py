from typing import List
from dataclasses import dataclass,field


@dataclass
class Address:
    country:str
    county:str
    city:str
    street_address:str
    postal_code:str


@dataclass
class Person:
    first_name:str
    last_name:str
    phone_number: int
    age: int
    address: List[Address] = field(default_factory=list)


@dataclass
class Professor:
    person : Person
    


address = Address('Kenya','Nairobi','Nairobi','8485874','9838948')
address1 = Address('Kenya','Mombasa','Mombasa','Nyali','88485948')
p = Person('kanja','samuel',487848,30,[address,address1])
print(p)