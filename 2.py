class LeapYear:

    def __init__(self, year):
        self.year = year

    def isLeapYear(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    print(f"{self.year} is a leap year")
                else:
                    print(f"{self.year} is not a leap year")
            else:
                print(f"{self.year} is a leap year")
        else:
            print(f"{self.year} is not a leap year")


obj = LeapYear(int(input("Enter a year:")))
obj.isLeapYear()
print(obj.isLeapYear)