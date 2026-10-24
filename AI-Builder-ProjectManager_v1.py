Tasks = ["Learn Python", "Practice English", "Study German", "Build AI Project"]

def show_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# Memulai while loop agar menu terus berulang
while True:
    print("======================")
    print("AI BUILDER PROJECT MANAGER")
    print("======================")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_tasks(Tasks)
        
    elif choice == "2":
        new_task = input("Enter new task: ")
        Tasks.append(new_task)
        print("Task berhasil ditambahkan!")
        show_tasks(Tasks) # Diperbaiki: tidak perlu dibungkus print() lagi
        
    elif choice == "3":
        print("Goodbye, AI Builder!")
        break # Menghentikan while loop dan keluar dari program
        
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
        
    print() # Memberi jarak baris agar tampilan lebih rapi