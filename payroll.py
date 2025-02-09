from Calculator import hs_mult

def hs_payroll():
    
    global employeeInformation
    totalPayroll = 0

    while True:
        try:
            name = input("Enter Employee name (or 'exit' to go back to the main menu): ").strip()
            if name.lower() == "exit":
                break

            hours = float(input(f"Enter the amount of hours worked for {name}: "))
            rate = float(input(f"Enter the hourly wage for {name} $: "))

            total = hs_mult(hours, rate)
            totalPayroll += total

            employeeInformation.append({
                "name": name,
                "hours": hours,
                "rate": rate,
                "total": total,
                "totalPayroll": totalPayroll
            })

            print("\nPay-Roll")
            print(f"{name:<20} hours worked {hours} @ ${rate:<10} {total:>10,.2f}")
            print(f"\n{'Total Payroll':<20}{'':>36}{totalPayroll:,.2f}")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

    if employeeInformation:
        print("\nSummary of Pay-Roll")
        print(f"{'Name':<20}{'Hours Worked':<15}{'Hourly Rate':<15}{'Total Payroll':<15}")
        print("-" * 60)
        for person in employeeInformation:
            print(f"{person['name']:<20}{person['hours']:<15.2f}${person['rate']:<14.2f}${person['totalPayroll']:<14,.2f}\n")

hs_payroll()
