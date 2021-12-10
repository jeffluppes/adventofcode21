# template for advent of code challenges
from collections import Counter
from itertools import repeat

def get_total(c: Counter()):
    return sum(c.values())

if __name__ == '__main__':
    with open('example.txt') as f:
        lanternfish: list[int] = f.read().splitlines()

    initial_fish = [int(x) for x in lanternfish[0].split(',')] # some post-processing
    lanternfish = Counter({x: 0 for x in range(0,10)}) # fix initialize this with an zero dict so we can track fish
    lanternfish.update(initial_fish)

    days = 256
    for i in range(days):

        # new borns
        lanternfish[9] += lanternfish.get(0, 0)
        
        # proud new parent fish
        lanternfish[7] += lanternfish.get(0, 0)
        
        # since every lanternfish moves a day closer toward spawning we can simply replace n with the value of n+1
        lanternfish = {x: lanternfish.get(x+1, 0) for x in lanternfish}

        print(f'Day {i+1} - You have {get_total(lanternfish)} lanternfish. What could ever go wrong?')