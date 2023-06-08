import csv


class Distance:
    def __init__(self, distance0, distance1, distance2, distance3,
                 distance4, distance5,
                 distance6, distance7, distance8,
                 distance9, distance10, distance11, distance12, distance13, distance14, distance15, distance16,
                 distance17, distance18,
                 distance19, distance20, distance21, distance22, distance23, distance24, distance25, distance26):
        self.distance0 = distance0
        self.distance1 = distance1
        self.distance2 = distance2
        self.distance3 = distance3
        self.distance4 = distance4
        self.distance5 = distance5
        self.distance6 = distance6
        self.distance7 = distance7
        self.distance8 = distance8
        self.distance9 = distance9
        self.distance10 = distance10
        self.distance11 = distance11
        self.distance12 = distance12
        self.distance13 = distance13
        self.distance14 = distance14
        self.distance15 = distance15
        self.distance16 = distance16
        self.distance17 = distance17
        self.distance18 = distance18
        self.distance19 = distance19
        self.distance20 = distance20
        self.distance21 = distance21
        self.distance22 = distance22
        self.distance23 = distance23
        self.distance24 = distance24
        self.distance25 = distance25
        self.distance26 = distance26

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
               "%s, %s" % \
               (self.distance0, self.distance1, self.distance2,
                self.distance3, self.distance4, self.distance5,
                self.distance6, self.distance7, self.distance8, self.distance9, self.distance10, self.distance11,
                self.distance12, self.distance13,
                self.distance14, self.distance15, self.distance16, self.distance17, self.distance18, self.distance19,
                self.distance20, self.distance21,
                self.distance22, self.distance23, self.distance24, self.distance25, self.distance26)


    @staticmethod
    def create(distanceList, inputfile):
        with open(inputfile, encoding='utf-8-sig') as distanceFile:
            distanceData = csv.reader(distanceFile, delimiter=",")

            for distanceInfo in distanceData:
                distance0 = distanceInfo[0]
                distance1 = distanceInfo[1]
                distance2 = distanceInfo[2]
                distance3 = distanceInfo[3]
                distance4 = distanceInfo[4]
                distance5 = distanceInfo[5]
                distance6 = distanceInfo[6]
                distance7 = distanceInfo[7]
                distance8 = distanceInfo[8]
                distance9 = distanceInfo[9]
                distance10 = distanceInfo[10]
                distance11 = distanceInfo[11]
                distance12 = distanceInfo[12]
                distance13 = distanceInfo[13]
                distance14 = distanceInfo[14]
                distance15 = distanceInfo[15]
                distance16 = distanceInfo[16]
                distance17 = distanceInfo[17]
                distance18 = distanceInfo[18]
                distance19 = distanceInfo[19]
                distance20 = distanceInfo[20]
                distance21 = distanceInfo[21]
                distance22 = distanceInfo[22]
                distance23 = distanceInfo[23]
                distance24 = distanceInfo[24]
                distance25 = distanceInfo[25]
                distance26 = distanceInfo[26]

                distanceList.append([distance0, distance1, distance2, distance3,
                                     distance4, distance5,
                                     distance6, distance7, distance8,
                                     distance9, distance10, distance11, distance12, distance13, distance14, distance15,
                                     distance16,
                                     distance17, distance18,
                                     distance19, distance20, distance21, distance22, distance23, distance24,
                                     distance25, distance26])
