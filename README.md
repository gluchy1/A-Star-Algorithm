
# A* Pathfinding Visualization Project

### 1. main.py

This is the main python script of the project.
It features the implementation of the A* Pathfinding Algorithm

The script contains a `astaralgorithm` class which extends the Tkinter's Frame class to create a GUI application.
The GUI application displays a maze-like grid and it animates the steps taken by the A* Algorithm to find a path from the start point to the goal.

The `astaralgorithm` class provides the following functionalities:

-   Reads a grid from a text file in comma-separated format.
-   Visualizes the A* pathfinding process.
-   A GUI window for starting, stopping, and interacting with the application.
-   Uses the Turtle Graphics for grid and path visualization.
-   Allows for the selection of the grid file.

### 2. array.txt

Simple Grid used by 'class astaralgorithm'

### 3. array_randomizer.py

Python script fills a predefined grid with random `0` and `1` values and then saves the result to the `array.txt` file. The `0,0` and the `len(array)-1, len(array[i])-1` grid cells are guaranteed to be open to allow for a possible path from the start to the goal.

tool for learning and understanding the A* Pathfinding Algorithm with a visual representation
