# A\* Pathfinder for Data Science
=============================

## What and Why

The A\* pathfinding algorithm is a popular choice for finding the shortest path between two points in a weighted graph or grid. This implementation is designed for data science applications, where efficient pathfinding is crucial for tasks like route optimization, image processing, and more.

## Install

To get started, install the project using pip:

```bash
pip install .
```

This will install the project's dependencies, including NumPy.

## Usage

The main entry point is `src/main.py`. You can run the example script like this:

```bash
python src/main.py
```

This will demonstrate the pathfinding capabilities of the A\* algorithm.

## Build from Source

To build the project from source, use the following commands:

```bash
pip install build
python -m build
```

This will create a wheel file in the `dist` directory, which you can then install using pip.

## Project Structure

The project is structured as follows:

* `src/main.py`: Main entry point
* `src/utils.py`: Utility functions for grid manipulation and heuristic calculations
* `test/test_astar.py`: Unit tests for the A\* pathfinder
* `setup.py`: Build script for packaging the project
* `pyproject.toml`: Project configuration file for dependency management
* `requirements.txt`: List of dependencies required by the project

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Features

* Support for 2D grid pathfinding
* Implementation of Manhattan distance heuristic
* Support for diagonal movements in the grid
* Unit tests for the A\* pathfinder

## Dependencies

* NumPy

## Architecture

For a more detailed overview of the project architecture, see the ARCHITECTURE.md file.

## Contributing

Contributions are welcome! Please submit pull requests or issues to this repository.