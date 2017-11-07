class TuringMachine:
    def __init__(self):
        self.states = []
        self.alphabet = []
        self.blank_symbol = 0
        self.halt_state = 'H'
        # 47176870 steps
        self.instructions = {'A': {0: (1, 1, 'B'), 1: (1, -1, 'C')},
                             'B': {0: (1, 1, 'C'), 1: (1, 1, 'B')},
                             'C': {0: (1, 1, 'D'), 1: (0, -1, 'E')},
                             'D': {0: (1, -1, 'A'), 1: (1, -1, 'D')},
                             'E': {0: (1, 1, "H"), 1: (0, -1, 'A')}
                             }

        self.tape = Tape(self.blank_symbol)
        self.state = 'A'

    def step(self):
        current_symbol = self.tape.read()
        write, direction, state = self.instructions[self.state][current_symbol]
        self.tape.write(write)
        self.state = state
        self.tape.shift(direction)

    def run(self):
        steps = 0
        while self.state is not self.halt_state:
            print(steps)
            # print(steps, self.state)
            # print(self.tape, '\n')
            self.step()
            steps += 1
        print(steps)


class Tape:
    def __init__(self, blank_symbol):
        self.blank_symbol = blank_symbol
        self.left = []      # (-infinity, -1]   in reverse order
        self.right = [blank_symbol]     # [0, infinity)
        self.head_pos = 0

    def read(self):
        if self.head_pos < 0:
            return self.left[abs(self.head_pos) - 1]
        else:
            return self.right[self.head_pos]

    def write(self, symbol):
        if self.head_pos < 0:
            self.left[abs(self.head_pos) - 1] = symbol
        else:
            self.right[self.head_pos] = symbol

    def shift(self, direction):
        self.head_pos += direction
        # Extend tape as needed
        if self.head_pos < 0:
            if abs(self.head_pos) > len(self.left):
                self.left.append(self.blank_symbol)
        else:
            if self.head_pos > len(self.right) - 1:
                self.right.append(self.blank_symbol)

    def __repr__(self):
        return ' '.join(str(n) for n in self.left + self.right) + '\n' + \
            ' ' * 2 * (len(self.left) + self.head_pos) + '^'


if __name__ == '__main__':
    tm = TuringMachine()
    tm.run()
