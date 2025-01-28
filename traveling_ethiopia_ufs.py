import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from cities_road_ufs import cities, roads


class TravelEthiopia:
    """
    A class for performing search on a graph representation of Ethiopian cities and roads.

    This class supports two search strategies:
    - Breadth-First Search (BFS)
    - Depth-First Search (DFS)

    The graph is visualized using NetworkX, and the search path is highlighted on the graph.

    Attrs:
        cities (list): A list of city names.
        roads (dict): A dictionary mapping each city to its neighboring cities and weights.
        initial_state (str): The starting city for the search.
        goal_state (str): The destination city for the search.
        strategy (str): The search strategy ("BFS" or "DFS").
        graph (dict): The adjacency list representation of the city graph.
    """
    def __init__(self, cities, roads, initial_state, goal_state, strategy):
        self.graph = self._build_graph(cities, roads)
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.strategy = strategy.upper()

    def _build_graph(self, cities, roads):
        """
            Q (1.1) Convert Figure 1 into a manageable data structure:
            Converts city list & roads dictionary into an adjacency list.
            Args:
                cities (list): List of city names.
                roads (dict): Dictionary of roads connecting cities, with weights.

            Returns:
                dict: Adjacency list representation of the graph.
        """
        graph = {city: [] for city in cities}
        for city, neighbors in roads.items():
            for neighbor, _ in neighbors:
                graph[city].append(neighbor)
                graph[neighbor].append(city)  
        return graph

    def search(self):
        """
            Q (1.2) Write a class for the search solution
            Executes search based on selected strategy.
            Returns:
                list or None: The solution path from initial_state to goal_state, or None if no path exists.
            Raises:
                ValueError: If the strategy is invalid.
        """
        if self.strategy == "BFS":
            return self._breadth_first_search()
        elif self.strategy == "DFS":
            return self._depth_first_search()
        else:
            raise ValueError("Invalid search strategy! Use 'BFS' or 'DFS'.")

    def _breadth_first_search(self):
        """
        Breadth-First Search implementation.
        Returns:
            list or None: The solution path from initial_state to goal_state, or None if no path exists.
        """
        queue = deque([[self.initial_state]])
        visited = set()

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == self.goal_state:
                self.visualize_path(path)
                return path

            if node not in visited:
                visited.add(node)
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        queue.append(path + [neighbor])

        return None  

    def _depth_first_search(self):
        """
            Depth-First Search implementation.
            Returns:
                list or None: The solution path from initial_state to goal_state, or None if no path exists.
        """
        stack = [[self.initial_state]]
        visited = set()

        while stack:
            path = stack.pop()
            node = path[-1]

            if node == self.goal_state:
                self.visualize_path(path)
                return path

            if node not in visited:
                visited.add(node)
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        stack.append(path + [neighbor])

        return None  

    def visualize_graph(self):
        """
        Visualizes the full graph using NetworkX.
        """
        G = nx.Graph()
        for city, neighbors in self.graph.items():
            for neighbor in neighbors:
                G.add_edge(city, neighbor)

        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(G, seed=42)  # Layout for consistent positioning
        nx.draw(G, pos, with_labels=True, node_size=300, node_color="lightblue", font_size=8, edge_color="gray")
        plt.title("Ethiopian Cities Road Network")
        plt.show()

    def visualize_path(self, path):
        """
        Visualizes the search path in the graph.

        Args:
            path (list): The solution path to highlight.
        """
        G = nx.Graph()
        for city, neighbors in self.graph.items():
            for neighbor in neighbors:
                G.add_edge(city, neighbor)

        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(G, seed=42)  # Layout for consistent positioning
        nx.draw(G, pos, with_labels=True, node_size=300, node_color="lightgray", font_size=8, edge_color="gray")

        # Highlight path
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="red", node_size=400)
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)

        plt.title(f"Path from {self.initial_state} to {self.goal_state}")
        plt.show()





if __name__ == "__main__":
    search_agent_bfs = TravelEthiopia(cities, roads, "Addis Ababa", "Hawassa", strategy="BFS")
    solution_path_bfs = search_agent_bfs.search()
    print("Solution Path (BFS):", solution_path_bfs)

    search_agent_dfs = TravelEthiopia(cities, roads, "Addis Ababa", "Hawassa", strategy="DFS")
    solution_path_dfs = search_agent_dfs.search()
    print("Solution Path (DFS):", solution_path_dfs)

    # Visualize the full graph
    search_agent_bfs.visualize_graph()
