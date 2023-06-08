class Truck:
    def __init__(self, truckID, packageList, milesTraveled):
        self.truckID = truckID
        self.packageList = packageList
        self.milesTraveled = milesTraveled

    def __str__(self):
        return "*** ((Truck ID#: %s))\n** Packages: %s\n** Miles Traveled: %s\n " % \
               (self.truckID, self.packageList, self.milesTraveled)


