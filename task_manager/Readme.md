Task Manager Readme
Task Management System
This is a simple Task Management System written in Python, designed for beginner-level understanding and to demonstrate key Object-Oriented Programming (OOP) principles. The system allows users to manage tasks by creating, updating, deleting, and assigning them to users.

Features
Users:

Create users with properties like id, name, and email.

Tasks:

Create tasks with properties like id, title, description, due_date, priority, status, and assigned_user.

Update task status to PENDING, IN_PROGRESS, or COMPLETED.

Assign tasks to users.

Retrieve tasks assigned to specific users.

Delete tasks.

Task Manager:

Manage all tasks and users.

Implements the Singleton design pattern to ensure a single instance of the TaskManager class.

Project Structure
project/
│
├── main.py          # Entry point for the application
├── user.py          # Contains the User class
├── task.py          # Contains the Task class
└── task_manager.py  # Contains the TaskManager class
Requirements
Python 3.7+

Installation
Clone the repository:

git clone https://github.com/your-repo/task-management-system.git
cd task-management-system
Run the main.py file:

python main.py
Usage
1. Creating Users
You can create users using the create_user method of the TaskManager class. Each user has an id, name, and email.

Example:

user1 = manager.create_user(1, "Alice", "alice@example.com")
user2 = manager.create_user(2, "Bob", "bob@example.com")
2. Creating Tasks
Tasks are created using the create_task method of the TaskManager class. Tasks can be assigned to a user and have properties like title, description, due_date, priority, and status.

Example:

task1 = manager.create_task(
    title="Complete AI Project",
    description="Work on an AI-driven chatbot.",
    due_date="2024-12-31",
    priority="High",
    assigned_user=user1
)
3. Updating Task Status
You can update the status of a task (e.g., PENDING, IN_PROGRESS, COMPLETED) using the update_task_status method.

Example:

manager.update_task_status(task1.id, "IN_PROGRESS")
4. Retrieving Tasks Assigned to a User
You can retrieve tasks assigned to a specific user using the get_tasks_by_user method.

Example:

user1_tasks = manager.get_tasks_by_user(user1.id)
for task in user1_tasks:
    print(task)
5. Deleting a Task
You can delete a task using the delete_task method by providing the task's id.

Example:

manager.delete_task(task2.id)
Example Output
When running main.py, the output will look like this:

Users created:
User(ID: 1, Name: Alice, Email: alice@example.com)
User(ID: 2, Name: Bob, Email: bob@example.com)

Tasks created:
Task(ID: 140314781851248, Title: Complete AI Project, Status: PENDING, Priority: High, Assigned To: User(ID: 1, Name: Alice, Email: alice@example.com))
Task(ID: 140314781851280, Title: Write Documentation, Status: PENDING, Priority: Medium, Assigned To: User(ID: 2, Name: Bob, Email: bob@example.com))

Updated task status:
Task(ID: 140314781851248, Title: Complete AI Project, Status: IN_PROGRESS, Priority: High, Assigned To: User(ID: 1, Name: Alice, Email: alice@example.com))

Tasks assigned to Alice:
Task(ID: 140314781851248, Title: Complete AI Project, Status: IN_PROGRESS, Priority: High, Assigned To: User(ID: 1, Name: Alice, Email: alice@example.com))

Remaining tasks:
Task(ID: 140314781851248, Title: Complete AI Project, Status: IN_PROGRESS, Priority: High, Assigned To: User(ID: 1, Name: Alice, Email: alice@example.com))
Key Concepts Demonstrated
Object-Oriented Programming (OOP):

Encapsulation of properties and methods in classes (User, Task, TaskManager).

Use of getters and setters for property validation.

String representations for better debugging and output.

Singleton Design Pattern:

Ensures only one instance of the TaskManager exists.

Thread Safety:

Use of a Lock in the Singleton implementation to ensure thread safety.

Data Management:

Handling user and task data with robust validation and efficient retrieval methods.

Future Enhancements
Add support for:

Email notifications for task reminders.

Saving data to a database or file.

User authentication and roles.

Improve the CLI or add a GUI for better user interaction.

Implement REST APIs to make the system accessible over a network.

License
This project is licensed under the MIT License. Feel free to use and modify it for educational or commercial purposes.

Contact
If you have any questions or suggestions, feel free to reach out.

