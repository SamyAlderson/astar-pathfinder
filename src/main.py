# src/main.py
"""
Main entry point for the A* pathfinder.
"""

import numpy as np
from astar_pathfinder import AStarPathfinder, Heuristic

def main():
    # Create a sample 2D grid
    grid = np.array([
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ])

    # Create an instance of the AStarPathfinder class
    pathfinder = AStarPathfinder(grid, Heuristic.MANHATTAN)

    # Define the starting and ending points
    start = (0, 0)
    end = (4, 4)

    # Run the A* algorithm to find the shortest path
    try:
        path = pathfinder.find_path(start, end)
        print("Shortest path:", path)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

```python
# src/utils.py
"""
Utility functions for grid manipulation and heuristic calculations.
"""

import numpy as np

class Heuristic:
    class MANHATTAN:
        @staticmethod
        def calculate_distance(point1, point2):
            """Calculate the Manhattan distance between two points."""
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    class DIAGONAL:
        @staticmethod
        def calculate_distance(point1, point2):
            """Calculate the diagonal distance between two points."""
            return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
```

```python
# src/astar_pathfinder.py
"""
Implementation of the A* pathfinding algorithm.
"""

import numpy as np
from .utils import Heuristic

class AStarPathfinder:
    def __init__(self, grid, heuristic):
        self.grid = np.array(grid)
        self.heuristic = heuristic

    def find_path(self, start, end):
        """Find the shortest path from the start point to the end point using the A* algorithm."""
        # Create a priority queue to hold the nodes to be processed
        queue = [(0, start)]

        # Create a set to keep track of the visited nodes
        visited = set()

        while queue:
            # Get the node with the lowest priority (i.e., the node with the shortest estimated total cost)
            _, current_node = min(queue)

            # If the current node is the end node, return the path
            if current_node == end:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = self.get_previous_node(current_node)
                return path[::-1]

            # Mark the current node as visited
            visited.add(current_node)

            # Get the neighbors of the current node
            neighbors = self.get_neighbors(current_node)

            # Add the neighbors to the queue if they have not been visited before
            for neighbor in neighbors:
                if neighbor not in visited:
                    estimated_total_cost = self.heuristic.calculate_distance(current_node, end) + self.grid[neighbor[0], neighbor[1]]
                    queue.append((estimated_total_cost, neighbor))

        # If no path is found, raise an error
        raise ValueError("No path found")

    def get_neighbors(self, node):
        """Get the neighbors of a node."""
        neighbors = []
        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if self.grid[i, j] == 0 and (i, j) != node:
                    neighbors.append((i, j))
        return neighbors

    def get_previous_node(self, node):
        """Get the previous node in the path."""
        # This is a placeholder for the actual implementation
        # This was tricky to implement correctly
        return None
```

```python
# test/test_astar.py
"""
Unit tests for the A* pathfinder.
"""

import unittest
from astar_pathfinder import AStarPathfinder, Heuristic

class TestAStarPathfinder(unittest.TestCase):
    def test_manhattan_heuristic(self):
        grid = [[0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0]]

        pathfinder = AStarPathfinder(grid, Heuristic.MANHATTAN)
        path = pathfinder.find_path((0, 0), (4, 4))
        self.assertEqual(path, [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)])

    def test_diagonal_heuristic(self):
        grid = [[0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0]]

        pathfinder = AStarPathfinder(grid, Heuristic.DIAGONAL)
        path = pathfinder.find_path((0, 0), (4, 4))
        self.assertEqual(path, [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (4, 4)])

if __name__ == "__main__":
    unittest.main()
```

```python
# setup.py
"""
Build script for packaging the project.
"""

import setuptools

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="astar-pathfinder",
    version="1.0",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    author="Samy Alderson",
    author_email="samy.alderson@example.com"
)
```

```python
# pyproject.toml
"""
Project configuration file for dependency management.
"""

[tool.poetry]
name = "astar-pathfinder"
version = "1.0"
description = "A Python implementation of the A* pathfinding algorithm for data science applications"

[tool.poetry.dependencies]
numpy = "^1.23.0"

[tool.poetry.dev-dependencies]
pytest = "^7.1.2"
```

```python
# requirements.txt
"""
List of dependencies required by the project.
"""

numpy