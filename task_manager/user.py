class User:
    def __init__(self, user_id, name, email):
        self._id = user_id
        self._name = name
        self._email = email

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("ID must be an integer.")
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email address.")
        self._email = value

    def __str__(self):
        return f"User(ID: {self.id}, Name: {self.name}, Email: {self.email})"
