
# A* Pathfinding Visualization Project

This project consists of three main files, which are: `main.py`, `array.txt`, and `array_randomizer.py`.

### 1. main.py

This is the main python script of the project. It features the implementation of the A* Pathfinding Algorithm, a popular AI technique used in pathfinding and graph traversal, which is the process of finding a path from a designated start to a goal point.

The script contains a `astaralgorithm` class which extends the Tkinter's Frame class to create a GUI application. The GUI application displays a maze-like grid and it animates the steps taken by the A* Algorithm to find a path from the start point to the goal.

The `astaralgorithm` class provides the following functionalities:

-   Reads a grid from a text file in comma-separated format.
-   Visualizes the A* pathfinding process.
-   A GUI window for starting, stopping, and interacting with the application.
-   Uses the Turtle Graphics for grid and path visualization.
-   Allows for the selection of the grid file.

### 2. array.txt

This file contains a grid representation in a comma-separated format. Each row represents a row in the grid. `0` represents an open cell (a cell that can be traversed) while `1` represents a blocked cell (a cell that cannot be traversed).

### 3. array_randomizer.py

This is a Python script that generates a randomized grid for testing purposes. It fills a predefined grid with random `0` and `1` values and then saves the result to the `array.txt` file. The `0,0` and the `len(array)-1, len(array[i])-1` grid cells are guaranteed to be open to allow for a possible path from the start to the goal.

In summary, this project is a wonderful tool for learning and understanding the A* Pathfinding Algorithm. It offers a visual representation of the steps taken by the algorithm, which aids the comprehension of the algorithm's working process.
