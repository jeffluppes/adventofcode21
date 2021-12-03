import numpy as np

def part1(measurements):
    gamma = '' # using string because the first might be zero
    for i in range(len(measurements[0])): 
        m = [x[i:] for x in measurements]

        gamma_bit = find_majority_bit(m)
        gamma += gamma_bit

    return gamma, flip_bits(gamma)

def flip_bits(s: str):
    return ''.join('1' if x == '0' else '0' for x in s)

def find_majority_bit(m):
    m = [int(x[0]) for x in m]
    print(np.sum(m))
    if np.sum(m) > (len(m)/2):
        return '1'
    else:
        return '0'

def part2(m,e, mode):
    print(e)
    filter = list(e)
    candidates = m
    i = 0
    offset = 0
    while len(candidates) != 1:
        new_candidates = []
        
        # reset e if we need and move to the next bit
        if i > len(e):
            i = 0
            offset +=1

        majority_bit = find_majority_bit_mode(candidates, i, mode)
        for c in candidates:
            if c[i+offset] == majority_bit:
                new_candidates.append(c)

        candidates = new_candidates
        i+=1

        print(f'iteration {i} done, {len(candidates)} remain {candidates[:3]}')

    return int(candidates[0], 2)

def find_majority_bit_mode(m,i, mode):
    m = [int(x[i]) for x in m]

    if mode == 'ox':
        if np.sum(m) >= (len(m)/2):
            return '1'
        else:
            return '0'
    else:
        if np.sum(m) >= (len(m)/2):
            return '0'
        else:
            return '1'  


if __name__ == '__main__':
    with open('input.txt') as f:
        measurements: list[str] = f.read().splitlines()

    g, e = part1(measurements)
    print(f'Power consumption is {int(g,2)} multiplied by {int(e,2)} or rather {int(g,2)*int(e, 2)}')
    ox_rating = part2(measurements, g, 'ox')
    co2_rating = part2(measurements, e, 'co2')
    print(f'life support is ox rating {ox_rating} multiplied by co2 rating {co2_rating} or rather {ox_rating*co2_rating}')