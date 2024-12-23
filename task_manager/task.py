from user import User

class Task:
    def __init__(self, title, description, due_date, priority, assigned_user=None):
        self._id = id(self)
        self._title = title
        self._description = description
        self._due_date = due_date
        self._priority = priority
        self._status = "PENDING"
        self._assigned_user = assigned_user

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value.strip():
            raise ValueError("Title cannot be empty.")
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not value.strip():
            raise ValueError("Description cannot be empty.")
        self._description = value

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        self._due_date = value

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        if value not in ["High", "Medium", "Low"]:
            raise ValueError("Priority must be 'High', 'Medium', or 'Low'.")
        self._priority = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in ["PENDING", "IN_PROGRESS", "COMPLETED"]:
            raise ValueError("Invalid status.")
        self._status = value

    @property
    def assigned_user(self):
        return self._assigned_user

    @assigned_user.setter
    def assigned_user(self, value):
        if value is not None and not isinstance(value, User):
            raise ValueError("Assigned user must be a User object or None.")
        self._assigned_user = value

    def __str__(self):
        return (f"Task(ID: {self.id}, Title: {self.title}, Status: {self.status}, "
                f"Priority: {self.priority}, Assigned To: {self.assigned_user})")
