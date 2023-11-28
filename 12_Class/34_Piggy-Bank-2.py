class piggybank:
    def __init__(self):
        # Has variable self.coins contains an empty dict at the start
        # Has key as a coin value, and value as a number of coins
        self.coins = {}

    def add(self, v, n):
        # If a number of coin increase by n coins and exceed 100,
        # it will not increase, return False as add function has failed
        # Convert v into float first (5 -> 5.0)
        # If a bank never have any v coins, make self.coins[v]=0
        # Call function self.coins[v] += n
        # Return True as add function is a success
        v = float(v)
        if n + sum(self.coins.values()) > 100: return False
        
        if v not in self.coins: self.coins[v] = 0
        self.coins[v] += n

        return True

    def __float__(self):
        # Multiply coins value with a number of coin for every coin types
        # Must return only as float (0 -> 0.0)
        return float(sum([k * v for k, v in self.coins.items()]))

    def __str__(self):
        # Return string that show a number of coin of every coin types
        # Arrange from the lowest to highest coin values
        sc = sorted(self.coins.keys())
        out = [str(e) + ':' + str(self.coins[e]) for e in sc]
        return '{' + ', '.join(out) + '}'


cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank()
p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
