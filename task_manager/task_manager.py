from threading import Lock
from task import Task
from user import User

class TaskManager:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.tasks = []
                cls._instance.users = []
        return cls._instance

    def create_user(self, user_id, name, email):
        user = User(user_id, name, email)
        self.users.append(user)
        return user

    def create_task(self, title, description, due_date, priority, assigned_user=None):
        task = Task(title, description, due_date, priority, assigned_user)
        self.tasks.append(task)
        return task

    def get_tasks_by_user(self, user_id):
        return [task for task in self.tasks if task.assigned_user and task.assigned_user.id == user_id]

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task_status(self, task_id, status):
        task = self.get_task_by_id(task_id)
        if task:
            task.status = status
            return task
        return None

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    #search the task based on the criteria
    def search_task(self, **criteria):
        results = self.tasks
        if "title" in criteria:
            results = [task for task in results if task.title == criteria["title"]]
        if "priority" in criteria:
            results = [task for task in self.tasks if task.priority == criteria["priority"]]
        if "status" in criteria:
            results = [task for task in results if task.status == criteria["status"]]
        
        return results
    
    def __str__(self):
        return f"TaskManager(Users: {len(self.users)}, Tasks: {len(self.tasks)})"
