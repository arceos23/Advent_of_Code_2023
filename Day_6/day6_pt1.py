import re

# Get race records
file = open('day6_input.txt', 'r')
race_records = file.readlines()
file.close()

# Get times and distances from the race records
times = [int(time) for time in re.sub('Time:\s+', '', race_records[0]).split()]
distances = [int(distance) for distance in re.sub('Distance:\s+', '', race_records[1]).split()]

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

# Calculate the number of ways to win records across all races
won_record = False
total_ways_win_record = 1
for i in range(len(times)):
    num_ways_win_record = calc_num_ways_win_record(times[i], distances[i])
    if num_ways_win_record > 0:
        won_record = True
        total_ways_win_record *= num_ways_win_record

print(total_ways_win_record if won_record == True else 0) # My puzzle answer: 1312850