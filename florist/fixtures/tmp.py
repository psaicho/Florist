class Person():
    def __init__(self, id: int, FirstName: str, lastName: str, age: int):
        self.id = id
        self.firstName = FirstName
        self.lastName = lastName
        self.age = age

personDict = [
    {"id": 1, "firstName": "Jan", "lastname": "Nowak", "age": 32},
    {"id": 2, "firstName": "Paweł", "lastname": "Kowalski", "age": 12},
    {"id": 3, "firstName": "Kajetan", "lastname": "Iksiński", "age": 34},
    {"id": 4, "firstName": "Kacper", "lastname": "Ruta", "age": 67}
]

Guests = {}
for person in personDict:
    guest_name = f"Guest_{person['id']}"
    Guests[guest_name] = Person(
        person["id"],
        person["firstName"],
        person["lastname"],
        person["age"]
    )


for guest_name, guest in Guests.items():
    print(f"Nazwa obiektu: {guest_name}")
    print(f"id: {guest.id}")
    print(f"First Name: {guest.firstName}")
    print(f"Last Name: {guest.lastName}")
    print(f"Age: {guest.age}")
    print()
