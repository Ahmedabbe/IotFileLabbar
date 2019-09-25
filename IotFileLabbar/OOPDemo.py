import datetime

class Employee:
    def __init__(self, namn, birthDate):
        self.Namn = namn
        self._BirthDate = birthDate
        self._PostNr = ""
        self._PostOrt = ""
        self._GatuAdress = ""
        self._WorkedHour = 0

    def SetWorkedHours(self, newValue):
        if newValue < 0:
            raise ValueError("Ange fel värde")
        self._WorkedHour = newValue

    def SetAddress(self, gatuAdress, postNr, postOrt):
        self._GatuAdress = gatuAdress
        self._PostNr = postNr
        self._PostOrt = postOrt

    def CalculateSalary(self):
        hourSalary = 120
        if self._BirthDate.year < 1973:
            hourSalary = 220
        salary = hourSalary * self._WorkedHour
        return salary

    

e = Employee("Stefan", datetime.date(1972,8,3))  
e.Namn = "Kalle"

e.SetAddress("testgatan 1","213","sdadasdsa")
e.SetWorkedHours(12)

r = Employee("Kerstin",datetime.date(1973,3,5))    
r.SetWorkedHours(14)

lista = [e,r]

for emp in lista:
    salary = emp.CalculateSalary()
    print(f"{emp.Namn} får {salary}")


