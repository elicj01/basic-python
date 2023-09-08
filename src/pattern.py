
# Print the pattern

sequence = []

for i in range(1, 6):
    sequence.append(str("*"))
    sequence_str = ' '.join(sequence)
    print(sequence_str)

for i in range(6, 1, -1):
    sequence.pop()
    sequence_str = ' '.join(sequence)
    print(sequence_str)