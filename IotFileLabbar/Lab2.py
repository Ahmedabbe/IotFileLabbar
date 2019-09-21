import os

def DeleteIfExists(s):
    if os.path.isfile(s):
        os.remove(s)

DeleteIfExists("SampleFile-Lab2Result.txt")#not needed since "w" recreates

with open("SampleFile-Lab2Result.txt", "w") as outDataFile:
    with open("SampleFile-Lab1.txt", "r") as indataFile1:
        for line in indataFile1:
            outDataFile.write(line)
    with open("SampleFile2-Lab1.txt", "r") as indataFile2:
        for line in indataFile2:
            outDataFile.write(line)
