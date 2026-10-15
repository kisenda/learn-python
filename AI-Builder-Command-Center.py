#AI Builder Command Center

print("Welcome to the AI Builder Command Center!");

print("1. Calculator");
print("2. Project");
print("3. Progress");
print("4. Exit");
    
choice = input("Choose: ")

if choice == "1": import Calculator ;
elif choice == "2": print("Current Project: AI + Blender + MCP."); 
elif choice == "3": print("Month: 1, Week: 1, Status: Building") ;
elif choice == "4": exit()
else: print("Invalid choice. Please try again.");  