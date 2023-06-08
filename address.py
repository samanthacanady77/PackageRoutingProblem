import csv


class Address:
    def __init__(self, address):
        self.address = address

    def __str__(self):
        return "%s, %s" % \
               self.address

    @staticmethod
    def create(addressList, inputfile):
        with open(inputfile, encoding='utf-8-sig') as addressfile:
            addressData = csv.reader(addressfile, delimiter=",")

            for addressInfo in addressData:
                address = addressInfo[0]

                addressList.append(address)

    @staticmethod
    def lookup(address, addressList, distanceList):
        for i in range(len(addressList)):
            if addressList[i] == address:
                    return distanceList[i]
        return print("Address not found")


    @staticmethod
    def lookupReturnIndex(address, addressList, distanceList):
        for i in range(len(addressList)):
            if addressList[i] == address:
                    return i
        return print("Address not found")