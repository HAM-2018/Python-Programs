from Calculator import hs_div

def hs_MPG():
    global tripStats
    mpg = 0

    while True:
        try:
        
            tripName = input ("Enter the name of the trip! (Enter 'exit' to go back.): ").strip()
            if tripName.lower() == "exit":
                break
            car = input("Enter the car used on this trip: ").strip()
            miles = float(input(f"Enter the miles driven in the {car}: "))
            gallons = float(input("Enter the gallons consumed during the trip: "))

            mpg = hs_div(miles, gallons)

            tripStats.append({
                "tripName": tripName,
                "car": car,
                "miles": miles,
                "gallons": gallons,
                "MPG": mpg
            })

            print(f"\n{tripName}")
            print("-" * 18)
            print(f"\n{car:<10} Miles: {miles:<10} Gallons: {gallons:<10} MPG: {mpg:<10}\n")

        except ValueError: 
            print("Please enter numbers only for miles and gallons!!")

    if (tripStats):
        print("Summary of trips!")
        print("-" * 40)
        for trip in tripStats:
            print(f"{trip['tripName']}")
            print(f"{trip['car']:<15} Miles: {trip['miles']:<10.2f} Gallons: {trip['gallons']:<10.2f} MPG: {trip['MPG']:<10.2f}\n")


hs_MPG()