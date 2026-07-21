# src/utils.py

import numpy as np

def calculate_manhattan_distance(grid, start, end):
    """
    Calculate the Manhattan distance between two points in a grid.

    This is a heuristic function used in the A\* pathfinding algorithm.
    It's not an exact distance, but a reasonable approximation.

    :param grid: The grid data structure
    :param start: The starting point as a tuple (x, y)
    :param end: The ending point as a tuple (x, y)
    :return: The Manhattan distance between the start and end points
    """
    return abs(end[0] - start[0]) + abs(end[1] - start[1])

def is_valid_move(grid, point):
    """
    Check if a move is valid in the grid.

    A move is valid if the point is within the grid boundaries
    and the point is not an obstacle.

    :param grid: The grid data structure
    :param point: The point to check as a tuple (x, y)
    :return: True if the move is valid, False otherwise
    """
    x, y = point
    rows, cols = grid.shape
    return 0 <= x < rows and 0 <= y < cols and grid[x, y] != 1  # 1 represents an obstacle

def generate_neighbors(grid, point):
    """
    Generate all possible neighboring points in the grid.

    This includes all four cardinal directions (up, down, left, right)
    and the four diagonal directions.

    :param grid: The grid data structure
    :param point: The point to generate neighbors for as a tuple (x, y)
    :return: A list of neighboring points
    """
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        x, y = point[0] + dx, point[1] + dy
        if is_valid_move(grid, (x, y)):
            neighbors.append((x, y))
    return neighbors

def reconstruct_path(came_from, current):
    """
    Reconstruct the path from the start to the end point.

    This is done by backtracking from the end point to the start point
    using the came_from dictionary.

    :param came_from: A dictionary mapping points to their predecessors
    :param current: The end point as a tuple (x, y)
    :return: A list of points representing the reconstructed path
    """
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(current)
    return path[::-1]