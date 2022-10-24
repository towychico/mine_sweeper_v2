from queue import Queue

import  numpy as np
import random
#matrix = np.ones((12, 7), dtype=np.int32)
#print(matrix)
#matrix2 = np.ones((5, 5), dtype=np.int32)
#print(matrix2)
#print(matrix.shape[1])

#seed_v = 20
#rand_n = np.random.default_rng(seed = seed_v)
#noice = rand_n.integers(0,2,(5,5))
#print(noice)

def get_adjacent_cords( matrix, position):
    """
    The get_adjacent_cords function takes a matrix and a position as input.
    It returns the coordinates of all adjacent cells to the one given in the position argument.
    The function checks for out of bounds errors and does not return any values that are equal to 0.

    :param self: Reference the object of the class
    :param matrix:  2D numpy array
    :param position: Python list, fist element is the x position,second element is the y position
    :return: A list of all the adjacent cells cords
    :doc-author: Trelent, Lou
    """
    adjacent_index_list = []
    for row in range(-1, 2):
        for column in range(-1, 2):
            range_x = range(0, matrix.shape[0])  # X map bounds
            range_y = range(0, matrix.shape[1])  # Y map bounds
            # new_x and new_y are going to be the cell that we want to check and all the adjacent cells
            (new_x, new_y) = (position[0] + row, position[1] + column)  # current cell
            # here we check if the current cell is not out of range and is not the original cell
            if (new_x in range_x) and (new_y in range_y) and (row, column) != (0, 0):
                adjacent_index_list.append([new_x, new_y])

    return adjacent_index_list
#
#
#def crate_stain():
#    size = 5
#    matrix = np.ones((size, size), dtype=np.int32)
#    for row in range(0, matrix.shape[0],-1):
#        for col in row:
#            if random.randint(0, 1) == 0:
#                matrix[row][col] = 0
#initial_p = [4,5]
#for i in range(random.randint(6)):
#    adjecent = get_adjacent_cords(matrix, initial_p)
#    for j in range(random.randint(4)):
#        adject_branch = get_adjacent_cords()

testM = [[0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 1, 1, 0, 0, 0]
         ]
def BFS_flood_fill(matrix,cords,value = 0):
    x = cords[0]
    y = cords[1]
    current_data = matrix[x][y]
    x_dimension = matrix.shape[1]

    y_dimension = matrix.shape[0]
    queue = Queue()
    queue.put((x, y))
    while not queue.empty():
        x, y = queue.get()
        if x < 0 or x >= x_dimension or y <0 or y >= y_dimension or matrix[x][y] != current_data:
            continue
        else:
            matrix[x][y] = value
            queue.put((x+1, y))
            queue.put((x-1, y))
            queue.put((x, y+1))
            queue.put((x, y-1))

def flood_fill(array,y,x,desired_value):
    height = len(array)
    width = len(array[0])
    current_value = 0
    queue = Queue()
    queue.put((y, x))
    while not queue.empty():
        y, x = queue.get()
        if y < 0 or y >= height or x < 0 or x >= width or array[y][x] != current_value:
            continue
        else:
            array[y][x] = desired_value
            queue.put((y+1, x))
            queue.put((y-1, x))
            queue.put((y, x+1))
            queue.put((y, x-1))

def debug_print(nested_list):
    for row in nested_list:
        print(row, sep='\n')

debug_print(testM)
flood_fill(testM,4,4,8)
print('\n')
debug_print(testM)