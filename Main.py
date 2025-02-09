'''
Program name: Test

class info: name, number, term, year (CSC1340. 9 February 2025)

Author: Haden Smith

Data: 

Notes: Thisnow imports both MPG.py and payroll.py and executes them within the main program.

'''

employeeInformation = []
tripStats = []

def displayMenu ():
    print("Menu")
    print("1. Payroll Information")
    print("2. Miles Per Gallon")
    print("3. Exit")
    

def main():
    while True:
       displayMenu()
       choice = input("Please make your selection: ")

       if choice == '1':
           f = open('payroll.py')
           exec(f.read(), globals())
        
       elif choice == '2':
           f = open('MPG.py')
           exec(f.read(), globals())

       elif choice == '3':
           print("Exiting Program.")
           break
       else:
           print("Invalid selection. Try again!")

main()