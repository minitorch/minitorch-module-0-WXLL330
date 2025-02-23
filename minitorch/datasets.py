import math
import random
from dataclasses import dataclass
from typing import List, Tuple


def make_pts(N):
    """Generate a list of N random 2D points.

    Args:
        N (int): The number of points to generate.

    Returns:
        list of tuple: A list containing N tuples, each with two random float values representing a 2D point.

    """
    X = []
    for i in range(N):
        x_1 = random.random()
        x_2 = random.random()
        X.append((x_1, x_2))
    return X


@dataclass
class Graph:
    N: int
    X: List[Tuple[float, float]]
    y: List[int]


def simple(N):
    """Generates a simple dataset for binary classification.

    Args:
        N (int): The number of data points to generate.

    Returns:
        Graph: A Graph object containing the generated data points and their labels.

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def diag(N):
    """Generates a dataset of N points and assigns a label based on the sum of the coordinates.

    Args:
        N (int): The number of points to generate.

    Returns:
        Graph: A Graph object containing the generated points and their corresponding labels.

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 + x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def split(N):
    """Splits the generated points into two classes based on the x_1 coordinate.

    Args:
        N (int): The number of points to generate.

    Returns:
        Graph: A Graph object containing the generated points and their corresponding classes.

    The function generates N points using the make_pts function. Each point is classified into one of two classes based on the x_1 coordinate:
        - Class 1 if x_1 < 0.2 or x_1 > 0.8
        - Class 0 otherwise

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.2 or x_1 > 0.8 else 0
        y.append(y1)
    return Graph(N, X, y)


def xor(N):
    """Generates a dataset for the XOR problem.

    Args:
        N (int): The number of data points to generate.

    Returns:
        Graph: A graph object containing the generated points and their corresponding XOR labels.

    The function generates N points in a 2D space and labels them according to the XOR logic:
    - Label is 1 if one of the coordinates is greater than 0.5 and the other is less than 0.5.
    - Label is 0 otherwise.

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.5 and x_2 > 0.5 or x_1 > 0.5 and x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def circle(N):
    """Generates a dataset of N points arranged in a circle pattern.

    Args:
        N (int): The number of points to generate.

    Returns:
        Graph: A graph object containing the generated points and their labels.
               The labels are 1 if the point lies outside a circle of radius sqrt(0.1)
               centered at (0.5, 0.5), and 0 otherwise.

    """
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        x1, x2 = x_1 - 0.5, x_2 - 0.5
        y1 = 1 if x1 * x1 + x2 * x2 > 0.1 else 0
        y.append(y1)
    return Graph(N, X, y)


def spiral(N):
    """Generates a spiral dataset.

    Args:
        N (int): The total number of points in the dataset. Must be an even number.

    Returns:
        Graph: A Graph object containing the generated points and their corresponding labels.

    The function generates two interleaving spirals, each with N/2 points. The points are 
    calculated using parametric equations for a spiral and then shifted to fit within a 
    unit square. The labels for the points are 0 for the first spiral and 1 for the second spiral.

    """
    def x(t):
        return t * math.cos(t) / 20.0

    def y(t):
        return t * math.sin(t) / 20.0

    X = [
        (x(10.0 * (float(i) / (N // 2))) + 0.5, y(10.0 * (float(i) / (N // 2))) + 0.5)
        for i in range(5 + 0, 5 + N // 2)
    ]
    X = X + [
        (y(-10.0 * (float(i) / (N // 2))) + 0.5, x(-10.0 * (float(i) / (N // 2))) + 0.5)
        for i in range(5 + 0, 5 + N // 2)
    ]
    y2 = [0] * (N // 2) + [1] * (N // 2)
    return Graph(N, X, y2)


datasets = {
    "Simple": simple,
    "Diag": diag,
    "Split": split,
    "Xor": xor,
    "Circle": circle,
    "Spiral": spiral,
}
