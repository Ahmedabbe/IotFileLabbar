import os

def DeleteIfExists(s):
    if os.path.isfile(s):
        os.remove(s)


DeleteIfExists("SampleFile-Lab3Result.txt")#not needed since "w" recreates

row = 1
with open("SampleFile-Lab3Result.txt", "w") as outDataFile:
    with open("SampleFile-Lab1.txt", "r") as indataFile1:
        for line in indataFile1:
            outDataFile.write(f"{row} {line}")
            row = row + 1




with open("SampleFile-Lab3Result.txt", "w") as outDataFile:
    with open("inData.txt", "r") as inDataFile:
        for line in inDataFile:
            outDataFile.write(line)
