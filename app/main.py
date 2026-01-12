class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people.clear()
    created_list = [Person(person.get("name"),
                           person.get("age"))
                    for person in people]

    i = 0
    for person in people:
        if person.get("husband"):
            created_list[i].husband = Person.people[person.get("husband")]

        elif person.get("wife"):
            created_list[i].wife = Person.people[person.get("wife")]

        i += 1
    return created_list
