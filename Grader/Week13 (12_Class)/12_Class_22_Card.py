class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return '(' + self.value + ' ' + self.suit + ')'

    def getScore(self):
        royals = ['J', 'Q', 'K']
        if self.value in royals:    s = 10
        elif self.value == 'A':     s = 1
        else:                       s = int(self.value)
        return s

    def sum(self, other):
        return (self.getScore() + other.getScore()) % 10

    def __lt__(self, rhs):
        if self.value != rhs.value:
            if self.value == '2':       sv = 15
            elif self.value == 'A':     sv = 14
            elif self.value == 'K':     sv = 13
            elif self.value == 'Q':     sv = 12
            elif self.value == 'J':     sv = 11
            else:   sv = int(self.value)

            if rhs.value == '2':        rv = 15
            elif rhs.value == 'A':      rv = 14
            elif rhs.value == 'K':      rv = 13
            elif rhs.value == 'Q':      rv = 12
            elif rhs.value == 'J':      rv = 11
            else:   rv = int(rhs.value)

            return sv < rv
        return self.suit < rhs.suit


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))

for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])
