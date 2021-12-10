# template for advent of code challenges
import scipy.misc
import numpy as np
from skimage.draw import line

if __name__ == '__main__':


    # input
    with open('input.txt') as f:
        input: list[str] = f.read().splitlines()

    # parse commands
    commands = []
    for i in input:
        temp = {}
        i = i.replace(' -> ', ',')
        temp['from_x'], temp['from_y'], temp['to_x'], temp['to_y'] = [int(x) for x in i.split(',')]

        commands.append(temp)

    # part 1
    vent_map = np.zeros(shape=(1000,1000))
    for c in commands:
        if c['from_x'] == c['to_x'] or c['from_y'] == c['to_y']:
            rr, cc= line(c['from_x'], c['from_y'], c['to_x'], c['to_y'])
            vent_map[rr, cc] += 1

    print(np.count_nonzero(vent_map > 1))

    # part 2
    vent_map = np.zeros(shape=(1000,1000))
    for c in commands:
        rr, cc= line(c['from_x'], c['from_y'], c['to_x'], c['to_y'])
        vent_map[rr, cc] += 1

    print(np.count_nonzero(vent_map > 1))