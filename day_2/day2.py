# Calculate the horizontal position and depth you would have after 
# following the planned course. What do you get if you multiply
# your final horizontal position by your final depth?
horizontal_moves = ['forward']
vertical_moves = ['up', 'down']


def part1(commands: list[str]):
    x = 0
    y = 0
    for c in commands:
        if c.split(' ')[0] == 'forward':
            x += int(c.split()[1])
        elif c.split()[0] == 'up':
            y -= int(c.split()[1])
        else:
            y += int(c.split()[1])
    
    # we need to calculate x*y only
    return x*y

def part2(commands: list[str]):
    x = 0
    y = 0
    aim = 0
    for c in commands:
        if c.split(' ')[0] == 'forward':
            x += int(c.split()[1])
            y += aim*int(c.split()[1])
        elif c.split()[0] == 'up':
            aim -= int(c.split()[1])
        else:
            aim += int(c.split()[1])
    
    # we need to calculate x*y only
    return x*y

if __name__ == '__main__':
    with open('input.txt') as f:
        measurements: list[str] = f.read().splitlines()

    print(part1(measurements))
    print(part2(measurements))