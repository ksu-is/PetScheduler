def add_task(schedule):
    # Add a new task to the pet's schedule.
    print("\n--- Add a New Task ---")
    pet_name = input("Enter the pet's name: ")
    task_type = input("Enter the type of task (e.g., Vet Visit, Grooming): ")
    date = input("Enter the date for the task (YYYY-MM-DD): ")
    time = input("Enter the time for the task (e.g., 10:00 AM): ")
    
    task = (pet_name, task_type, date, time) 
    schedule.append(task)
    print("\nTask added| " + " [Pet Name: " + str(task[0]) +"]  " + "[Task type: " + str(task[1]) +"]  " + "[Date: " + str(task[2]) +"]  " + "[Time: " + str(task[3]) +"]  ")
    return schedule

def view_schedule(schedule):
    # Display all tasks in the schedule.
    print("\n--- View Schedule ---")
    if not schedule:
        print("No tasks scheduled.")
    else:
        index = 1
        for task in schedule:
            print(str(index) + ". " + task[0] + " - " + task[1] + " on " + task[2] + " at " + task[3])
            index += 1

def delete_task(schedule):
    # Remove a task from the schedule.
    print("\n--- Delete a Task ---")
    pet_name = input("Enter the pet's name for the task to delete: ")
    task_type = input("Enter the type of task to delete: ")
    
    task_found = False
    updated_schedule = []
    for task in schedule:
        if str(task[0]).lower() == pet_name.lower() and str(task[1]).lower() == task_type.lower():
            task_found = True
        else:
            updated_schedule.append(task)
    
    if task_found:
        print("Task '" + task_type + "' for " + pet_name + " removed.")
    else:
        print("No matching task found for '" + task_type + "' of " + pet_name + ".")
    return updated_schedule

def update_task(schedule):
    # Update a specific task in the schedule.
    print("\n--- Update a Task ---")
    pet_name = input("Enter the pet's name for the task to update: ")
    old_task_type = input("Enter the current type of task: ")
    
    updated = False
    updated_schedule = []
    for task in schedule:
        if str(task[0]).lower() == pet_name.lower() and str(task[1]).lower() == old_task_type.lower():
            print("Begin updating task below...")
            new_task_type = input("Enter the new task type: ")
            new_date = input("Enter the new date (YYYY-MM-DD): ")
            new_time = input("Enter the new time (e.g., 2:00 PM): ")
            updated_task = (pet_name, new_task_type, new_date, new_time)
            updated_schedule.append(updated_task)
            updated = True
            print("\nTask updated| " + " [Pet Name: " + str(updated_task[0]) +"]  " + "[Task type: " + str(updated_task[1]) +"]  " + "[Date: " + str(updated_task[2]) +"]  " + "[Time: " + str(updated_task[3]) +"]  ")
        else:
            updated_schedule.append(task)
    
    if not updated:
        print("No task found for '" + old_task_type + "' of " + pet_name + ".")
    return updated_schedule

def main():
    # Main function to run the Pet Care Scheduler.
    schedule = []
    while True:
        print("\n--- Pet Care Scheduler ---")
        print("1. Add Task")
        print("2. View Schedule")
        print("3. Delete Task")
        print("4. Update Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            schedule = add_task(schedule)
        elif choice == "2":
            view_schedule(schedule)
        elif choice == "3":
            schedule = delete_task(schedule)
        elif choice == "4":
            schedule = update_task(schedule)
        elif choice == "5":
            print("Exiting the scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
main()
