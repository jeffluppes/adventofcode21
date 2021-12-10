# template for advent of code challenges
import numpy as np

def part1(seq: list[str],):
    pass
    #return 

def part2(commands: list[str]):
    pass
    # return

import numpy as np

if __name__ == '__main__':


    # input
    with open('input.txt') as f:
        inputs: list[str] = f.readline().split('\n')[0].split(',')

        boards: list[str] = f.read().split('\n\n')

    # process board
    boards_ds = []
    for b in boards:
        temp = np.ndarray(shape=(5,5))
        rows = b.split('\n')
        for idx, r in enumerate(rows):
            if len(r) >0:
                numbers = r.split()
                temp[idx:] = numbers
        boards_ds.append(temp)
    
    print(np.shape(boards_ds))
    #print(boards_ds)

    board_masks = np.zeros(shape=np.shape(boards_ds))
    boards_ds = np.array(boards_ds)
    has_won = list(np.zeros(100))
    for i in inputs:
        # go through all the boards and if we get a match, mark the mask with 1
        for b in range(np.shape(boards_ds)[0]):
            if not int(has_won[b]):
                for row in range(np.shape(boards_ds)[1]):
                    for index in range(np.shape(boards_ds)[2]):
                        if int(i) == int(boards_ds[b, row, index]):
                            #print(boards_ds[b, row, index])
                            board_masks[b, row, index] =  1


        # check all boards
        for idx, b in enumerate(board_masks):
            # check rows
            if not int(has_won[idx]):
                for row in range(np.shape(boards_ds)[1]):
                    if np.sum(b[row]) == 5 or np.sum(b[:,row]) == 5:
                        score = np.sum(boards_ds[idx].astype(int)) - np.sum(boards_ds[idx].astype(int)[b.astype(bool)])
                        print(f'BINGO! board: {idx} with input {i} won! Score: {score*int(i)} - There are {np.sum(has_won)} boards that have already won')
                        has_won[idx] = 1


