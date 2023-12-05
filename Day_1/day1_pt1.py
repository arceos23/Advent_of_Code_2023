file = open('day1_input.txt', 'r')
calibration_doc = file.readlines()
file.close()

calibration_value_sum = 0
for line in calibration_doc:
    # Find first digit of calibration value
    left = 0
    while not line[left].isnumeric():
        left += 1
    calibration_value = int(line[left])

    calibration_value *= 10

    # Find last digit of calibration value
    right = len(line) - 1
    while not line[right].isnumeric():
        right -= 1
    calibration_value += int(line[right])

    # Update running total for current line's calibration value
    calibration_value_sum += calibration_value

print(calibration_value_sum) # My puzzle answer: 55002