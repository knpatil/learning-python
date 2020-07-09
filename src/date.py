class Date:
    def __init__(self, month, day):
        self.month = month  # member variable  / properties
        self.day = day

    def advance(self):
        # last day of the month
        if self.month in [1, 3, 5, 7, 8, 10, 12]:  # 31 days in this category
            if self.day < 31:
                self.day += 1
            else:
                self.day = 1
                if self.month < 12:
                    self.month += 1
                else:
                    self.month = 1
        elif self.month in [4, 6, 9, 11]: # 30 days in this category
            if self.day < 30:
                self.day += 1
            else:
                self.day = 1
                self.month += 1
        else:  # feb
            if self.day < 28:
                self.day += 1
            else:
                self.day = 1
                self.month += 1

    def days_in_month(self):
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif self.month in [4, 6, 9, 11]:
            return 30
        else:
            return 28

    def __eq__(self, obj):
        return self.month == obj.month and self.day == obj.day  # logical expression

    def __str__(self):
        return f"{self.month}/{self.day}"


d1 = Date(7, 8)

print(d1.days_in_month())

d2 = Date(7, 11)

if d1 == d2:
    print("same date")
else:
    print("different")

d3 = Date(7, 8)

if d1 == d3:
    print("same date")
else:
    print("different")