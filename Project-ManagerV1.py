def show_tasks(tasks):
        print("====My Tasks====")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

Tasks = ["Learn Python", "Practice English", "Study German", "Build AI Project"]

show_tasks(Tasks)