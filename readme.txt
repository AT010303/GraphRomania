Romania Graph Search Algorithms

This mini project implements various search algorithms on a graph representing cities in Romania. The goal of the algorithms is to find a path from the city of Arad to Bucharest using different search strategies.

Graph

The graph is visualized using the tkinter library. Cities are represented as nodes, and connections between cities are displayed as lines. The coordinates of the cities are defined in the graph module.

Requirements
The project is implemented in Python and requires the following dependencies:

tkinter: This library is used for creating the graphical user interface. graph: This module contains the Romania map graph representation. node: This module defines the node class for representing cities in the graph. pqueue: This module implements the priority queue data structure. searchalgo: This module contains the search algorithms implemented on the graph. Usage To run the program, execute the main.py file. This will launch a graphical user interface that displays the Romania graph and provides buttons for selecting different search algorithms.

Deployment
To deploy this project run

    python main.py
Search Algorithms Implemented
The following search algorithms are implemented:

Depth-First Search (DFS): This algorithm explores the graph using a depth-first search strategy. 

Depth-Limited Search (DLS): This algorithm explores the graph using a depth-limited search strategy with a specified depth limit. 

Iterative Deepening Depth-First Search (IDDFS): This algorithm implements the iterative deepening depth-first search strategy.

Best-First Search: This algorithm uses the best-first search strategy to find the path. A*: This algorithm implements the A* search algorithm using a heuristic function. 

Running the Algorithms To run a specific search algorithm, click on the corresponding button in the user interface. 
The algorithm will be applied to find a path from Arad to Bucharest in the Romania graph. 
The results will be displayed in the text box, including the path, depth, path cost, and the number of nodes generated during the search process.