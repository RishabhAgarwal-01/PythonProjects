from task_manager import TaskManager

def main():
    manager = TaskManager()

    # Step 1: Create Users
    user1 = manager.create_user(1, "Alice", "alice@example.com")
    user2 = manager.create_user(2, "Bob", "bob@example.com")
    print("Users created:")
    print(user1)
    print(user2)

    # Step 2: Create Tasks
    task1 = manager.create_task(
        title="Complete AI Project",
        description="Work on an AI-driven chatbot.",
        due_date="2024-12-31",
        priority="High",
        assigned_user=user1
    )
    task2 = manager.create_task(
        title="Write Documentation",
        description="Prepare the project documentation.",
        due_date="2024-12-25",
        priority="Medium",
        assigned_user=user2
    )
    print("\nTasks created:")
    print(task1)
    print(task2)

    # Step 3: Update Task Status
    manager.update_task_status(task1.id, "IN_PROGRESS")
    print("\nUpdated task status:")
    print(task1)

    # Step 4: Get Tasks for a User
    user1_tasks = manager.get_tasks_by_user(user1.id)
    print(f"\nTasks assigned to {user1.name}:")
    for task in user1_tasks:
        print(task)

    # Step 5: Delete a Task
    manager.delete_task(task2.id)
    print("\nRemaining tasks:")
    for task in manager.tasks:
        print(task)

if __name__ == "__main__":
    main()
