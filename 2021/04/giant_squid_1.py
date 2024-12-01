#!/usr/bin/env python

import numpy as np
import re


class Board:
    def __init__(self):
        self.arr = np.zeros((5, 5), dtype=int)
        self.marked = np.zeros((5, 5), dtype=int)
        self.last_val = None

    def mark(self, value):
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                if self.arr[i, j] == value:
                    self.marked[i, j] = 1
        self.last_val = value

    def check_win(self):
        for row in range(len(self.marked)):
            if np.sum(self.marked[row]) == 5:
                return True
        for col in range(len(self.marked[0])):
            if np.sum(self.marked[:, col]) == 5:
                return True
        return False

    def get_score(self):
        _sum = 0
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                if self.marked[i, j] == 0:
                    _sum += self.arr[i, j]
        return _sum * self.last_val

    def __str__(self):
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'

        output = ''
        for row in range(5):
            for col in range(5):
                if self.marked[row, col] == 1:
                    if self.arr[row, col] == self.last_val:
                        output += f'{BOLD}{UNDERLINE}{self.arr[row, col]}{END} '
                    else:
                        output += f'{BOLD}{self.arr[row, col]}{END} '
                else:
                    output += f'{self.arr[row, col]} '
            output += '\n'
        output += f'Win: {self.check_win()}'
        output += '\n'

        return output


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = re.sub(' +', ' ', lines[i]).strip()
        lines.append('')
    numbers = [int(i) for i in lines[0].split(',')]

    # Load in boards
    boards = []
    board = Board()
    board_row_index = 0
    for i in range(2, len(lines)):
        if len(lines[i]) == 0:
            boards.append(board)
            board = Board()
            board_row_index = 0
        else:
            board.arr[board_row_index] = [int(j) for j in lines[i].split(' ')]
            board_row_index += 1

    # Make moves
    for number in numbers:
        for board in boards:
            board.mark(number)
            if board.check_win():
                print(board.get_score())
                quit()
