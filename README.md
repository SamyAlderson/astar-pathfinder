# A\* Pathfinder
A lightweight Python implementation of the A\* pathfinding algorithm for data science applications.

## What it does
This project implements the A\* pathfinding algorithm, which finds the shortest path between two points in a weighted graph or grid. It's designed for data science use cases, where pathfinding is a common problem.

## Installation
To use this project, clone the repository and install the dependencies with pip:
```bash
git clone https://github.com/SamyAlderson/astar-pathfinder.git
cd astar-pathfinder
pip install .
```
## Usage
To use the A\* pathfinder, import the `astar` module and call the `astar` function with a grid or graph and the start and end points:
```python
from astar import astar

grid = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)
path = astar(grid, start, end)

print(path)  # prints the shortest path from start to end
```
## Building from source
To build the project from source, simply run the `setup.py` script:
```bash
python setup.py sdist
```
This will create a source distribution in the `dist` directory.

## Running tests
To run the unit tests, use the `pytest` command:
```bash
pytest
```
This will run all the tests in the `tests` directory.

## Project structure
The project is structured as follows:

* `astar.py`: the main implementation of the A\* pathfinder
* `tests`: the unit test suite for the A\* pathfinder
* `setup.py`: the setup script for building and distributing the project
* `README.md`: this file

## License
Copyright (c) 2026 SamyAlderson

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.