"""Rung 3: Guided implement.

Topic: a small base class + super()

Define a base class `Animal`:
- `__init__(self, name: str)` stores `self.name`.
- A method `speak(self) -> str` that returns "(generic noise)".

Then define a subclass `Dog(Animal)`:
- Override `speak` to return f"{self.name} says woof".
- Override `__init__` to accept (name, breed). Call super().__init__(name)
  to reuse the parent's init, then set self.breed = breed.
"""


class Animal:
    def __init__(self, name: str) -> None:
        # TODO: store name
        raise NotImplementedError

    def speak(self) -> str:
        # TODO: return "(generic noise)"
        raise NotImplementedError


class Dog(Animal):
    def __init__(self, name: str, breed: str) -> None:
        # TODO: call super().__init__(name) and store breed
        raise NotImplementedError

    def speak(self) -> str:
        # TODO: return f"{self.name} says woof"
        raise NotImplementedError
