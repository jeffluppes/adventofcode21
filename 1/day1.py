# https://adventofcode.com/2021/day/1


def part1(measurements: list) -> int:
    larger_than_previous_measurements = 0 
    
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i-1]: 
            larger_than_previous_measurements +=1

    return larger_than_previous_measurements

def part2(measurements: list) -> int:
    sliding_window_values = []
    for i in range(2, len(measurements)):
        sliding_window_values.append(sum(measurements[i-3:i]))

    return part1(sliding_window_values)

if __name__ == '__main__':
    with open('input.txt') as f:
        measurements: list[str] = f.read().splitlines()

    measurements: list = [int(x) for x in measurements]
    print(f'part 1: {part1(measurements)} measurements')
    print(f'part 2: {part2(measurements)} measurements')