print("======================")
print("AI BUILDER PROJECT MANAGER")
print("======================")

print("1. Show Tasks")
print("2. Add Task")
print("3. Exit")

choice = input("Choose: ")

Tasks = ["Learn Python", "Practice English", "Study German", "Build AI Project"]

def show_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

if choice == "1":
    show_tasks(Tasks)
if choice == "2":
    new_task = input("Enter new task: ")
    Tasks.append(new_task)
    print(show_tasks(Tasks))
if choice == "3":
    print("Goodbye, AI Builder!")