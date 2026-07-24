# src/utils.py

def calculate_manhattan_distance(node1, node2):
    """
    Calculate the Manhattan distance between two nodes.

    This is used as a heuristic in the A\* pathfinding algorithm.
    It is an admissible heuristic because it never overestimates the distance to the goal.

    :param node1: The first node.
    :param node2: The second node.
    :return: The Manhattan distance between the two nodes.
    """
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])


def reconstruct_path(came_from, current):
    """
    Reconstruct the path from the start node to the current node.

    This is used to return the shortest path from the start node to the goal node.

    :param came_from: A dictionary mapping each node to its parent node.
    :param current: The current node.
    :return: A list of nodes representing the shortest path.
    """
    path = []
    while current:
        path.append(current)
        current = came_from[current]
    return path[::-1]


def heuristic(node, goal):
    """
    Calculate the heuristic value for a node.

    This is an estimate of the cost to reach the goal node from the current node.

    :param node: The current node.
    :param goal: The goal node.
    :return: The heuristic value.
    """
    return calculate_manhattan_distance(node, goal)


def astar_search(graph, start, goal):
    """
    Perform an A\* search on the graph.

    This returns the shortest path from the start node to the goal node.

    :param graph: A dictionary representing the graph, where each key is a node and each value is a list of neighboring nodes.
    :param start: The start node.
    :param goal: The goal node.
    :return: A list of nodes representing the shortest path, or None if no path was found.
    """
    # Create a set to store the nodes we've visited
    visited = set()

    # Create a dictionary to store the node with the lowest f-score
    open_set = {}

    # Create a dictionary to store the node we came from
    came_from = {}

    # Create a dictionary to store the f-score of each node
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    # Create a dictionary to store the h-score of each node
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)

    # Add the start node to the open set
    open_set[start] = f_score[start]

    while open_set:
        # Find the node with the lowest f-score
        current = min(open_set, key=lambda node: open_set[node])

        # If the current node is the goal node, reconstruct the path
        if current == goal:
            return reconstruct_path(came_from, current)

        # Remove the current node from the open set
        del open_set[current]

        # Add the current node to the visited set
        visited.add(current)

        # Update the g-score and f-score of the current node's neighbors
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + 1  # The distance between the current node and its neighbor is 1
            if neighbor not in visited and tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                if neighbor not in open_set:
                    open_set[neighbor] = f_score[neighbor]

    # If no path was found, return None
    return None