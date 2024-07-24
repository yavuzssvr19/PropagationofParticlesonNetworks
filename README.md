# Network Graph Simulation

This project simulates dynamic processes on a graph using NetworkX and Matplotlib. It also calculates and visualizes the powers of the adjacency matrix of a graph at various time steps (t).

## Table of Contents

- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example Outputs](#example-outputs)
- [Contributing](#contributing)
  
## Usage
To run the project, execute the `core.py` file:
  python main.py
  
## Code Explanation
1.  Graph Creation and Visualization:
    *  A chain graph is created and visualized.
2.  Adjacency Matrix Calculation:
    *  The adjacency matrix of the graph is calculated and transformed into the scipy.sparse format.
3.  Calculating and Visualizing Matrix Powers:
    *  Various powers of the adjacency matrix are calculated and visualized as heatmaps.
4.  Creating and Simulating a Random Graph:
    *  A random graph is created using the Erdos-Renyi model, and the adjacency matrix is calculated and visualized at different time steps.

## Example Outputs
Adjacency Matrix Visualization
Chain Graph:
  *  t=0 (A^0)
  *  t=1 (A^1)
  *  t=2 (A^2)
  *  t=3 (A^3)
  *  t=4 (A^4)
  *  t=100 (A^100)

Random Graph:
  *  t=1 (A^1)
  *  t=2 (A^2)
  *  t=3 (A^3)

## Contributing
If you would like to contribute, please open a pull request or issue. We welcome all feedback and contributions.

