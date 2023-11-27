#!/usr/bin/python3
# """Module containing a function that solves the N queens puzzle"""

# import sys


# def init_board(n):
#     """Initialize an `n`x`n` sized chessboard with 0's"""
#     board = []
#     [board.append([]) for i in range(n)]
#     [row.append(' ') for i in range(n) for row in board]
#     return (board)


# def board_copy(board):
#     """Return a deepcopy of the chessboard"""
#     if isinstance(board, list):
#         return list(map(board_copy, board))
#     return board


# def get_solution(board):
#     """Return the list of lists representation of a solved chessboard"""
#     solution = []
#     for row in range(len(board)):
#         for column in range(len(board)):
#             if board[row][column] == "Q":
#                 solution.append([row, column])
#                 break
#     return solution


# def xout(board, row, col):
#     """X out spots on a chessboard.
#         All spots where non-attacking queens can no
#         longer be played are X-ed out.
#     Args:
#         board (list): The current working chessboard.
#         row (int): The row where a queen was last played.
#         col (int): The column where a queen was last played.
#     """
#     # X out all forward spots
#     for c in range(col + 1, len(board)):
#         board[row][c] = "x"
#     # X out all backwards spots
#     for c in range(col - 1, -1, -1):
#         board[row][c] = "x"
#     # X out all spots below
#     for r in range(row + 1, len(board)):
#         board[r][col] = "x"
#     # X out all spots above
#     for r in range(row - 1, -1, -1):
#         board[r][col] = "x"
#     # X out all spots diagonally down to the right
#     c = col + 1
#     for r in range(row + 1, len(board)):
#         if c >= len(board):
#             break
#         board[r][c] = "x"
#         c += 1
#     # X out all spots diagonally up to the left
#     c = col - 1
#     for r in range(row - 1, -1, -1):
#         if c < 0:
#             break
#         board[r][c] = "x"
#         c -= 1
#     # X out all spots diagonally up to the right
#     c = col + 1
#     for r in range(row - 1, -1, -1):
#         if c >= len(board):
#             break
#         board[r][c] = "x"
#         c += 1
#     # X out all spots diagonally down to the left
#     c = col - 1
#     for r in range(row + 1, len(board)):
#         if c < 0:
#             break
#         board[r][c] = "x"
#         c -= 1


# def recursive_solve(board, row, queens, solutions):
#     """Recursively solve an N-queens puzzle.
#     Args:
#         board (list): The current working chessboard.
#         row (int): The current working row.
#         queens (int): The current number of placed queens.
#         solutions (list): A list of lists of solutions.
#     Returns:
#         solutions
#     """
#     if queens == len(board):
#         solutions.append(get_solution(board))
#         return (solutions)

#     for c in range(len(board)):
#         if board[row][c] == " ":
#             tmp_board = board_copy(board)
#             tmp_board[row][c] = "Q"
#             xout(tmp_board, row, c)
#             solutions = recursive_solve(tmp_board, row + 1,
#                                           queens + 1, solutions)

#     return (solutions)


# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: nqueens N")
#         sys.exit(1)
#     if sys.argv[1].isdigit() is False:
#         print("N must be a number")
#         sys.exit(1)
#     if int(sys.argv[1]) < 4:
#         print("N must be at least 4")
#         sys.exit(1)

#     board = init_board(int(sys.argv[1]))
#     solutions = recursive_solve(board, 0, 0, [])
#     for sol in solutions:
#         print(sol)

"""

This module contains an algorithm that resolves the N-Queen puzzle
using backtracking

"""


def isSafe(m_queen, nqueen):
    """ Method that determines if the queens can or can't kill each other

    Args:
        m_queen: array that has the queens positions
        nqueen: queen number

    Returns:
        True: when queens can't kill each other
        False: when some of the queens can kill

    """

    for i in range(nqueen):

        if m_queen[i] == m_queen[nqueen]:
            return False

        if abs(m_queen[i] - m_queen[nqueen]) == abs(i - nqueen):
            return False

    return True


def print_result(m_queen, nqueen):
    """ Method that prints the list with the Queens positions

    Args:
        m_queen: array that has the queens positions
        nqueen: queen number

    """

    res = []

    for i in range(nqueen):
        res.append([i, m_queen[i]])

    print(res)


def Queen(m_queen, nqueen):
    """ Recursive function that executes the Backtracking algorithm

    Args:
        m_queen: array that has the queens positions
        nqueen: queen number

    """

    if nqueen is len(m_queen):
        print_result(m_queen, nqueen)
        return

    m_queen[nqueen] = -1

    while((m_queen[nqueen] < len(m_queen) - 1)):

        m_queen[nqueen] += 1

        if isSafe(m_queen, nqueen) is True:

            if nqueen is not len(m_queen):
                Queen(m_queen, nqueen + 1)


def solveNQueen(size):
    """ Function that invokes the Backtracking algorithm

    Args:
        size: size of the chessboard

    """

    m_queen = [-1 for i in range(size)]

    Queen(m_queen, 0)


if __name__ == '__main__':

    import sys

    if len(sys.argv) == 1 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solveNQueen(size)
