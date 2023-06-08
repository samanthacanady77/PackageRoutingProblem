from operator import itemgetter

def Algorithm(packageHash, distanceList, addressList, myAddress, myDistance, truckList,
              totalMiles):


    unsortedList = list()
    packagesLoaded = list()

    leftHub = False

    # This loops through every truck.
    for i in range(len(truckList)):
        truck = truckList[i]
        packageList = truck.packageList

        # A temp list used to prevent modification of the initial list of packages and keep track of what packages
        # have been loaded.
        remainingPackages = list() + packageList

        # This keeps the loop going while there are packages left to be sorted
        while len(remainingPackages) > 0:

            # If the package hasn't left the hub, it creates a list of all the packages and adds them to a list
            # with their distance to the hub.
            if not leftHub:

                for i in range(len(remainingPackages)):

                        currentPackage = remainingPackages[i]
                        currentDistance = distanceList[0][
                            addressList.index(packageHash.search(remainingPackages[i]).address)]

                        unsortedList.append([currentPackage, float(currentDistance)])

                leftHub = True

            # If the package has left the hub:
            elif leftHub:

                # Gets the previous package from the sorted package list (packagesLoaded) by finding the final
                # index
                previousPackage = packagesLoaded[len(packagesLoaded) - 1][0]
                previousPackageAddress = packageHash.search(previousPackage).address
                previousPackageAddressIndex = addressList.index(previousPackageAddress)

                # This creates a list of all the remaining packages and their distance from the previous package.
                for i in range(len(remainingPackages)):

                        currentPackage = remainingPackages[i]
                        currentDistance = distanceList[previousPackageAddressIndex][
                            addressList.index(packageHash.search(remainingPackages[i]).address)]

                        unsortedList.append([currentPackage, float(currentDistance)])

            # This finds the minimum distance from the sorted list of packages above
            minDistance = min(unsortedList, key=itemgetter(1))

            # This appends the package ID and distance data to a list for the sorted packages.
            packagesLoaded.append(minDistance)

            # This removes the package that was loaded from the remaining package list.
            remainingPackages.remove(minDistance[0])

            # This clears the unsorted list to be used on the next iteration.
            unsortedList.clear()

        # This loads the sorted packages onto the truck.
        truck.packageList = list(packagesLoaded)

        # This calculates how many miles were traveled using the distance data saved to the sorted list.
        milesTraveled = 0
        for i in range(len(packagesLoaded)):
            milesTraveled = milesTraveled + packagesLoaded[i][1]
            totalMiles = totalMiles + packagesLoaded[i][1]

        # This gets the return distance of the final package.
        finalPackage = packagesLoaded[len(packagesLoaded) - 1][0]
        returnDistance = distanceList[addressList.index(packageHash.search(finalPackage).address)][0]

        totalMiles = totalMiles + float(returnDistance)
        milesTraveled = milesTraveled + float(returnDistance)

        # This adds the total number of miles traveled to the truck objects.
        truck.milesTraveled = milesTraveled

        packagesLoaded.clear()
        leftHub = False
