import numpy as np
from scipy.ndimage import measurements
from collections import Counter

def get_low_points(m):
    low_points = []
    low_indexes = []

    for r in range(np.shape(m)[0]):
        for n in range(np.shape(m)[1]):
            # special flow if we're in a corner
            neighbours =  []

            if n > 0:
                #left_neighbour
                neighbours.append(m[r, n-1])

            if n < np.shape(m)[0]-1:
                #right_neighbour 
                neighbours.append(m[r, n+1])

            if r > 0:
                #up_neighbour 
                neighbours.append(m[r-1, n])

            if r < np.shape(m)[0]-1:
                #down_neighbour 
                neighbours.append(m[r+1, n])

            if m[r, n] < min(neighbours):
                low_points.append(m[r, n])
                low_indexes.append((r,n))

                # now determine the basin size: how many

    return low_points, low_indexes

def get_biggest_basin_size(m):
    masked_m = [[1 if num < 9 else 0 for num in row] for row in m]
    labels, num_labels = measurements.label(list(masked_m))

    # now count how many
    labels = [a for lab in labels for a in lab]
    values =  Counter(labels).most_common(4)[1:4]
    values = [v[1] for v in values]
    return np.prod(values)

if __name__ == '__main__':
    with open('input.txt') as f:
        readings: list[str] = f.readlines()

    readings = [list(row.strip()) for row in readings]
    readings = [[int(num) for num in row] for row in readings]

    readings = np.array(readings)
    low_points, low_indexes = get_low_points(readings)

    # print out the answer to part 1
    print(np.sum(low_points) + len(low_points))

    # part 2 - what is the product of the three largest basin sizes?
    print(get_biggest_basin_size(readings))