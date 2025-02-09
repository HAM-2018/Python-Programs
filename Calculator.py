'''
Program name: Test

class info: CSC1340  18 January 2025

Author: Haden Smith

Data: 

Notes: Simple menu and calculator program

'''


def hs_add(x, y):
    return x + y

def hs_sub(x,y):
    return x - y

def hs_mult(x, y):
    return x * y

def hs_div(x, y):
    if y == 0:
        return "Can not divide by zero!"
    return x / y

def hs_printResult(x, y, operation, symbol):
    result = operation(x, y)
    print(f"{x} {symbol} {y} = {result}")

    
def main():
    name = input("Enter your name: ")

    print(f"Welcome {name}!")

    while True:
        print("1) hs_add\n2) hs_sub\n3) hs_mult\n4) hs_div\n 5) Exit\n What would you like to do? ")
        choice = input("What would you like to do? ")

        if choice == "5":
            print(f"Goodbye {name}, thanks for using my application!")
            break

        if choice in ["1", "2", "3", "4"]:
            try:
                x = float(input("Enter the first number: "))
                y = float(input("Enter the second number: "))
    
                if choice == "1":
                    hs_printResult(x, y, hs_add, '+')
                if choice =="2":
                    hs_printResult(x,y,hs_sub,"-")
                if choice =="3":
                    hs_printResult(x, y, hs_mult, '*')
                if choice == "4":
                    hs_printResult(x, y, hs_div, '/')

            except ValueError:
                print("Please enter a numeric value!")
        else:
            print("Invalid choice! Please try")

if __name__ == "__main__":
    main()
