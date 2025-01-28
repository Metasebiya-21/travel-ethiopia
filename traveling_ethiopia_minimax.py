import matplotlib.pyplot as plt
import networkx as nx
from cities_road_minimax import roads



class MiniMaxSearch:
    """
    A class implementing the MiniMax search algorithm for decision-making in a graph-based environment.
   
    Attributes:
        graph (dict): The graph representation of the environment, where nodes have utilities, neighbors, and terminal status.
    """
import matplotlib.pyplot as plt
import networkx as nx

class TravelEthiopia:
    """
    A class implementing the MiniMax search algorithm for decision-making in a graph-based environment.
    N.B: minimax method doesn't handle cyclic graphs effectively. 
        If there are cycles in the graph, the recursion can endlessly visit the same nodes, leading to a stack overflow.

    Attributes:
        graph (dict): The graph representation of the environment, where nodes have utilities, neighbors, and terminal status.
    """

    def __init__(self, graph):
        """
        Initialize the TravelEthiopia object with a graph.

        Args:
            graph (dict): A dictionary representing the graph.
        """
        self.graph = graph

    def minimax(self, node, depth, maximizing_player, visited):
        """
        Perform the MiniMax search algorithm with cycle detection.

        Args:
            node (str): The current node being evaluated.
            depth (int): The current depth in the search tree.
            maximizing_player (bool): True if the current player is maximizing, False if minimizing.
            visited (set): A set of visited nodes to avoid cycles.

        Returns:
            int: The utility value of the node.
        """
        if node in visited:
            return 0  # Avoid cycles by returning a neutral value

        # If the node is terminal, return its utility
        if self.graph[node]['terminal']:
            return self.graph[node]['utility']

        visited.add(node)

        # Maximizing player's turn
        if maximizing_player:
            max_eval = float('-inf')
            for neighbor, is_blocked in self.graph[node]['neighbors']:
                if not is_blocked:
                    eval = self.minimax(neighbor, depth + 1, False, visited)
                    max_eval = max(max_eval, eval)
            visited.remove(node)
            return max_eval

        # Minimizing player's turn
        else:
            min_eval = float('inf')
            for neighbor, is_blocked in self.graph[node]['neighbors']:
                if not is_blocked:
                    eval = self.minimax(neighbor, depth + 1, True, visited)
                    min_eval = min(min_eval, eval)
            visited.remove(node)
            return min_eval

    def find_best_move(self, start_node):
        """
        Find the best move for the maximizing player from the start node.

        Args:
            start_node (str): The starting node.

        Returns:
            tuple: The best move and its utility value.
        """
        best_move = None
        best_value = float('-inf')

        for neighbor, is_blocked in self.graph[start_node]['neighbors']:
            if not is_blocked:
                eval = self.minimax(neighbor, 0, False, set())
                if eval > best_value:
                    best_value = eval
                    best_move = neighbor

        return best_move, best_value

    def visualize_graph(self, start_node, best_path=None):
        """
        Visualize the graph using matplotlib and networkx.

        Args:
            start_node (str): The starting node for visualization.
            best_path (list, optional): A list of nodes representing the best path. Defaults to None.
        """
        G = nx.Graph()

        # Add nodes and edges to the graph
        for node, data in self.graph.items():
            for neighbor, is_blocked in data['neighbors']:
                if not is_blocked:
                    G.add_edge(node, neighbor)

        # Draw the graph
        pos = nx.spring_layout(G)
        plt.figure(figsize=(12, 8))
        
        # Highlight best path if provided
        if best_path:
            path_edges = list(zip(best_path, best_path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

        # Highlight the start node
        nx.draw_networkx_nodes(G, pos, nodelist=[start_node], node_size=800, node_color='green')

        # Draw other nodes
        remaining_nodes = set(G.nodes()) - {start_node}
        nx.draw_networkx_nodes(G, pos, nodelist=list(remaining_nodes), node_size=700, node_color='lightblue')

        # Draw all edges
        nx.draw_networkx_edges(G, pos)

        # Add node utilities
        labels = {node: f"{node}\n({data['utility']})" for node, data in self.graph.items()}
        nx.draw_networkx_labels(G, pos, labels=labels, font_size=8, font_color='black')

        plt.title(f"Traveling Ethiopia Search Graph (Start: {start_node})")
        plt.show()

if __name__ == "__main__":
    ethiopia_search = TravelEthiopia(roads)
    start = 'Addis Ababa'
    best_move, best_value = ethiopia_search.find_best_move(start)

    # Find the best path (for visualization)
    path = [start, best_move]

    # Display results
    print(f"Best move from {start}: {best_move} with utility {best_value}")

    # Visualize the graph
    ethiopia_search.visualize_graph(start, best_path=path)
