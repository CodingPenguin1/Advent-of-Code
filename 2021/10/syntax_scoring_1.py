#!/usr/bin/env python

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    score = 0
    for line in lines:
        stack = []
        corrupt = False
        print(line)
        for char in line:
            if char in {'{', '[', '(', '<'}:
                stack.append(char)
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '>' and stack[-1] == '<':
                stack.pop()
            else:
                corrupt = char
                break

        if stack and not corrupt:
            print('Incomplete line\n')
        if corrupt:
            print(f'Corrupt: {char}\n')
            scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
            score += scores[corrupt]

    print(score)
