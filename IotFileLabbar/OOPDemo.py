import datetime

class Employee:
    def __init__(self, namn, birthDate):
        self.Namn = namn
        self.BirthDate = birthDate
        self.PostNr = ""
        self.PostOrt = ""
        self.GatuAdress = ""
        self.WorkedHour = 0

    def SetAddress(self, gatuAdress, postNr, postOrt):
        self.GatuAdress = gatuAdress
        self.PostNr = postNr
        self.PostOrt = postOrt

e = Employee("Stefan", datetime.date(1972,8,3))  

e.SetAddress("testgatan 12", "13245", "teststad")
e.WorkedHour = 12

r = Employee("Kerstin",datetime.date(1973,3,5))    
r.WorkedHour = 14



def CalculateSalary(employee):
    hourSalary = 120
    if employee.BirthDate.year < 1973:
        hourSalary = 220
    salary = hourSalary * employee.WorkedHours
    print(f"{employee.Namn} får {salary} i lön")    







lista = [e,r]

for emp in lista:
    CalculateSalary(emp)


