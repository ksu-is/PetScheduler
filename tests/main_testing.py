
def add_task(pet_name, task_type, date, time):
    # Add a new task to the pet's schedule.
    task = ("pet_name", pet_name, "task_type", task_type, "date", date, "time", time)
    print("Task added: " + str(task))
    return task

def view_schedule(schedule):
    # Display all tasks in the schedule.
    if len(schedule) == 0:
        print("No tasks scheduled.")
    else:
        for task in schedule:
            print(task[1] + " - " + task[3] + " on " + task[5] + " at " + task[7])

def delete_task(schedule, pet_name, task_type):
    # Remove a task from the schedule.
    updated_schedule = []
    task_found = False
    for task in schedule:
        if task[1] == pet_name and task[3] == task_type:
            task_found = True
        else:
            updated_schedule.append(task)
    if task_found:
        print("Task '" + task_type + "' for " + pet_name + " removed.")
    else:
        print("No matching task found for " + pet_name + ".")
    return updated_schedule

def update_task(schedule, pet_name, old_task_type, new_task_type, new_date, new_time):
    # Update a specific task in the schedule.
    updated = False
    for task in schedule:
        if task[1] == pet_name and task[3] == old_task_type:
            task = ("pet_name", pet_name, "task_type", new_task_type, "date", new_date, "time", new_time)
            updated = True
            print("Task updated: " + str(task))
    if not updated:
        print("Task '" + old_task_type + "' for " + pet_name + " not found.")
    return schedule
