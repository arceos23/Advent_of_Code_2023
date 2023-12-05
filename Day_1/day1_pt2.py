file = open('day1_input.txt', 'r')
calibration_doc = file.readlines()
file.close()

DIGIT_WORD_TO_VAL = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 
                     'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

calibration_value_sum = 0
for line in calibration_doc:
    # Find first representation of digit of calibration value
    calibration_value = 0
    left_digit_found = False
    left = 0
    while not left_digit_found:
        # Check if value at the current index is a digit
        if line[left].isnumeric():
            calibration_value = int(line[left])
            break

        # Check if a digit word begins at the current index
        for digit_word in DIGIT_WORD_TO_VAL.keys():
            if left + len(digit_word) < len(line) and line[left : left + len(digit_word)] == digit_word:
                calibration_value = DIGIT_WORD_TO_VAL[digit_word]
                left_digit_found = True

        left += 1

    calibration_value *= 10

    # Find last representation of digit of calibration value
    right_digit_found = False
    right = len(line) - 1
    while not right_digit_found:
        # Check if value at the current index is a digit
        if line[right].isnumeric():
            calibration_value += int(line[right])
            break

        # Check if a digit word begins at the current index
        for digit_word in DIGIT_WORD_TO_VAL.keys():
            if right + len(digit_word) < len(line) and line[right : right + len(digit_word)] == digit_word:
                calibration_value += DIGIT_WORD_TO_VAL[digit_word]
                right_digit_found = True

        right -= 1

    # Update running total for current line's calibration value
    calibration_value_sum += calibration_value

print(calibration_value_sum) # My puzzle answer: 55093