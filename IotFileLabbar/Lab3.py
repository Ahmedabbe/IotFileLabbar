import os

def DeleteIfExists(s):
    if os.path.isfile(s):
        os.remove(s)


row = 1
DeleteIfExists("SampleFile-Lab3Result.txt")#not needed since "w" recreates

with open("SampleFile-Lab3Result.txt", "w") as outDataFile:
    with open("SampleFile-Lab1.txt", "r") as indataFile1:
        for line in indataFile1:
            outDataFile.write(f"{row} {line}")
            row = row + 1
