import numpy as np
import random
from cell_handler import Cell


class Map:
    def __init__(self, width, height, game_session):
        self.game_session = game_session
        self.width = width
        self.height = height
        self.matrix = self.build_matrix(width, height)
        self.board = self.build_board(self.matrix.tolist())


    def update_cells(self):
        upper_i = 0
        for row in self.board:
            lower_i = 0
            for _ in row:
                cell = self.board[upper_i][lower_i]
                self.game_session.window.blit(cell.image, (cell.x_pos, cell.y_pos))
                lower_i += 1
            upper_i += 1


    def build_board(self, nested_list):

        temp = np.zeros((self.width, self.height))
        new_board = temp.tolist()
        upper_i = 0
        for row in nested_list:
            lower_i = 0
            for _ in row:
                x_pos = (upper_i * 70 + 8)*self.game_session.sprites_scale
                y_pos = (lower_i * 70 + 250)*self.game_session.sprites_scale
                temp_cell = Cell(upper_i, lower_i, nested_list[upper_i][lower_i], x_pos, y_pos, self.game_session)
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
                temp = random.randint(0, 5)
                if temp == 1:
                    matrix_array[upper_i][lower_i] = -1
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
