import heapq
import networkx as nx
import matplotlib.pyplot as plt
from cities_road_ifs import roads

class CityGraph:
    def __init__(self, roads_data):
        self.roads_data = roads_data
        self.graph = self._create_graph()

    def _create_graph(self):
        """Creates a NetworkX graph from the roads data."""
        G = nx.Graph()
        for city, data in self.roads_data.items():
            for neighbor, distance in data['neighbors']:
                G.add_edge(city, neighbor, weight=distance)
        return G

    def get_neighbors(self, city):
        """Returns the neighbors of a given city."""
        return self.roads_data[city]['neighbors']

    def get_heuristic(self, city):
        """Returns the heuristic (straight-line distance) for a city."""
        return self.roads_data[city]['cost']


class AStarSearch:
    def __init__(self, graph):
        self.graph = graph

    def search(self, start, goal):
        """Performs A* search to find the optimal path from start to goal."""
        open_set = []
        heapq.heappush(open_set, (0 + self.graph.get_heuristic(start), start))

        g_costs = {start: 0}
        came_from = {}

        while open_set:
            _, current_city = heapq.heappop(open_set)

            if current_city == goal:
                return self._reconstruct_path(came_from, current_city)

            for neighbor, distance in self.graph.get_neighbors(current_city):
                tentative_g_cost = g_costs[current_city] + distance

                if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g_cost
                    f_cost = tentative_g_cost + self.graph.get_heuristic(neighbor)
                    heapq.heappush(open_set, (f_cost, neighbor))
                    came_from[neighbor] = current_city

        return None  # No path found

    def _reconstruct_path(self, came_from, current):
        """Reconstructs the optimal path from the 'came_from' data."""
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.append(current)
        path.reverse()
        return path


class AStarVisualizer:
    def __init__(self, graph):
        self.graph = graph

    def visualize(self, path):
        """Visualizes the graph and highlights the found path."""
        pos = nx.spring_layout(self.graph.graph, seed=42)
        plt.figure(figsize=(15, 10))

        nx.draw(self.graph.graph, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)

        path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(self.graph.graph, pos, edgelist=path_edges, edge_color='red', width=2)
        nx.draw_networkx_nodes(self.graph.graph, pos, nodelist=path, node_color='orange')

        edge_labels = nx.get_edge_attributes(self.graph.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph.graph, pos, edge_labels=edge_labels)

        plt.title("A* Search Path Visualization", fontsize=15)
        plt.show()


if __name__ == '__main__':
    city_graph = CityGraph(roads)
    searcher = AStarSearch(city_graph)
    visualizer = AStarVisualizer(city_graph)

    start_city = 'Addis Ababa'
    goal_city = 'Moyale'

    path = searcher.search(start_city, goal_city)

    if path:
        print(f"Optimal path from {start_city} to {goal_city}: {' -> '.join(path)}")
        visualizer.visualize(path)
    else:
        print(f"No path found from {start_city} to {goal_city}.")
