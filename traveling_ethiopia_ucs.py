import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue
from cities_road_ucs import roads

class TravelEthiopia:
    """
    Implements Uniform Cost Search (UCS) for finding the optimal path in a weighted graph.

    Attributes:
        graph (dict): The adjacency list representation of the graph, where keys are nodes and 
                      values are lists of tuples (neighbor, cost).
        visited (set): A set to keep track of visited nodes.
    """

    def __init__(self, graph):
        """
        Initialize the UniformCostSearch class.

        Args:
            graph (dict): The adjacency list of the graph.
        """
        self.graph = graph

    def find_path(self, start, goal):
        """
        Find the shortest path from start to goal using UCS.

        Args:
            start (str): The initial state.
            goal (str): The goal state.

        Returns:
            tuple: The shortest path as a list of nodes and its total cost.
        """
        priority_queue = PriorityQueue()
        priority_queue.put((0, [start]))  # (cumulative_cost, path)
        visited = set()

        while not priority_queue.empty():
            cost, path = priority_queue.get()
            current_node = path[-1]

            if current_node in visited:
                continue
            visited.add(current_node)

            if current_node == goal:
                return path, cost

            for neighbor, edge_cost in self.graph.get(current_node, []):
                if neighbor not in visited:
                    new_cost = cost + edge_cost
                    new_path = path + [neighbor]
                    priority_queue.put((new_cost, new_path))

        return None, float('inf')  # Return None if no path is found

    def find_path_to_multiple_goals(self, start, goals):
        """
        Find a path that visits multiple goal states using UCS.

        Args:
            start (str): The initial state.
            goals (list): A list of goal states to visit.

        Returns:
            tuple: The shortest path that visits all goals and its total cost.
        """
        remaining_goals = set(goals)
        current_node = start
        total_cost = 0
        full_path = []

        while remaining_goals:
            shortest_path = None
            shortest_cost = float('inf')

            for goal in remaining_goals:
                path, cost = self.find_path(current_node, goal)
                if cost < shortest_cost:
                    shortest_path = path
                    shortest_cost = cost

            if not shortest_path:
                return None, float('inf')  # Return if any goal is unreachable

            full_path.extend(shortest_path[:-1])  # Append path except the last node to avoid duplicates
            current_node = shortest_path[-1]
            total_cost += shortest_cost
            remaining_goals.remove(current_node)

        full_path.append(current_node)  # Add the final goal
        return full_path, total_cost

    def visualize_path(self, path, title="Path Visualization"):
        """
        Visualize the path on the graph using networkx and matplotlib.

        Args:
            path (list): The path as a list of nodes.
            title (str): Title of the visualization.
        """
        G = nx.Graph()

        # Add edges to the graph
        for node, neighbors in self.graph.items():
            for neighbor, cost in neighbors:
                G.add_edge(node, neighbor, weight=cost)

        # Get edge colors (highlight the path in a different color)
        edge_colors = []
        for edge in G.edges:
            if (edge[0] in path and edge[1] in path) and \
               (path.index(edge[0]) == path.index(edge[1]) - 1 or path.index(edge[1]) == path.index(edge[0]) - 1):
                edge_colors.append("red")
            else:
                edge_colors.append("black")

        # Draw the graph
        pos = nx.spring_layout(G)  # Use spring layout for positioning
        nx.draw(G, pos, with_labels=True, node_size=500, font_size=8, edge_color=edge_colors)
        nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)})

        plt.title(title)
        plt.show()



if __name__ == "__main__":
    ucs = TravelEthiopia(roads)

    # Task 2.2: Find a path from Addis Ababa to Lalibela
    path, cost = ucs.find_path("Addis Ababa", "Lalibela")
    print(f"Path from Addis Ababa to Lalibela: {path}, Cost: {cost}")
    ucs.visualize_path(path, title="Path from Addis Ababa to Lalibela")

    # Task 2.3: Visit multiple goals from Addis Ababa
    goals = ["Axum", "Gondar", "Lalibela", "Babile", "Jimma", "Bale", "Sof Oumer", "Arba Minch"]
    path, cost = ucs.find_path_to_multiple_goals("Addis Ababa", goals)
    print(f"Path to visit all goals: {path}, Total Cost: {cost}")
    ucs.visualize_path(path, title="Path to Visit All Goals")
