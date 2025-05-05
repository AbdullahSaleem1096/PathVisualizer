PathVisualizer

🧭 Pathfinding Visualizer
A simple and interactive pathfinding visualizer built using Python and Pygame. This project demonstrates how an informed search algorithm (A*) navigates a grid to find the shortest path between a start and end point while avoiding barriers.

📌 Features
Visualizes the A* (A-star) pathfinding algorithm in real time.

Interactive grid creation:

Set Start and End points.

Draw Barriers with mouse clicks.

Highlights the path explored and the shortest path found.

Designed for educational and demonstration purposes.

📽️ Demo
You can insert a GIF or screenshot here once available
Example placeholder:

🧠 Algorithm Used
The visualizer uses the A* Search Algorithm:

g(n) = cost from the start node to the current node.

h(n) = estimated cost from the current node to the end (using Manhattan Distance).

f(n) = g(n) + h(n).

📦 Requirements
Python 3.x

pygame

Install dependencies with:

bash
Copy
Edit
pip install pygame
▶️ How to Run
Run the program with:

🎮 Controls
Action	Input
Place Start	Left-click (1st)
Place End	Left-click (2nd)
Place Barrier	Left-click (after)
Remove Cell	Right-click
Start Visualization	Press Spacebar
Quit	Close the window

📂 Project Structure
bash
Copy
Edit
Pathisualizer/
├── path_visualizer.py   # Main visualization script
└── README.md            # Project documentation
📚 Learning Objectives
Understand how the A* algorithm works.

Learn to integrate search logic with GUI using Pygame.

Visualize the decision-making process in pathfinding.

🚧 Future Improvements
Add support for other algorithms (Dijkstra, BFS, DFS).

Step-by-step simulation with pause/resume.

Random maze generation.

GUI controls (buttons, dropdowns) for algorithm and grid size selection.

📄 License
This project is licensed under the MIT License.
Feel free to use, modify, and share it!
