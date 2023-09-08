
# Print the numbers described in the exercise

sequence = []

for i in range(1, 11):
    sequence.append(str(i))
    sequence_str = ' '.join(sequence)
    print(sequence_str)

if lines and lines[-1].strip() == '':
    lines.pop()