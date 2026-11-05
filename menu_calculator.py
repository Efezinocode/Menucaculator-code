def get_numbers():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    return num1, num2

def menu():
    result = None  

    while True:  
        print('\n1. Addition')  
        print('2. Subtraction')  
        print('3. Multiplication')  
        print('4. Division')  
        print('5. Exit')  

        choice = input("Choose option (1-5): ")  

        if choice == '5':
            print("Exit")
            break

        if choice in ['1', '2', '3', '4']:
            # Get numbers if this is the first calculation
            if result is None:
                num1, num2 = get_numbers()
            else:
                num1 = result
                num2 = int(input("Enter next number: "))

            # Perform operations
            if choice == '1':
                result = num1 + num2
            elif choice == '2':
                result = num1 - num2
            elif choice == '3':
                result = num1 * num2
            elif choice == '4':
                if num2 == 0:
                    print("Error: Cannot divide by zero")
                    continue 
                result = num1 / num2

            print("Answer:", result)
        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    menu()
