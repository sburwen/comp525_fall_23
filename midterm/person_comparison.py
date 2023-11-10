"""
Create a Python class Person with attributes for a person's name and age. 
Implement a method to compare the ages of two people, returning a message that 
indicates who is older. For example, if person1 is 30 years old and person2 is 
25 years old, calling person1.compare_age(person2) should return 
"person1 is older."

- Use appropriate function docstrings. 
- Include the time complexity of your function in your docstring.
- No need for design documents, unit tests, etc. Just the function and a call
to the function.

File: midterm/person_comparison.py
Contributor: Sean Burwen
Date: 11/9/2023
"""


class Person:
    """
    Class representation of a person
    """

    def __init__(self, name, age):
        """
        Constructor,
        Complexity O(1)

        :param name: string, name of person
        :param age: integer, age of person
        """
        self.name = name
        self.age = age

    def compare_age(self, other_person):
        """
        Compares age of self and another person object,
        Complexity O(1)

        :param other_person: Person object
        :return: string, representing comparison outcome
        """
        if self.age > other_person.age:
            return self.name + " is older."
        elif self.age < other_person.age:
            return other_person.name + " is older."
        else:
            return self.name + " and " + other_person.name + " are the same age."


person1 = Person("Sean", 21)
person2 = Person("Dan", 34)
person3 = Person("Jen", 34)
print(person1.compare_age(person2))
print(person2.compare_age(person3))
