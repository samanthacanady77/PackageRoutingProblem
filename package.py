import csv


class Package:
    def __init__(self, id, address, city, state, zipcode, deadline, weight, notes, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status

    def __str__(self):
        return "*** ((Package ID#: %s))\n** %s, %s, %s,  %s\n* %-3skg | Deadline: %-15s | Status: %-15s | Notes: %s\n " % \
               (self.id, self.address, self.city, self.state, self.zipcode, self.weight, self.deadline, self.status,
                self.notes,)

    # This is a part of my scalable solution to adjusting the size of the hashtable at execution. It counts the lines
    # in the package CSV.

    @staticmethod
    def count(inputfile):
        with open(inputfile, encoding='utf-8-sig') as packagefile:
            packageData = csv.reader(packagefile, delimiter=",")
            totalPackages = 0

            for _ in packageData:
                totalPackages = totalPackages + 1

        return totalPackages

    # This creates the package objects and loads them into the hashtable from the CSV.
    @staticmethod
    def create(packageHash, inputfile):
        with open(inputfile, encoding='utf-8-sig') as packagefile:
            packageData = csv.reader(packagefile, delimiter=",")

            for packageInfo in packageData:
                pId = int(packageInfo[0])
                address = packageInfo[1]
                pCity = packageInfo[2]
                pState = packageInfo[3]
                pZipcode = packageInfo[4]
                pDeadline = packageInfo[5]
                pWeight = packageInfo[6]
                pNote = packageInfo[7]
                pStatus = "at the hub"

                packageObj = Package(pId, address, pCity, pState, pZipcode, pDeadline, pWeight, pNote, pStatus)

                packageHash.insert(pId, packageObj)  # O(n)

    # This is my solution to tracking packages.

    @staticmethod
    def packageTimeTracker(truckList, packageID, packageHash, timeCheckedString):
        speed = 18  # in mph

        if ":" not in timeCheckedString:
            print("Invalid entry, please try again using the format HH:mm")
            return

        # This ensures the data being input is in the proper time format by checking the length of the string
        if len(timeCheckedString) < 4:
            print("Invalid entry, please try again using the format HH:mm")
            return

        # The user passes in a string in the format of HH:mm that is then split at the ":" and loaded into a list.
        timeList = timeCheckedString.split(':')

        # This checks that the minutes input isn't less than 2 digits.

        if len(timeList[1]) < 2:
            print("Invalid entry, please try again using the format HH:mm")
            return

        # This catches any exceptions that arise from inputting any non-numeric entries for the time.
        try:
            timeCheckedHours = float(timeList[0])
            timeCheckedMinutes = float(timeList[1])
            # print(timeCheckedHours)
            # print(timeCheckedMinutes)

        except ValueError:
            print("Invalid entry, please try again")
            return

        if timeCheckedMinutes > 59:
            print("Invalid entry, minutes cannot exceed 59")
            return

        if timeCheckedHours > 23:
            print("Invalid entry, hours cannot exceed 23")
            return

        # This adds the integer values from the timeList and then converts them into minutes
        timeCheckedConverted = timeCheckedHours * 60 + timeCheckedMinutes

        # message to be printed from the menu
        printMessage = ""

        # Loops through every truck.
        for i in range(len(truckList)):

            # This is the time the hub opens in minutes. Converting everything into minutes was the easiest way to
            # figure out the arrival times.
            startTime = 480.0  # in minutes, 8:00am

            currentTruck = truckList[i]
            currentTruckPackageList = truckList[i].packageList

            # Delays truck 2 for the packages that are arriving late by flight
            if currentTruck == truckList[1]:
                startTime = 540.5  # in minutes, 9:05am

            # factors in truck 3 leaving only once the updated package address arrives at 10:20, not very scalable but a
            # good place for improvements later on
            if currentTruck == truckList[2]:
                startTime = 620.0  # in minutes, 10:20am

            # Goes through every package on each individual truck.
            for i in range(len(currentTruckPackageList)):

                # If the package ID entered matches one on the truck, it continues.
                if currentTruckPackageList[i][0] == packageID:

                    # This adds every package in route before the chosen package to a list.
                    tempList = currentTruckPackageList[0:(i + 1)]

                    packageTravelTime = 0

                    # This loops through all the packages in the temporary list and then adds the distances up.
                    for i in range(len(tempList)):
                        packageTravelTime = packageTravelTime + tempList[i][1]

                    # This takes the sum of the distance traveled for the chosen package and all packages that are
                    # delivered before it and converts it into minutes.
                    packageTravelTime = packageTravelTime / speed * 60  # minutes

                    # The arrival time is found by adding the start time (8:00 a.m) to the minutes it takes until the
                    # chosen package is delivered.
                    packageArrivalTime = startTime + packageTravelTime

                    # This updates package with the status "at the hub" and prints the status.
                    if timeCheckedConverted <= startTime:

                        # For proper formatting, takes minutes values less than 10 and adds a "0" to them.
                        if timeCheckedMinutes < 10:

                            packageHash.updateStatus(packageID, (
                                    "at the hub " + str(int(timeCheckedHours)) + ":0" + str(
                                int(timeCheckedMinutes))))
                            printMessage = "*Package #" + str(packageID) + " is " + packageHash.search(packageID).status

                        else:
                            packageHash.updateStatus(packageID, (
                                    "at the hub " + str(int(timeCheckedHours)) + ":" + str(int(timeCheckedMinutes))))
                            printMessage = "*Package #" + str(packageID) + " is " + packageHash.search(packageID).status


                    # This updates the package of the status with "en route" and prints the status.
                    elif packageArrivalTime > timeCheckedConverted > startTime:

                        # For proper formatting, takes minutes values less than 10 and adds a "0" to them.
                        if timeCheckedMinutes < 10:

                            packageHash.updateStatus(packageID, (
                                    "en route " + str(int(timeCheckedHours)) + ":0" + str(
                                int(timeCheckedMinutes))))
                            printMessage = "*Package #" + str(packageID) + " is " + packageHash.search(packageID).status

                        else:
                            packageHash.updateStatus(packageID, (
                                    "en route " + str(int(timeCheckedHours)) + ":" + str(int(timeCheckedMinutes))))
                            printMessage = "*Package #" + str(packageID) + " is " + packageHash.search(packageID).status


                    # This updates the status with the time the package was delivered and prints it.
                    elif timeCheckedConverted >= packageArrivalTime:
                        packageArrivalTimeHoursConverted = int(packageArrivalTime / 60)
                        packageArrivalTimeMinutesConverted = int(packageArrivalTime % 60)

                        # For proper formatting, takes minutes values less than 10 and adds a "0" to them.
                        if packageArrivalTimeMinutesConverted < 10:

                            packageHash.updateStatus(packageID, " was delivered at " + str(
                                packageArrivalTimeHoursConverted) + ":0" + str(packageArrivalTimeMinutesConverted))
                            printMessage = "Package #" + str(packageID) + packageHash.search(packageID).status
                        else:

                            packageHash.updateStatus(packageID, " was delivered at " + str(
                                packageArrivalTimeHoursConverted) + ":" + str(packageArrivalTimeMinutesConverted))
                            printMessage = "Package #" + str(packageID) + packageHash.search(packageID).status

                    print(printMessage)

                    return
