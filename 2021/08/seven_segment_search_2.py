#!/usr/bin/env python


def count_shared(a, b):
    return sum(c in b for c in a)


def process(line):
    inputs, outputs = line.split(' | ')
    inputs = inputs.split(' ')
    outputs = outputs.split(' ')
    for i in range(len(inputs)):
        inputs[i] = ''.join(sorted(inputs[i]))
    for i in range(len(outputs)):
        outputs[i] = ''.join(sorted(outputs[i]))

    code_mapping = [[]] * 10

    ### === Get 1, 4, 7, 8 === ###
    for _input in inputs:
        if len(_input) in {2, 4, 3, 7}:
            # 1
            if len(_input) == 2:
                code_mapping[1] = _input
            # 4
            elif len(_input) == 4:
                code_mapping[4] = _input
            # 7
            elif len(_input) == 3:
                code_mapping[7] = _input
            # 8
            elif len(_input) == 7:
                code_mapping[8] = _input

    ### === Get rest === ###
    for _input in inputs:
        # 2, 3, 5
        if len(_input) == 5:
            # 3 : input shares both segments with "1"
            if count_shared(_input, code_mapping[1]) == 2:
                code_mapping[3] = _input
            # 5 : input shares 1 segment with "1" and 3 segments with "4"
            elif count_shared(_input, code_mapping[1]) == 1 and count_shared(_input, code_mapping[4]) == 3:
                code_mapping[5] = _input
            # 2
            else:
                code_mapping[2] = _input

        # 0, 6, 9
        elif len(_input) == 6:
            # 9 : input shares all segments with "4"
            if count_shared(_input, code_mapping[4]) == 4:
                code_mapping[9] = _input
            # 6 : input shares 1 segment with "1" and 3 segments with "4"
            elif count_shared(_input, code_mapping[1]) == 1 and count_shared(_input, code_mapping[4]) == 3:
                code_mapping[6] = _input
            # 0
            else:
                code_mapping[0] = _input

    ### === Determine output === ###
    code = [str(code_mapping.index(output)) for output in outputs]
    code = int(''.join(code))
    return code


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    print(sum(process(line.strip()) for line in lines))
