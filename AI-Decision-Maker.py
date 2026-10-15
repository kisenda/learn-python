input("What is your name ?")
input("What do you want to learn ?")
hours = input("How many hours can you study today ?")

if float(hours) >= 3 : 
    print("Great! You can learn deeply today.")
elif float(hours) >= 1 and float(hours) < 3 :
    print("Good! Focus on one small skill today.")
else:
    print("Even 30 minutes is valuable. Keep going!")