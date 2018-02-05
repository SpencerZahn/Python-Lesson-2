#Spencer Zahn - Python lesson 2 - Exercise 5 - 013118

#Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

x = int(input("Enter temperature in Celsius: "))

fah = (1.8 * x) + 32

cel = (fah - x) / 1.8

    
print (fah)
