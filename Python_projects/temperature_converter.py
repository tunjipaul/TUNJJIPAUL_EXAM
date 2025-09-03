#define functions for all temperature parameters.

def celsius_to_kelvin(c):
    if c < 0:
     raise ValueError("Kelvin is absolute and cannot be less than zero")
    return c + 273
def celsius_to_farenheit(c):
    return  (c * 1.8) + 32
def kelvin_to_celsius(k):
    return k-273
def kelvin_to_farenheit(k):
    return (1.8 * k) - 459.67
def farenheit_to_kelvin(f):
    if f < 0:
     raise ValueError("Kelvin is absolute and cannot be less than zero.")
    return (f + 459.67)/1.8
def farenheit_to_celsius(f):
    return (f-32)/1.8

#collect input for temp, choice and validate with try and except.
name = input("what is your name: ")
print(f"Welcome to {name} temp. converter")
print("Convert from\n1. Celsius to Farenheit\n2. Celsius to Kelvin\n3. Farenheit to Celsius\n4. Farenheit to Kelvin\
      \n5. Kelvin to Celsius\n6. Kelvin to Farenheit\n7. Exit")

while True:
    try:
     choice = input("Pick from the following options 1/2/3/4/5/6/7: ")
     temp = float(input("Enter the value of the temperature: "))
     if choice == "1":
          print(f"Celsius -> Farenheit: {celsius_to_farenheit(temp):,.2f}farenheit")  
     elif choice == "2":
         print(f"Celsius -> Kelvin: {celsius_to_kelvin(temp):,.2f}kelvin")
     elif choice == "3":
         print(f"Farenheit -> Celsius: {farenheit_to_celsius(temp):,.2f}celsius")
     elif choice == "4":
         print(f"Farenheit -> Kelvin: {farenheit_to_kelvin(temp):,.2f}kelvin")
     elif choice == "5":
         print(f"Kelvin -> Celsius: {kelvin_to_celsius(temp):,.2f}celsius")
     elif choice == "6":
         print(f"Kelvin -> Farenheit: {kelvin_to_farenheit(temp):,.2f}farenheit")
     elif choice == "7":
         print(f"Thank you for using {name} converter! Have a productive day!")
         break
     else:
         print("You have picked the wrong option. Try Again.")
    except ValueError:
        raise("You have entered the wrong value for temperature")
#handle edge cases such as negative kelvin values.

