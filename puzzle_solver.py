from typing import List, Tuple, Set, Optional

"""Magic Variable's: """
WHITE = 1
BLACK = 0
UNKWON_CELL = -1

##################################
INVALID = 0
VALID = 1
MAYBE_VALID = 2


##################################


def coord_is_valid(row: int, col: int, picture: List[List[int]],
                   unknown_is_white: bool) -> bool:
    """
    this func is checking and doing validation if the coordinates are valid.
    :param row: the row of the value by index.
    :param col: the col of the value by index.
    :param picture: an 2D list that contain the data of the board.
    :param unknown_is_white: unknown Square with value if its white or black.
    :return: true if the val is white and in the right coords and false if the
    val is not right.
    """
    if row >= len(picture) or col >= len(picture[0]) or row < 0 or col < 0:
        return False

    if unknown_is_white:
        if picture[row][col] == BLACK:
            return False
    else:
        if picture[row][col] != WHITE:
            return False

    return True


def checking_the_length_of_the_possible_cells_right(row, col, picture,
                                                    unknown_is_white,
                                                    counter=0) -> int:
    """
    this func is checking how many cells the sol one can see in a single
    moment to he's right.
    :param row: the row of the cell that we check.
    :param col: the col of the cell that we check.
    :param picture: an 2D list that contain the data of the board.
    :param unknown_is_white: unknown Square with value if its white or black.
    :param counter: count how many cells there is.
    :return: the counter of how many.
    """
    if not coord_is_valid(row, col, picture, unknown_is_white):
        return counter
    return checking_the_length_of_the_possible_cells_right(row, col + 1,
                                                           picture,
                                                           unknown_is_white,
                                                           counter + 1)


def checking_the_length_of_the_possible_cells_left(row, col, picture,
                                                   unknown_is_white,
                                                   counter=0) -> int:
    """
    this func is checking how many cells the sol one can see in a single
    moment to he's left.
    :param row: the row of the cell that we check.
    :param col: the col of the cell that we check.
    :param picture: an 2D list that contain the data of the board.
    :param unknown_is_white: unknown Square with value if its white or black.
    :param counter: count how many cells there is.
    :return: the counter of how many.
    """
    if not coord_is_valid(row, col, picture, unknown_is_white):
        return counter
    return checking_the_length_of_the_possible_cells_left(row, col - 1,
                                                          picture,
                                                          unknown_is_white,
                                                          counter + 1)


def checking_the_length_of_the_possible_cells_up(row, col, picture,
                                                 unknown_is_white,
                                                 counter=0) -> int:
    """
    this func is checking how many cells the sol one can see in a single
    moment above him.
    :param row: the row of the cell that we check.
    :param col: the col of the cell that we check.
    :param picture: an 2D list that contain the data of the board.
    :param unknown_is_white: unknown Square with value if its white or black.
    :param counter: count how many cells there is.
    :return: the counter of how many.
    """
    if not coord_is_valid(row, col, picture, unknown_is_white):
        return counter
    return checking_the_length_of_the_possible_cells_up(row - 1, col, picture,
                                                        unknown_is_white,
                                                        counter + 1)


def checking_the_length_of_the_possible_cells_down(row, col, picture,
                                                   unknown_is_white,
                                                   counter=0) -> int:
    """
    this func is checking how many cells the sol one can see in a single
    moment under him.
    :param row: the row of the cell that we check.
    :param col: the col of the cell that we check.
    :param picture: an 2D list that contain the data of the board.
    :param unknown_is_white: unknown Square with value if its white or black.
    :param counter: count how many cells there is.
    :return: the counter of how many.
    """
    if not coord_is_valid(row, col, picture, unknown_is_white):
        return counter
    return checking_the_length_of_the_possible_cells_down(row + 1, col,
                                                          picture,
                                                          unknown_is_white,
                                                          counter + 1)


def seen_cells(picture: List[List[int]], row: int, col: int,
               unknown_is_white: bool) -> int:
    """
    this func is combining all the aid funcs about see a cell from a
    specific single cell.
    :param picture: an 2D list that contain the data of the board.
    :param row: the row of the cell that we check.
    :param col: the col of the cell that we check.
    :param unknown_is_white: unknown Square with value if its white or black.
    :return: the count that explain how many cells there is that are possible.
    """
    if unknown_is_white:
        if picture[row][col] == BLACK:
            return 0
    else:
        if picture[row][col] != WHITE:
            return 0

    count = 1  # original cell was white hens + 1
    count += checking_the_length_of_the_possible_cells_right(row, col + 1,
                                                             picture,
                                                             unknown_is_white)
    count += checking_the_length_of_the_possible_cells_left(row, col - 1,
                                                            picture,
                                                            unknown_is_white)
    count += checking_the_length_of_the_possible_cells_up(row - 1, col,
                                                          picture,
                                                          unknown_is_white)
    count += checking_the_length_of_the_possible_cells_down(row + 1, col,
                                                            picture,
                                                            unknown_is_white)

    return count


def max_seen_cells(picture: List[List[int]], row: int, col: int) -> int:
    """
    this func is calculating the amount of seen cells this a sol cell can see
    from a white cell to another.
    :param picture: an 2D list that contain the data of the board.
    :param row: the row of the value by index.
    :param col: the col of the value by index.
    :return: an int number that reflects the seen cells of the val.
    """
    return seen_cells(picture, row, col, True)


def min_seen_cells(picture: List[List[int]], row: int, col: int) -> int:
    """
    this func is calculating the amount of seen cells this a sol cell can see
    from a black to another.
    :param picture: an 2D list that contain the data of the board.
    :param row: the row of the value by index.
    :param col: the col of the value by index.
    :return: an int number that reflects the seen cells of the val.
    """
    return seen_cells(picture, row, col, False)


def check_constraints(picture: List[List[int]],
                      constraints_set: Set[Tuple[int, int, int]]) -> int:
    """
    this func do a validation for the constraints.
    :param picture: an 2D list that contain the data of the board.
    :param constraints_set: a set that contains all the constraints for a cell.
    :return: True or False regarding the constraints' status.
    """

    maybe_flag = False
    for constraint in constraints_set:
        constraint_status = check_one_constraint_tp(picture, constraint)
        if constraint_status is INVALID:
            return INVALID
        if constraint_status is MAYBE_VALID:
            maybe_flag = True

    if maybe_flag:
        return MAYBE_VALID
    else:
        return VALID


def check_one_constraint_tp(picture: List[List[int]],
                            constraint: Tuple[int, int, int]) -> int:
    """
    this func is doing a validation for a constraint to a single cell.
    :param picture: an 2D list that contain the data of the board.
    :param constraint: a single constraint regarding a sol cell.
    :return: True or False regarding the constraint status.
    """
    max_seen = max_seen_cells(picture, constraint[0], constraint[1])
    min_seen = min_seen_cells(picture, constraint[0], constraint[1])

    if max_seen == min_seen == constraint[2]:
        return VALID

    if max_seen >= constraint[2] >= min_seen:
        return MAYBE_VALID
    return INVALID


def find_first_unknown_cell(picture: List[List[int]]) -> Tuple[int, int]:
    """
    this func is finding the first cell that is an unknown cell out of the
    current board that is checking.
    :param picture: an 2D list that contain the data of the board.
    :return: a tuple of the first cell that is unknown about his color.
    """
    for i in range(len(picture)):
        for j in range(len(picture[0])):
            if picture[i][j] == UNKWON_CELL:
                return i, j


def _solve_puzzle_helper(picture,
                         constraints_set: Set[Tuple[int, int, int]]) -> \
Optional[List[List[int]]]:
    """
    this func is giving a solution regarding the question of solving the
    puzzle.
    :param picture: an 2D list that contain the data of the board.
    :param constraints_set: a set that contains all the constraints for a cell.
    :return: a solution if there is and None if there isn't.
    """
    if check_constraints(picture, constraints_set) == INVALID:
        return None

    if check_constraints(picture, constraints_set) == VALID:
        return picture

    row, col = find_first_unknown_cell(picture)

    black_picture = copy_pic_with_colored_cell(picture, row, col, BLACK)
    black_try = _solve_puzzle_helper(black_picture, constraints_set)
    if black_try is not None:
        return black_try

    white_picture = copy_pic_with_colored_cell(picture, row, col, WHITE)
    white_try = _solve_puzzle_helper(white_picture, constraints_set)
    if white_try is not None:
        return white_try
    return None


def create_picture(n: int, m: int) -> List[List[int]]:
    """
    this func is creating a board of -1's.
    :param n: the amount  of row's in the board.
    :param m: the amount of col's in the board.
    :return: a board fo the game full of -1.
    """
    board = []
    for row in range(n):
        board.append([])
        for col in range(m):
            board[row].append(-1)
    return board


def copy_pic_with_colored_cell(picture: List[List[int]], row: int, col: int,
                               color: int) -> Optional[List[List[int]]]:
    """
    this func is simulating a dip-copy of the picture.
    :param picture: an 2D list that contain the data of the board.
    :param row:the row of the picture.
    :param col: the col of the picture.
    :param color: the color that we chose to be for the first unknown cell.
    :return: a dip copy of the picture that is not the original one.
    """
    copy_picture = []
    for r in range(len(picture)):
        col_list = []
        for c in range(len(picture[0])):
            col_list.append(picture[r][c])
        copy_picture.append(col_list)
    copy_picture[row][col] = color
    return copy_picture


def solve_puzzle(constraints_set: Set[Tuple[int, int, int]], n: int, m: int) -> \
        Optional[List[List[int]]]:
    """

    :param constraints_set:a set that contains all the constraints
    regarding the game and the way a cell can be painted.
    :param n: the amount  of row's in the picture.
    :param m: the amount of col's in the picture.
    :return: a solved puzzle of the game.
    """
    picture = create_picture(n, m)
    return _solve_puzzle_helper(picture, constraints_set)


def how_many_unknown(picture: List[List[int]]) -> int:
    """
    this func is counting the amount of unknown cells there is ih the picture.
    :param picture: an 2D list that contain the data of the board.
    :return: the amount of unknown cells.
    """
    counter = 0
    for row in range(len(picture)):
        for item in range(len(picture[0])):
            if picture[row][item] == UNKWON_CELL:
                counter += 1
    return 2 ** counter


def _how_many_solutions_helper(picture: List[List[int]], constraints_set: Set[
    Tuple[int, int, int]]) -> int:
    """
    this func is counting the amount of solution's that there is for a pattern.
    :param picture: an 2D list that contain the data of the board.
    :param constraints_set: a set that contains all the constraints
    regarding the game and the way a cell can be painted.
    :return: an int that say how many solutions there is.
    """
    if check_constraints(picture, constraints_set) == INVALID:
        return 0

    if check_constraints(picture, constraints_set) == VALID:
        return how_many_unknown(picture)

    row, col = find_first_unknown_cell(picture)

    black_picture = copy_pic_with_colored_cell(picture, row, col, BLACK)
    black_try = _how_many_solutions_helper(black_picture, constraints_set)

    white_picture = copy_pic_with_colored_cell(picture, row, col, WHITE)
    white_try = _how_many_solutions_helper(white_picture, constraints_set)

    return black_try + white_try


def how_many_solutions(constraints_set: Set[Tuple[int, int, int]], n: int,
                       m: int) -> int:
    """
    this func is counting the amount of solutions there is for a single picture
    with different painting of the first unknown cell in Black or White.
    :param constraints_set: a set that contains all the constraints
    regarding the game and the way a player can move.
    :param n: the amount  of row's in the board.
    :param m: the amount of col's in the board.
    :return: an int that say how many solutions there is for a picture.
    """
    empty_picture = create_picture(n, m)

    return _how_many_solutions_helper(empty_picture, constraints_set)


def generate_puzzle(picture: List[List[int]]) -> Set[Tuple[int, int, int]]:
    """
    ...
    :param picture: an 2D list that contain the data of the board.
    :return:
    """
    pass


if __name__ == "__main__":
    pass
