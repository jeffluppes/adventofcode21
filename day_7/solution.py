# template for advent of code challenges
import numpy as np


if __name__ == '__main__':
    with open('input.txt') as f:
        crab_pos: list[int] = f.read().splitlines()

    crab_pos = [int(x) for x in crab_pos[0].split(',')] # some post-processing

    # part 2 - Horizontal crab alignment - only required sum(range(abs(x-i)+1)) over abs(x-i)
    # therefore I just left this as-is and moved on to the next

    min_fuel = 0
    
    for i in range(min(crab_pos), max(crab_pos)):  
        fuel_list = [sum(range(abs(x - i)+1)) for x in crab_pos]
        if i == 0:
            min_fuel = np.sum(fuel_list)
        else:
            min_fuel = min(min_fuel,np.sum(fuel_list))

        print(f'Pos {i} - would take {np.sum(fuel_list)}')


    print(f'Lowest amount of fuel: {min_fuel}')