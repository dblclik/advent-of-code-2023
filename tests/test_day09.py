from advent_of_code_2023.helpers.sequences import reduce_deltas_to_zeroes


def test_day09_examples():
    sequences = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

    sequences = sequences.split("\n")
    sequences = [[int(val) for val in seq.split(" ")] for seq in sequences]

    extrapolated_values = []

    for seq in sequences:
        seqs = reduce_deltas_to_zeroes(seq)
        value = 0
        for ind in range(len(seqs), 0, -1):
            value += seqs[ind - 1][-1]

        extrapolated_values.append(value)

    print(sum(extrapolated_values))

    # sequences = sequences.split("\n")
    # sequences = [[int(val) for val in seq.split(" ")] for seq in sequences if len(seq) > 0]

    extrapolated_values = []

    for seq in sequences:
        seqs = reduce_deltas_to_zeroes(seq)
        value = 0
        for ind in range(len(seqs), 0, -1):
            value = seqs[ind - 1][0] - value

        extrapolated_values.append(value)

    print(sum(extrapolated_values))


def test_day09():
    sequences = open("inputs/input-09.txt").read()

    sequences = sequences.split("\n")
    sequences = [
        [int(val) for val in seq.split(" ")] for seq in sequences if len(seq) > 0
    ]

    extrapolated_values = []

    for seq in sequences:
        seqs = reduce_deltas_to_zeroes(seq)
        value = 0
        for ind in range(len(seqs), 0, -1):
            value += seqs[ind - 1][-1]

        extrapolated_values.append(value)

    print(sum(extrapolated_values))

    extrapolated_values = []

    for seq in sequences:
        seqs = reduce_deltas_to_zeroes(seq)
        value = 0
        for ind in range(len(seqs), 0, -1):
            value = seqs[ind - 1][0] - value

        extrapolated_values.append(value)

    print(sum(extrapolated_values))
