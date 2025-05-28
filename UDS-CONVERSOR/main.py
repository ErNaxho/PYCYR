def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Conversor de Unidades")
    print("1. Kilómetros a Millas")
    print("2. Millas a Kilómetros")
    print("3. Celsius a Fahrenheit")
    print("4. Fahrenheit a Celsius")
    print("5. Salir")

    while True:
        choice = input("Seleccione una opción (1-5): ")
        if choice == '1':
            km = float(input("Ingrese kilómetros: "))
            print(f"{km} kilómetros son {km_to_miles(km):.2f} millas.")
        elif choice == '2':
            miles = float(input("Ingrese millas: "))
            print(f"{miles} millas son {miles_to_km(miles):.2f} kilómetros.")
        elif choice == '3':
            celsius = float(input("Ingrese grados Celsius: "))
            print(f"{celsius}°C son {celsius_to_fahrenheit(celsius):.2f}°F.")
        elif choice == '4':
            fahrenheit = float(input("Ingrese grados Fahrenheit: "))
            print(f"{fahrenheit}°F son {fahrenheit_to_celsius(fahrenheit):.2f}°C.")
        elif choice == '5':
            print("Saliendo del conversor. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()