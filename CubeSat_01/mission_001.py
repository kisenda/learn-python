
#Sensor Input

print("===EDU-01 TELEMETRY===")
print()
temperature = float(input("Input the temperature in Celsius: "))
print(f"The temperature is {temperature:.2f} °C.")

battery_voltage = float(input("Input the battery voltage in Volts: "))
if battery_voltage <= 0:
    print("CHECK: Invalid voltage")
else:
    print("NORMAL: Voltage is positive")
    print(f"The battery voltage is {battery_voltage:.2f} V.")

