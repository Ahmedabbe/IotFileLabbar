import os

def GetUserLines():
    if not os.path.isfile("Lab5Users.txt"):
        return []
    with open("Lab5Users.txt", "r") as indataFile1:
        return indataFile1.readlines()


def UserExists(namn):
    for line in GetUserLines():
        parts = line.split("###")
        if len(parts) == 2:
            if parts[0].lower() == namn.lower():
                return True
    return False

def UserCorrectPassword(namn,pwd):
    for line in GetUserLines():
        parts = line.strip().split("###")
        if len(parts) == 2:
            if parts[0].lower() == namn.lower() and parts[1] == pwd:
                return True
    return False

def UserAdd(namn,pwd):
    with open("Lab5Users.txt", "a") as indataFile1:
        indataFile1.write(namn + "###" + pwd + "\n")

def Registrera():
    print("NY")

    while True:
        namn  = input("Ange användarnamn")
        if UserExists(namn):
            print("Redan taget")
            continue
        break

    pwd = input("Ange lösenord")
    UserAdd(namn,pwd)


def Login():
    print("Login")
    namn  = input("Ange användarnamn")
    pwd = input("Ange lösenord")
    if not UserExists(namn):
        return False
    if UserCorrectPassword(namn,pwd):
        return True
    return False


while True:
    print("Meny")
    print("a. Registrera")
    print("b. Logga in")
    sel= input("Välj->").lower()
    if sel == "a":
        Registrera()
    if sel == "b":
        if Login():
            print("Welcome")
        else:
            print("No access")
            