"""Rung 3: Guided — solved version.

`Dog.__init__` calls `super().__init__(name)` to let the parent handle
the attribute it owns (`self.name`), then adds its own attribute
(`self.breed`). Overriding `speak` returns the dog-specific string,
using the `name` attribute set by the parent.
"""


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return "(generic noise)"


class Dog(Animal):
    def __init__(self, name: str, breed: str) -> None:
        super().__init__(name)
        self.breed = breed

    def speak(self) -> str:
        return f"{self.name} says woof"
