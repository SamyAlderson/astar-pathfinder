import unittest
import numpy as np
from src.utils import calculate_manhattan_distance

class TestAStar(unittest.TestCase):

    def test_no_path(self):
        grid = np.array([
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ])
        start = (0, 0)
        goal = (4, 4)
        # this was tricky, we need to find a path that doesn't exist
        with self.assertRaises(ValueError):
            self.astar_search(grid, start, goal)

    def test_simple_path(self):
        grid = np.array([
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ])
        start = (0, 0)
        goal = (4, 4)
        path = self.astar_search(grid, start, goal)
        self.assertEqual(path, [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
                                (4, 1), (4, 2), (4, 3), (4, 4)])

    def test_diagonal_path(self):
        grid = np.array([
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ])
        start = (0, 0)
        goal = (4, 4)
        path = self.astar_search(grid, start, goal, allow_diagonals=True)
        self.assertEqual(path, [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)])

    def astar_search(self, grid, start, goal, allow_diagonals=False):
        """
        Perform an A* search on the grid to find the shortest path from start to goal.
        """
        # not proud of this but it works
        if start == goal:
            return [start]

        # convert grid to coordinates
        x, y = np.where(grid == 0)
        coordinates = list(zip(x, y))

        # calculate Manhattan distance heuristic
        h = calculate_manhattan_distance(start, goal)

        # initialize priority queue with start node
        queue = [(0, start, [])]
        visited = set()

        while queue:
            # select node with lowest f value
            f, current, path = min(queue)
            queue.remove((f, current, path))

            # if we've already visited this node, skip it
            if current in visited:
                continue

            # mark node as visited
            visited.add(current)

            # if we've reached the goal, return the path
            if current == goal:
                return path + [current]

            # generate neighbors
            neighbors = []
            if allow_diagonals:
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                    nx, ny = current[0] + dx, current[1] + dy
                    if (nx, ny) in coordinates:
                        neighbors.append((nx, ny))
            else:
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = current[0] + dx, current[1] + dy
                    if (nx, ny) in coordinates:
                        neighbors.append((nx, ny))

            # calculate g and h values for each neighbor
            for neighbor in neighbors:
                g = len(path) + 1
                h_n = calculate_manhattan_distance(neighbor, goal)
                f_n = g + h_n

                # add neighbor to queue
                queue.append((f_n, neighbor, path + [current]))

        # if we've reached this point, there is no path to the goal
        raise ValueError("No path found")

if __name__ == '__main__':
    unittest.main()