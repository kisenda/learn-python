#Rocket Science

thrust = float(input("Input the thrust applied to the rocket in N: "))
mass = float(input("Input the mass of the rocket in kg: "))
drag = float(input("Input the drag force acting on the rocket in N: "))

if mass <= 0:
    print("Mass must be greater than zero.")
elif drag < 0:
    print("Drag force cannot be negative.")
else:
    gravity = 9.81  # Acceleration due to gravity in m/s²
    weight = mass * gravity  # Calculate weight in Newtons

    net_force = thrust - weight - drag
    acceleration = net_force / mass
    print(f"The acceleration of the rocket is {acceleration:.2f} m/s².")