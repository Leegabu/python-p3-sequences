#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = []
    if length <=0:
        print(sequence)
    elif length == 1:
        sequence.append(0)
        print(sequence)
    else:
        sequence.append(0)
        sequence.append(1)
        for i in range(2,length):
            sequence.append(sequence[i -1] + sequence[i - 2])
        print(sequence[:length])
    pass