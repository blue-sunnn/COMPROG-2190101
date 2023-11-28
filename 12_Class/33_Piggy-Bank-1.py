class piggybank:
    def __init__(self):
        # has 4 variables storing the amount for each type of coins
        self.ones = 0
        self.twos = 0
        self.fives = 0
        self.tens = 0

    def add1(self, n):
        # adds n into the variable that stores 1-Baht coins
        self.ones += n

    def add2(self, n):
        # adds n into the variable that stores 2-Baht coins
        self.twos += n

    def add5(self, n):
        # adds n into the variable that stores 5-Baht coins
        self.fives += n

    def add10(self, n):
        # adds n into the variable that stores 10 Baht coins
        self.tens += n

    def __int__(self):
        # returns the total value (the amount of coins multiplied by coins value)
        ones = self.ones * 1
        twos = self.twos * 2
        fives = self.fives * 5
        tens = self.tens * 10
        return ones + twos + fives + tens

    def __lt__(self, rhs):
        # comparing the total money between self and rhs
        return int(self) < int(rhs)

    def __str__(self):
        # return the strings that shows the amount of each coin per example
        return '{' + '1:' + str(self.ones) + \
              ', ' + '2:' + str(self.twos) + \
              ', ' + '5:' + str(self.fives) + \
              ', ' + '10:' + str(self.tens) + '}'


cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank()
p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
