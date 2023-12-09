# Get historical data
file = open('day9_input.txt', 'r')
histories = file.readlines()
file.close()

# Find the predicted values for each history
predicted_values = [0] * len(histories)
for i, history in enumerate(histories):
    # Find the parts of the predicted value for the current history
    history = [int(val) for val in history.split()]
    sequences = [history]
    zero_diff = False
    while not zero_diff:
        zero_diff = True
        sequence = []
        for j in range(1, len(history)):
            diff = history[j] - history[j - 1]
            if diff != 0:
                zero_diff = False
            sequence.append(diff)
        sequences.append(sequence.copy())
        history = sequence

    # Calculate the predicted value based on the sequences found
    predicted_value = 0
    for sequence in sequences:
        predicted_value += sequence[-1]
    predicted_values[i] = predicted_value

print(sum(predicted_values)) # My puzzle answer: 1641934234