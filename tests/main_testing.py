
def add_task(pet_name, task_type, date, time):
    """Add a new task to the pet's schedule."""
    task = ("pet_name", pet_name, "task_type", task_type, "date", date, "time", time)
    print("Task added: " + str(task))
    return task
