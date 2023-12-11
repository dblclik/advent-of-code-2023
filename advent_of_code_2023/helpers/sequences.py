from typing import List


def reduce_deltas_to_zeroes(input_sequence: List[int]):
    sequences = []
    sequences.append(input_sequence)
    while not all([s == 0 for s in sequences[-1]]):
        next_sequence = [
            sequences[-1][ind + 1] - sequences[-1][ind]
            for ind in range(len(sequences[-1]) - 1)
        ]
        sequences.append(next_sequence)

    return sequences
