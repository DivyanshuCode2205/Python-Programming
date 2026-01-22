def conversion(c):
    return ((9/5 * c) + 32)

temperature = int(input("Enter temperature: "))

print(f"Celsius {temperature} to fahrenheit {conversion(temperature)}")