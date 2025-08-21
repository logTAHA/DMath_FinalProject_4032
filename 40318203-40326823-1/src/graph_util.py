from typing import *
import networkx as nx
import csv
import matplotlib.pyplot as plt

def build_graph(is_directed, path="../data/following.csv"):
    try:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)

            if is_directed:
                G = nx.MultiDiGraph()
            else:
                G = nx.MultiGraph()

            for src, rel, tgt in reader:
                add_edge(G, src, tgt, rel)
    except Exception as e:
        raise RuntimeError(f"Unable to open file in this path: '{path}'") from e
    # return graph
    return G

default_attrs = {"type": "user", "color": "white", "size": "3.14"}
def add_edge(G, src, tgt, rel):
    if src not in G:
        G.add_node(src, **default_attrs)
    if tgt not in G:
        G.add_node(tgt, **default_attrs)
    G.add_edge(src, tgt, relation=rel)

def direct_status(G):
    return G.is_directed()

def weight_status(G):
    return nx.is_weighted(G)

def degree_calculator(
        G: Union[nx.Graph, nx.DiGraph, nx.MultiGraph, nx.MultiDiGraph],
        node: Optional[Any] = None
) -> Dict[Any, Union[int, Dict[str, int]]]:
    if G is None or G.number_of_nodes() == 0:
        raise ValueError("The input graph is empty or not loaded.")

    if node is not None and not G.has_node(node):
        raise ValueError(f"The node '{node}' does not exist in the graph.")

    results: Dict[Any, Union[int, Dict[str, int]]] = {}
    nodes = [node] if node is not None else G.nodes()

    if nx.is_directed(G):
        for n in nodes:
            results[n] = {"in_degree": G.in_degree(n),"out_degree": G.out_degree(n)}
    else:
        for n in nodes:
            results[n] = G.degree(n)

    return results

def find_connected_components(
        G: Union[nx.Graph, nx.DiGraph, nx.MultiGraph, nx.MultiDiGraph],
) -> List[Set[Union[int, str]]]:
    if G is None or G.number_of_nodes() == 0:
        raise ValueError("The input graph is empty or not loaded.")

    if nx.is_directed(G):
        components = list(nx.strongly_connected_components(G))
    else:
        components = list(nx.connected_components(G))

    return components

def dfs(G, start_node, direction='out'):
    if direction != 'in' and direction != 'out' and direction != 'both':
        raise ValueError(f"Direction '{direction}' is not supported. Choose from 'in', 'out', or 'both'")
    stack = [start_node]
    visited = set()
    path = []
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        path.append(node)
        # graph is multy directed graph
        neighbors = list()
        if direction == 'out':
            neighbors = list(G.successors(node))
        elif direction == 'in':
            neighbors = list(G.predecessors(node))
        elif direction == 'both':
            out_neighbors = set(G.successors(node))
            in_neighbors = set(G.predecessors(node))
            neighbors = list(out_neighbors | in_neighbors)

        stack.extend(reversed(neighbors))
    return path

def bfs(G, start_node, direction='out'):
    if direction != 'in' and direction != 'out' and direction != 'both':
        raise ValueError(f"Direction '{direction}' is not supported. Choose from 'in', 'out', or 'both'")
    queue = [start_node]
    visited = set()
    path = []

    while queue:
        node = queue.pop()
        if node in visited:
            continue
        visited.add(node)
        path.append(node)
        neighbors = list()
        if direction == 'out':
            neighbors = list(G.successors(node))
        elif direction == 'in':
            neighbors = list(G.predecessors(node))
        elif direction == 'both':
            out_neighbors = set(G.successors(node))
            in_neighbors = set(G.predecessors(node))
            neighbors = list(out_neighbors | in_neighbors)
        queue = neighbors + queue
    return path

def find_shortest_path(
        G: Union[nx.Graph, nx.DiGraph, nx.MultiGraph, nx.MultiDiGraph],
        source: Any,
        target: Any,
        weight: Optional[str] = None
) -> Optional[Tuple[List[Any], float]]:
    if G is None or G.number_of_nodes() == 0:
        raise ValueError("The input graph is empty or not loaded.")

    if not G.has_node(source) or not G.has_node(target):
        raise ValueError(f"Source node '{source}' or target node '{target}' not found in the graph.")

    try:
        path = nx.dijkstra_path(G, source, target, weight=weight)
        distance = nx.dijkstra_path_length(G, source, target, weight=weight)
        return path, distance
    except nx.NodeNotFound:
        raise ValueError(f"Source node '{source}' or target node '{target}' not found in the graph.")
    except nx.NetworkXNoPath:
        print(f"No path exists between {source} and {target}.")
        return None

def analyze_centrality(
        G: Union[nx.Graph, nx.DiGraph, nx.MultiGraph, nx.MultiDiGraph],
        top_n: int = 5
) -> Dict[str, Dict[Any, float]]:
    if G is None or G.number_of_nodes() == 0:
        raise ValueError("The input graph is empty or not loaded.")

    results = {}

    degree_centrality = nx.degree_centrality(G)
    top_degree = dict(sorted(degree_centrality.items(), key=lambda item: item[1], reverse=True)[:top_n])
    results["degree_centrality"] = top_degree

    if nx.is_directed(G):
        in_degree_centrality = nx.in_degree_centrality(G)
        top_in_degree = dict(sorted(in_degree_centrality.items(), key=lambda item: item[1], reverse=True)[:top_n])
        results["in_degree_centrality"] = top_in_degree

        out_degree_centrality = nx.out_degree_centrality(G)
        top_out_degree = dict(sorted(out_degree_centrality.items(), key=lambda item: item[1], reverse=True)[:top_n])
        results["out_degree_centrality"] = top_out_degree


    betweenness_centrality = nx.betweenness_centrality(G)
    top_betweenness = dict(sorted(betweenness_centrality.items(), key=lambda item: item[1], reverse=True)[:top_n])
    results["betweenness_centrality"] = top_betweenness


    closeness_centrality = nx.closeness_centrality(G)
    top_closeness = dict(sorted(closeness_centrality.items(), key=lambda item: item[1], reverse=True)[:top_n])
    results["closeness_centrality"] = top_closeness


    try:
        eigenvector_centrality = nx.eigenvector_centrality(G, max_iter=1000)
        top_eigenvector = dict(list(sorted(eigenvector_centrality.items(), key=lambda item: item[1], reverse=True))[:top_n])
        results["eigenvector_centrality"] = top_eigenvector
    except nx.PowerIterationFailedConvergence:
        print("Eigenvector centrality did not converge.")
        results["eigenvector_centrality"] = {}

    return results

def print_menu():
    print("\n" + "=" * 40)
    print("           Graph Analyzer Menu")
    print("=" * 40)
    print("1. Calculate Node Degrees")
    print("2. Find Connected Components")
    print("3. Run BFS Traversal")
    print("4. Run DFS Traversal")
    print("5. Find Shortest Path Between Two Nodes")
    print("6. Analyze Centrality (Find Key Nodes)")
    print("7. Draw Graph")
    print("8. Exit")
    print("=" * 40)