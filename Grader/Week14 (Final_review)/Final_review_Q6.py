class stack:
    # Task 1
    def __init__(self, size):  # DO NOT modify this line
        self.capacity = size
        self.content = [None] * size
        self.tos = 0

    # Task 2
    def __str__(self):  # DO NOT modify this line
        out = '-----'
        if self.tos == self.capacity:   out += '*\n'
        else:                           out += '\n'

        for i in range(len(self.content) - 1, -1, -1):
            out += str(self.content[i])
            if i == self.tos: out += '*'
            out += '\n'
        return out + '-----'

    # Task 3
    def push(self, data):  # DO NOT modify this line
        if self.tos < self.capacity:
            self.content[self.tos] = data
            self.tos += 1
        else:
            print('ERROR: stack is full')

    # Task 4
    def pop(self):  # DO NOT modify this line
        if self.tos > 0:
            self.tos -= 1
            out = self.content[self.tos]
            self.content[self.tos] = None
            return out
        else:
            print('ERROR: stack is empty')
            return None


# Task 5
def main():
    # (1) get an integer number, n, from keyboard
    n = int(input())
    # (2) create an empty stack with capacity equal n + 1, and print the stack created
    mtst = stack(n + 1)
    # (3) get n integer numbers from keyboard one line at time each time the input is entered the data should be added to stack created in (2) print the stack after all data are added
    for _ in range(n): mtst.push(int(input()))
    print(mtst)
    # (4) remove all elements except the bottom most of the stack, and calculate the summation of removed elements and print the summation to screen
    s = 0
    for _ in range(n - 1): s += mtst.pop()
    print(s)
    # (5) print the stack properties (DO NOT use show_stack())main()
    print(mtst)


main()
