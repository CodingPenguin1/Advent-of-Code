#!/usr/bin/env python

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    incomplete_lines = []
    for line in lines:
        stack = []
        corrupt = False
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

        if not corrupt:
            incomplete_lines.append(line)

    char_scores = {'(': 1, '[': 2, '{': 3, '<': 4}
    scores = []
    for line in incomplete_lines:
        last_clean = line
        while True:
            cleaned = last_clean.replace('()', '').replace('<>', '').replace('{}', '').replace('[]', '')
            if cleaned == last_clean:
                break
            else:
                last_clean = cleaned

        score = 0
        for char in cleaned[::-1]:
            score *= 5
            score += char_scores[char]
        scores.append(score)

    scores.sort()
    print(scores[int(len(scores) / 2)])
