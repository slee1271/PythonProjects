def celsius_convert(celsius: float) -> float:
    farenheit = (9/5)*celsius + 32
    kelvin = celsius + 273.15
    return farenheit,kelvin

def farenheit_convert(farenheit: float) -> float:
    celsius = (farenheit - 32) * (5/9)
    kelvin = ((farenheit - 32) * (5/9)) + 273.15
    return celsius,kelvin

def kelvin_convert(kelvin: float) -> float:
    celsius = kelvin - 273.15
    farenheit = ((kelvin - 273.15) * (9/5)) + 32
    return celsius,farenheit


while True:
    print("What temperature do you currently have?") 
    print("1. Celsius")
    print("2. Farenheit")
    print("3. Kelvin")
    print("4. quit")
    user_input = input(": ")
    if user_input == "4" or user_input.lower() == "quit" or user_input == "":
        break 
    elif user_input == "1" or user_input.lower() == "celsius":
        celsius = float(input("What is your temperate in CELSIUS?: "))
        farenheit,kelvin = celsius_convert(celsius)
        print(f"Celsius: {celsius:.2f} --- Farenheit: {farenheit:.2f} --- Kelvin: {kelvin:.2f}")
        print("--------------------------------------------------------\n")   
    elif user_input == "2" or user_input.lower() == "farenheit":
        farenheit = float(input("What is your temperate in FARENHEIT?: "))
        celsius,kelvin = farenheit_convert(farenheit)
        print(f"Celsius: {celsius:.2f} --- Farenheit: {farenheit:.2f} --- Kelvin: {kelvin:.2f}")
        print("--------------------------------------------------------\n")  
    elif user_input == "3" or user_input.lower() == "kelvin":
        kelvin = float(input("What is your temperate in KELVIN?: "))
        celsius,farenheit = kelvin_convert(kelvin)
        print(f"Celsius: {celsius:.2f} --- Farenheit: {farenheit:.2f} --- Kelvin: {kelvin:.2f}")
        print("--------------------------------------------------------\n")  
    else:
        print(f"Invalid input. Enter an integer or name of temperature you currently have\n")