import numpy as np
import random
from cell_handler import Cell
import pygame
from queue import Queue


class Map:
    def __init__(self, width, height, game_session):
        self.game_session = game_session
        self.width = width
        self.height = height
        self.matrix = self.build_matrix(width, height)
        self.board = self.build_board(self.matrix.tolist())

    def update_cells(self):
        """
        The update_cells function iterates through the board and blits each cell's image to the screen.
        It does this by first setting upper_i equal to 0, which will be used as an index for row in self.board.
        Then it sets lower_i equal to 0, which will be used as an index for _ in row.

        :param self: Access the class attributes
        :return: The board object
        :doc-author: Trelent
        """
        upper_i = 0
        for row in self.board:
            lower_i = 0
            for _ in row:
                cell = self.board[upper_i][lower_i]
                self.game_session.window.blit(cell.image, (cell.x_pos, cell.y_pos))
                lower_i += 1
            upper_i += 1

    def build_board(self, nested_list):
        """
        The build_board function takes a nested list of strings and creates a new board
        with the appropriate cells. The function iterates through the nested list, creating
        a cell for each element in the nested list. The x_pos and y_pos are calculated by multiplying
        the row number by 70 (width of one cell) plus 8 (for padding). Each cell is then added to
        the board.

        :param self: Access the variables and methods of the class in which it is used
        :param nested_list: Create the board
        :return: A list of lists that contains cell objects
        :doc-author: Trelent
        """
        temp = np.zeros((self.width, self.height))
        new_board = temp.tolist()
        upper_i = 0
        for row in nested_list:
            lower_i = 0
            for _ in row:
                x_pos = (upper_i * 70 + 8)
                y_pos = (lower_i * 70 + 250)
                temp_cell = Cell(upper_i, lower_i, nested_list[lower_i][upper_i], x_pos, y_pos, self.game_session)
                new_board[upper_i][lower_i] = temp_cell
                lower_i += 1
            upper_i += 1
        return new_board

    def fill_map_with_mines(self, matrix_array):
        """
        The fill_map_with_mines function takes a matrix as an argument and fills the matrix with mines
        at random locations.The function returns nothing.

        :param: matrix: Fill the matrix with mines
        :return: The matrix with the mines placed
        :doc-author: Trelent
        """

        upper_i = 0
        for row in matrix_array:
            lower_i = 0
            for _ in row:
                temp = random.randint(0, 7)
                if temp == 1:
                    matrix_array[upper_i][lower_i] = -1
                    self.game_session.number_of_mines += 1
                lower_i += 1
            upper_i += 1

    def get_adjacent_cords(self, matrix, position):
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

    def get_cell_position(self, xy_tuple):
        """
        The get_cell_position function takes a tuple of coordinates and returns the position of that cell in the matrix.
        The function iterates through each row in the matrix, then iterates through each cell within that row.
        If it finds a cell with a rect attribute containing xy_tuple, it returns its position as an (x, y) tuple.

        :param self: Access the class attributes
        :param xy_tuple: Get the coordinates of a mouse click
        :return: The position of the cell in the matrix that contains a given point
        :doc-author: Trelent
        """
        upper_i = 0
        for row in self.board:
            lower_i = 0
            for _ in row:
                cell = self.board[upper_i][lower_i]
                if pygame.Rect.collidepoint(cell.rect, xy_tuple):
                    return upper_i, lower_i
                lower_i += 1
            upper_i += 1

    def flood_fill_BFS(self, array, y, x):
        """
        The flood_fill function takes a 2D array and two integers, y and x. It then
        checks if the value at that point is equal to the current_value. If it is, it
        then checks if any of its neighbors are also equal to the current_value. If they
        are not, then nothing happens; however, if they are equal to the current value, 
        then all of their neighbors will be checked as well in a recursive fashion.
        
        :param self: Refer to the object itself
        :param array: Store the gameboard
        :param y: Specify the row of the array that is being checked
        :param x: Determine the column of the array that is being accessed
        :return: The updated array
        :doc-author: Trelent
        """
        height = len(array)
        width = len(array[0])

        queue = Queue()
        queue.put((y, x))  # The next class period I'm gonna miss the pre-built data structures :(
        while not queue.empty():
            y, x = queue.get()
            if y < 0 or y >= height or x < 0 or x >= width or array[y][x].number != 0 or array[y][x].is_expose == True:
                continue
            else:
                array[y][x].update_sprite()
                queue.put((y + 1, x))
                queue.put((y - 1, x))
                queue.put((y, x + 1))
                queue.put((y, x - 1))
        self.game_session.number_of_clicks += 1

    def show_cell(self, upper_i, lower_i):
        """
        The show_cell function takes two integers as arguments, an upper_i and a lower_i.
        It then updates the sprite of the cell at that location on the board.

        :param self: Access the attributes and methods of the class in python
        :param upper_i: Select the row of the cell that is to be updated
        :param lower_i: Determine which cell is being updated
        :return: The cell object of the upper_i and lower_i index
        :doc-author: Trelent
        """
        print(upper_i, lower_i)
        self.game_session.number_of_clicks += 1
        self.board[upper_i][lower_i].update_sprite()

    def handle_click(self, upper_i, lower_i):
        if self.game_session.number_of_clicks != 0:
            self.show_cell(upper_i, lower_i)

    def check_for_sourrondedd_mines(self):

        upper_i = 0
        for row in self.matrix:
            lower_i = 0
            for _ in row:

                if self.matrix[upper_i][lower_i] == -1:
                    adjacent_cell_index_list = self.get_adjacent_cords(self.matrix, [upper_i, lower_i])
                    required_number_of_exposed_cells = len(adjacent_cell_index_list)
                    temp = []
                    upper_i_inside = 0
                    for i in adjacent_cell_index_list:
                        lower_i_inside = 0
                        for j in i:
                            if self.board[upper_i_inside][lower_i_inside].is_expose or self.board[upper_i_inside][lower_i_inside].number == -1:
                                temp.append(1)
                            lower_i_inside += 1
                        upper_i_inside += 1
                    if sum(temp) == required_number_of_exposed_cells:
                        self.board[upper_i][lower_i].flag()
                lower_i += 1
            upper_i += 1

    def check_adjacent_cells_for_mines(self, matrix, lower_i, upper_i):
        """
        The check_adjacent_cells function takes a matrix and two indices as input.
        It then finds all the cells that are adjacent to the cell at those indices,
        and counts how many of them contain mines. It returns this count
        :param matrix: Access the cells in the matrix
        :param lower_i: Find the lower index of the cell that is being checked
        :param upper_i: Check the cells above the cell in question
        :return: The number of mines in the adjacent cells
        :doc-author: Trelent
        """

        adjacent_cell_index_list = self.get_adjacent_cords(matrix, [lower_i, upper_i])
        list_of_mines = []
        for cell_cords in adjacent_cell_index_list:
            if matrix[cell_cords[0]][cell_cords[1]] == -1:
                list_of_mines.append(1)
            else:
                list_of_mines.append(0)
        return sum(list_of_mines)

    def add_numbers(self, matrix):

        """

        The add_numbers function adds the numbers of adjacent cells to a cell.
        The function starts at the upper left corner and moves through each row, adding
        the numbers of adjacent cells to each cell in that row. The function then moves
        down one row and repeats this process until it has reached the lower right corner.

        :param: matrix Store the matrix that is to be checked for adjacent cells
        :return: The matrix with the values of the adjacent cells added to each cell
        :doc-author: Trelent
        """

        upper_i = 0
        for row in matrix:
            lower_i = 0
            for _ in row:

                if matrix[upper_i][lower_i] != -1:
                    matrix[upper_i][lower_i] = self.check_adjacent_cells_for_mines(matrix, upper_i, lower_i)
                lower_i += 1
            upper_i += 1

    def add_patch_of_zeros(self, matrix, center_cords):
        patch = [center_cords]
        base = self.get_adjacent_cords(matrix, [center_cords[1], center_cords[0]])
        patch.extend(base)
        for cords in base:
            random_value = random.randint(len(patch))
            if random_value == 1:
                branch = self.get_adjacent_cords(matrix, [cords[0], cords[1]])
                base.extend(branch)

        upper_i = 0
        for row in matrix:
            lower_i = 0
            for _ in row:
                temp = [upper_i, lower_i]

                if temp in patch:
                    if matrix[upper_i][lower_i] == -1 and self.game_session.number_of_mines != 0:
                        self.game_session.number_of_mines -= 1
                    matrix[upper_i][lower_i] = 0

                lower_i += 1
            upper_i += 1

    def build_matrix(self, width, height):
        """
        The build_matrix function creates a matrix of zeros with the dimensions specified by width and height.
        It then fills this matrix with mines at random locations, and adds numbers to the cells adjacent to mines.
        The function returns a numpy array.

        :param self: Access the class attributes
        :param width: Determine the width of the matrix
        :param height: Create a matrix with the specified height
        :return: A matrix_array of the specified width and height
        :doc-author: Trelent
        """

        matrix_array = np.zeros((width, height))
        self.fill_map_with_mines(matrix_array)
        self.add_numbers(matrix_array)
        return matrix_array
