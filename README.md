
# A* (A-Star) Pathfinding Algorithm

> I got still a lot to learn, there is a bug that makes the circles appear on the black boxes, which indicates the wall and shouldn't be considered a path by this A* algorithm. Maybe a different solution to visualisation is necessary, or maybe I should scrap the current one.
(Made thanks to the tutorial by TechWithTim)[https://www.youtube.com/watch?v=JtiK0DOeI4A&ab_channel=TechWithTim]

### main.py

Implementation of the A* Pathfinding Algorithm

The script contains a `astaralgorithm` class which extends the Tkinter's Frame class to create a GUI application.
The GUI application displays a maze-like grid and it animates the steps taken by the A* Algorithm to find a path from the start point to the goal.

The `astaralgorithm` class provides the following functionalities:

-   Reads a grid from `array.txt` divided by coma.
-   Visualizes the A* pathfinding process (walls, paths etc)
-   A GUI window
-   Uses the Turtle Graphics for grid and path visualization.
-   Allows for the selection of the grid file.

### array.txt

Simple Grid used by 'class astaralgorithm'

### array_randomizer.py

Python script fills a predefined grid with random `0` and `1` values and then saves the result to the `array.txt` file. The `0,0` and the `len(array)-1, len(array[i])-1` grid cells are guaranteed to be open to allow for a possible path from the start to the goal.

## tool for learning and understanding the A* Pathfinding Algorithm with a visual representation
