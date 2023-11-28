public_deck = [(i, j) for i in range(3, 16) for j in ('club', 'diamond', 'heart', 'spade')]
public_Jto2 = {'J': 11, 'Q': 12, 'K': 13, 'A': 14, '2': 15}

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return '(' + str(self.value) + ' ' + str(self.suit) + ')'

    def next1(self):
        deck = public_deck
        Jto2 = public_Jto2
        rev = {v: k for k, v in Jto2.items()}

        if self.value in Jto2:
            val = Jto2[self.value]
        else:
            val = int(self.value)

        idx = (deck.index((val, self.suit)) + 1) % 52
        out = deck[idx]

        if out[0] in rev:
            out = rev[out[0]], out[1]
        return Card(str(out[0]), str(out[1]))

    def next2(self):
        deck = public_deck
        Jto2 = public_Jto2
        rev = {v: k for k, v in Jto2.items()}

        if self.value in Jto2:
            val = Jto2[self.value]
        else:
            val = int(self.value)

        idx = (deck.index((val, self.suit)) + 1) % 52
        out = deck[idx]

        if out[0] in rev:
            out = rev[out[0]], out[1]
        self.value, self.suit = str(out[0]), str(out[1])


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))

for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
