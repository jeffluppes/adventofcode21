# https://adventofcode.com/2021/day/1

with open('input.txt') as f:
    lines = f.read().splitlines()

print(f'{len(lines)} lines in sample')

# start at 1 because the first number is always an increase as it starts the measurements
larger_than_previous_measurements = 1

for i in range(1, len(lines)):
    if lines[i] >= lines[i-1]:
        larger_than_previous_measurements +=1

print(f'There are {larger_than_previous_measurements} measurements that are larger than the previous measurement')

# part 2: sliding window for 3 measurements 
sliding_window_values = []
num_measurements = 3

lines = [int(x) for x in lines]


for i in range(num_measurements-1, len(lines)):
    threedaysum = lines[i]+lines[i-1]+lines[i-2]
    sliding_window_values.append(threedaysum)


larger_than_previous_measurements =0
for i in range(1, len(sliding_window_values)):
    if sliding_window_values[i] > sliding_window_values[i-1]:
        larger_than_previous_measurements +=1

print(sliding_window_values[0:10])
print(f'There are {larger_than_previous_measurements} 3-day measurements that are larger than the previous measurement')