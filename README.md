
# Principles and Techniques of AI Assignment

This project demonstrates various search algorithms applied to pathfinding problems in Ethiopian cities. The assignment includes implementations of both uninformed and informed search techniques for navigating a graph of cities and roads. The project uses different strategies to find paths between various cities, with visual representations of the results.

## File Structure

```
├── cities_road_ifs.py        # Informed search algorithms for the cities and roads problem
├── cities_road_minimax.py    # Minimax algorithm for decision-making in pathfinding
├── cities_road_ucs.py        # Uniform Cost Search (UCS) implementation
├── cities_road_ufs.py        # Uninformed Search (BFS/DFS) for the cities and roads problem
├── images                    # Folder containing pathfinding visualizations
│   ├── path_from_addis_ababa_to_lalibela.png  # Path from Addis Ababa to Lalibela
│   ├── traveling_ethiopia_astar.png            # A* search pathfinding result
│   ├── traveling_ethiopia_bfs.png             # BFS pathfinding result
│   └── traveling_ethiopia_dfs.png             # DFS pathfinding result
├── requirements.txt          # List of Python dependencies
├── traveling_ethiopia_ifs.py  # Informed search algorithms for traveling in Ethiopia
├── traveling_ethiopia_minimax.py # Minimax algorithm for Ethiopia travel problem
├── traveling_ethiopia_ucs.py   # UCS implementation for Ethiopia travel problem
└── traveling_ethiopia_ufs.py   # BFS/DFS implementation for traveling in Ethiopia
```

## Algorithms Implemented

### Uninformed Search
- **Breadth-First Search (BFS)**: Explores paths layer by layer, finding the shortest path in an unweighted graph.
- **Depth-First Search (DFS)**: Explores as far as possible along a path before backtracking.
- **Uniform Cost Search (UCS)**: A modified BFS that accounts for different path costs.

### Informed Search
- **A\* Search**: An informed search algorithm using heuristics to find the most efficient path.
- **Minimax Algorithm**: Used for decision-making, applicable in a game-theory context but also adapted here for pathfinding.

## Setup

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd <repo_directory>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Code

You can run the individual scripts corresponding to the search algorithms:

- For Uninformed Search:
  - `python cities_road_ufs.py`
  - `python cities_road_ucs.py`

- For Informed Search:
  - `python cities_road_ifs.py`
  - `python cities_road_minimax.py`

- For Traveling Ethiopia Problem (same algorithms):
  - `python traveling_ethiopia_ufs.py`
  - `python traveling_ethiopia_ucs.py`
  - `python traveling_ethiopia_ifs.py`
  - `python traveling_ethiopia_minimax.py`

## Visualizations

The `images` directory contains the following visualizations of search algorithm results:
- **A\* Search** (`traveling_ethiopia_astar.png`)
- **BFS Pathfinding** (`traveling_ethiopia_bfs.png`)
- **DFS Pathfinding** (`traveling_ethiopia_dfs.png`)
- **Addis Ababa to Lalibela Path** (`path_from_addis_ababa_to_lalibela.png`)

## Requirements

- Python 3.x
- Required Python packages listed in `requirements.txt`.

## Conclusion

This assignment demonstrates the application of both uninformed and informed search strategies to a real-world problem of pathfinding in Ethiopia. It showcases the differences in efficiency and path quality between various algorithms.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
