def main():

    import time

    def add(x, y):
        return x + y

    def minus(x, y):
        return x - y

    def times(x, y):
        return x * y

    def divide(x, y):
        return x / y

    print("Select your choice:")
    print("1- add")
    print("2- minus")
    print("3- times")
    print("4- divide")
    time.sleep (1)
    choice = input("Enter your choice: ")

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    if choice == '1':
        print(num1,"+",num2,"=", add(num1,num2))

    elif choice == '2':
        print(num1,"-",num2,"=", minus(num1,num2))

    elif choice == '3':
        print(num1,"*",num2,"=", times(num1,num2))

    elif choice == '4':
        print(num1,"/",num2,"=", divide(num1,num2))

    else:
        print("An error has occured, invalid choice.")
        
    restart= input("Do you wish to re-try? Y/N: ")
    if restart == "y":
        main()
        
    else:
        exit()
main()

        

        
