class Jar:
    def __init__(self, capacity: int=12):
        self._validate_positive_integer(capacity)

        if capacity < 0:
            raise ValueError("It's not a positive number.")

        self._capacity = capacity
        self._cookies = 0


    def __str__(self):
        return "🍪" * self._cookies


    def deposit(self, n: int):
        self._validate_positive_integer(n)

        if n > self._capacity or (self._cookies + n) > self._capacity:
            raise ValueError(f"Adding {n} cookies would exceed the jar's capacity.")

        self._cookies += n


    def withdraw(self, n: int):
        self._validate_positive_integer(n)

        if n > self._cookies:
            raise ValueError("There aren’t that many cookies in the cookie jar.")

        self._cookies -= n


    def _validate_positive_integer(self, value: int):
        if not isinstance(value, int):
            raise ValueError("It's not a number.")


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._cookies
