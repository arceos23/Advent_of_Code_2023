import re

# Get race records
file = open('day6_input.txt', 'r')
race_record = file.readlines()
file.close()

# Get time and distance of race record
time = int(''.join((re.sub('Time:\s+', '', race_record[0]).split())))
distance = int(''.join((re.sub('Distance:\s+', '', race_record[1]).split())))

# Calculates the number of ways to win a record based on different boat charging times
def calc_num_ways_win_record(race_time, dis_record):
    # Find smallest charge time to win record
    min_charging_time = None
    for charging_time in range(1, race_time):
        time_travelling = race_time - charging_time
        dis_travelled = time_travelling * charging_time # Charging time = speed travelled
        if dis_travelled > dis_record:
            min_charging_time = charging_time
            break

    # Find largest charge time to win record
    max_charging_time = None
    for charging_time in range(race_time - 1, -1, -1):
        time_travelling = race_time - charging_time
        dis_travelled = time_travelling * charging_time # Charging time = speed travelled
        if dis_travelled > dis_record:
            max_charging_time = charging_time
            break

    return max_charging_time - min_charging_time + 1

# Calculate the number of ways to win the record for the race
total_ways_win_record = calc_num_ways_win_record(time, distance)

print(total_ways_win_record) # My puzzle answer: 36749103