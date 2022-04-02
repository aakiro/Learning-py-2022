import random

print("Welcome to the Password generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=§£"

number = input("the Amount of password to generate, ")
number = int(number)

length = input("Your password length: ")
length = int(length)

print ("Here are your passwords: ")

for pwd in range (number):
    passwords = ""
    for c in range (length):
        passwords += random.choice(chars)
    print (passwords)
    
          


