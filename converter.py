#Fahrenheit to celsius conversion
def f_to_c(f):
    return (f-32)*5/9
#Celsius to fahrenheit conversion
def c_to_f(c):
    return (c*9/5)+32
#Kilometers to miles conversion
def km_to_mi(km):
    return km*0.621371
#Miles to kilometers conversion
def mi_to_km(mi):
    return mi*1.609344

def main():
    print('Hello it is a converter!\n\
----------\n\
[1]:Convert Celsius to Fahrenheit\n\
[2]:Convert Fahrenheit to celsius\n\
[3]:Convert Miles to Kilometers\n\
[4]:Convert Kilometers to Miles\n\
----------')

    #Ask what variable to convert
    ask = input('\nWhat conversion do you want to perform?(1 / 2 / 3 / 4): ')
    try:    
        print(f'{ask} chosen!')
    except ValueError:
        print('Invalid input. Please enter a numeric value')

    #Return converted variables
    if ask == '1':
        celsius = input('Type your celsius temperature: ')
        try:
            celsius = float(celsius)
            fahrenheit = c_to_f(celsius)
            print(f'{celsius} in fahrenheit will be {fahrenheit}')
        except ValueError:
            print('Invalid input. Please enter a numeric value for the temperature.')

    elif ask == '2':
        fahrenheit = input('Type your fahrenheit temperature: ')
        try:
            fahrenheit = float(fahrenheit)
            celsius = f_to_c(fahrenheit)
            print(f'{fahrenheit} in celsius will be {celsius}')
        except ValueError:
            print('Invalid input. Please enter a numeric value for the temperature.')

    elif ask == '3':
        miles = input('Type your miles distance: ')
        try:
            miles = float(miles)
            kilometers = mi_to_km(miles)
            print(f'{miles} in kilometers will be {kilometers}')
        except ValueError:
            print('Invalid input. Please enter a numeric value for the distance.')

    elif ask == '4':
        kilometers = input('Type your kilometers distance: ')
        try:
            kilometers = float(kilometers)
            miles = km_to_mi(kilometers)
            print(f'{kilometers} in miles will be {miles}')
        except ValueError:
            print('Invalid input. Please enter a numeric value for the distance.')
#Call the main function
main()