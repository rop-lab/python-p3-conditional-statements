#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
    
        print("Access denied")
        return "Access denied"
    # Test the function with different usern
result =  admin_login("admin", "12345")
print(result)
    

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature < 60:
        return "It's a little chilly out there!"
    elif 65 <= temperature <= 85:
        return "It's perfect out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    
    else:
        return "It's a pleasant day!"
        
    

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            print("Cannot divide by zero")
            return None
    else:
        print("Invalid operation!")
        return None

    
