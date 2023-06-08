
import sys
from algorithmRevised import Algorithm
from hashtable import Hashtable
from distance import Distance
from address import Address
from package import Package
from truck import Truck



distanceList = list()
addressList = list()
truckList = list()

myTruck = Truck(0, [], 0)
myPackage = Package(0, '', '', '', '', '', '', '', '')
myAddress = Address("")
myDistance = Distance(0, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                      '', '')

# A scalable way to get the total number of packages in the CSV file to pass to the hashtable class in order
# to create a hashtable of the necessary size.
totalPackages = myPackage.count('package.csv')  #

# This creates the package hashtable.
packageHash = Hashtable(totalPackages)

# This extracts the data from the 3 CSVs.
myDistance.create(distanceList, 'distance.csv')
myAddress.create(addressList, 'address.csv')
myPackage.create(packageHash, 'package.csv')

# Here I manually load the trucks for simplicity.
truck1 = Truck(1, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 2, 4, 40, 37], 0)

truck2 = Truck(2, [25, 3, 18, 36, 38, 6, 8, 10, 11, 12, 17, 21, 22, 23, 24], 0)

truck3 = Truck(3, [28, 9, 26, 27, 33, 35, 7, 39, 5, 32], 0)

# This creates a list of all available trucks. This could be done in a more scalable way using user input,
# but for simplicity's sake, I left it alone.
truckList.append(truck1)
truckList.append(truck2)
truckList.append(truck3)

totalMiles = 0

# This updates the incorrect address on package #9.
packageHash.search(9).address = "410 S State St"
packageHash.search(9).city = "Salt Lake City"
packageHash.search(9).state = "UT"
packageHash.search(9).zipcode = "84111"


# My Nearest Neighbor algorithm. It dynamically creates the route based on the shortest distance between packages.
Algorithm(packageHash, distanceList, addressList, myAddress, myDistance, truckList, totalMiles)  # Time: O(n^5 + n)


# A rudimentary menu for the user to interact with.
titleText = "\n^｡･ﾟﾟ･^｡･ﾟﾟ･Package Routing Program･ﾟﾟ･｡^･ﾟﾟ･｡^"
selectionMenuText = "\n\n   .・゜Please make a selection:゜・．\n\n" \
                    "       1.View the status of a package\n" \
                    "       2.View the status of all packages\n" \
                    "       3.View all trucks and total milage\n\n" \
                    ">>>Enter \"Exit\" at any time to exit<<<\n"

packageIDMenuText = ".・゜Enter package ID:゜・．\n"

timeMenuChoiceText = "Enter a time:\n" \
                     "(e.g. 13:00)\n"

print(titleText.center(5))

exit = False

# Keeps the program running until exit returns as True.
while not exit:
    selectionMenuChoice = input(selectionMenuText.center(5))

    # View the status of a package:
    if selectionMenuChoice == '1':
        exitStatusMenu = False

        # Keeps the package status menu running until exitStatusMenu returns as True.
        while not exitStatusMenu:
            exitPackageIDEnterMenu = False

            # Enter a package ID:
            packageIDMenuChoice = input(packageIDMenuText.center(5))

            # Exit option
            if packageIDMenuChoice == 'Exit':
                print("Goodbye!")
                sys.exit()

            # This handles string inputs for the package ID.
            try:
                if not isinstance(int(packageIDMenuChoice), int):
                    print("Invalid entry, please try again")
                    break
                # This alerts the user if the package ID does not exist within the hashtable.
                if packageHash.search(int(packageIDMenuChoice)) == None:
                    print("Package ID doesn't exist, please try again")
                    break
            # This handles other errors for inputs
            except ValueError:
                print("Invalid entry, please try again")
                break

            else:
                exitTimeMenu = False

                # This keeps the time menu open until exitTimeMenu is True.
                while not exitTimeMenu:

                    # Enter a time
                    timeMenuMenuChoice = input(timeMenuChoiceText.center(5))

                    # Exit option
                    if timeMenuMenuChoice == 'Exit':
                        print("Goodbye!")
                        sys.exit()

                    # Passes the data input to the time tracker.
                    myPackage.packageTimeTracker(truckList, int(packageIDMenuChoice), packageHash, timeMenuMenuChoice, )

                    exitTimeMenu = True

                exitStatusMenu = True

    # This shows the status of ALL packages.
    elif selectionMenuChoice == '2':
        exitTimeMenu = False

        # This keeps the time menu open until exitTimeMenu is True.
        while not exitTimeMenu:
            timeMenuMenuChoice = input(timeMenuChoiceText.center(5))

            # Exit option
            if timeMenuMenuChoice == 'Exit':
                print("Goodbye!")
                sys.exit()

            # Prints package status information for every package using an input time.
            for i in range(totalPackages):
                myPackage.packageTimeTracker(truckList, int(i + 1), packageHash, timeMenuMenuChoice)
                # (list of trucks, package ID, package hashtable, time being searched)
                print("(Deadline: " + packageHash.search(int(i + 1)).deadline + ")")

            exitTimeMenu = True

    # Prints all the necessary truck information from each truck in the truck list.
    elif selectionMenuChoice == '3':
        totalMilesTraveled = 0

        for i in range(len(truckList)):
            currentTruck = truckList[i]

            print("\n\n*** ((Truck ID#: " + str(truckList[i].truckID) + "))")
            print("**Miles Traveled: " + str(round(currentTruck.milesTraveled, 2)))
            print("*Packages: ")
            for i in range(len(currentTruck.packageList)):
                print(currentTruck.packageList[i][0], end=', ')

            totalMilesTraveled = totalMilesTraveled + currentTruck.milesTraveled

        print("\n\nTotal Miles: ")
        print(round(totalMilesTraveled, 2))

    # Exit
    elif selectionMenuChoice == 'Exit':
        exit = True
        print("Goodbye!")
