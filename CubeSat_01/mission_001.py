
from datetime import datetime

print("===EDU-01 TELEMETRY===")
print()

timestamp= datetime.now().strftime("%Y-%m-%d %H:%M:%S") #string format of the current date and time
print(f"Timestamp: {timestamp}")                                  

#temperature input
temperature = float(input("Input the temperature in Celsius: "))
if temperature < -40 or temperature > 85:
    print("CHECK: Temperature is out of range")
else:
    print("NORMAL: Temperature is within range")
print(f"The temperature is {temperature:.2f} °C.")

#batery voltage input
battery_voltage = float(input("Input the battery voltage in Volts: "))
if battery_voltage <= 0:
    print("CHECK: Invalid voltage")
else:
    print("NORMAL: Voltage is positive")
print(f"The battery voltage is {battery_voltage:.2f} V.")

