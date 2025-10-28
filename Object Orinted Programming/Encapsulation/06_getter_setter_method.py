# 06_getter_setter_method.py
# Simple OOP example showing getter/setter (classic methods + @property)

class Person:
    def __init__(self, name: str, age: int):
        self._name = None
        self._age = None
        self.set_name(name)   # use setter to validate
        self.age = age        # uses @property setter

    # Classic getter/setter for name
    def get_name(self) -> str:
        return self._name

    def set_name(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("name must be a non-empty string")
        self._name = value.strip()

    # Pythonic property for age with validation
    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if not isinstance(value, int) or value < 0:
            raise ValueError("age must be a non-negative integer")
        self._age = value

    def __repr__(self) -> str:
        return f"Person(name={self._name!r}, age={self._age!r})"


if __name__ == "__main__":
    p = Person("Alice", 30)
    print(p)                   # Person(name='Alice', age=30)

    # Using classic getters/setters
    p.set_name(" Bob ")
    print(p.get_name())        # "Bob"

    # Using property setter/getter
    p.age = 35
    print(p.age)               # 35

    # Validation example
    try:
        p.age = -1
    except ValueError as e:
        print("Error:", e)     # Error: age must be a non-negative integer