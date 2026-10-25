#Rocket Science

force = float(input("Input the force applied to the rocket in N: "))
mass = float(input("Input the mass of the rocket in kg: "))

if mass <= 0:
    print("Mass must be greater than zero.")
else:
    acceleration = force / mass
    print(f"The acceleration of the rocket is {acceleration:.2f} m/s².")