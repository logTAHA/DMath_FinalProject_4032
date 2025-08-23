from graph_util import *

def graph_analyze(G):
    while True:
        print_menu()
        choice = input("Please select an option (1-8): ")

        if choice == '0':
            print("Exiting...")
            break
        elif choice == '1':
            while True:
                node = input("Enter node ID (or press Enter for all nodes): ").strip() or None
                try:
                    degrees = degree_calculator(G, node) if node else degree_calculator(G)
                    print("\nDegree(s):")
                    for n, deg in degrees.items():
                        print(f"  - {n}: {deg}")
                    break
                except Exception as e:
                    print(e)
                    print("Please try again.\n")

        elif choice == '2':
            for component in find_connected_components(G):
                print(component)

        elif choice == '3':
            while True:
                direction = ask_direction().strip() or None
                start_node = ask_start_node(G)
                try:
                    path = bfs(G, start_node, direction) if direction else bfs(G, start_node)
                    print(path)
                except ValueError as e:
                    print(e)
                    print("Please try again.\n")

        elif choice == '4':
            while True:
                direction = ask_direction().strip() or None
                start_node = ask_start_node(G)
                try:
                    path = dfs(G, start_node, direction) if direction else dfs(G, start_node)
                    print(path)
                except ValueError as e:
                    print(e)
                    print("Please try again.\n")

        elif choice == '5':
            while True:
                try:
                    source = input("Enter source node: ")
                    target = input("Enter target node: ")
                    weight = input("Enter weight attribute (leave empty for unweighted): ")
                    if weight.strip() == "":
                        weight = None

                    result = find_shortest_path(G, source, target, weight=weight)

                    if result is None:
                        print(f"No path found from {source} to {target}")
                    else:
                        path, length = result
                        print(f"Shortest path: {path}, length: {length}")
                except ValueError as e:
                    print(e)
                    print("Please try again.\n")

        elif choice == '6':
            while True:
                try:
                    n = input("How many top nodes to display? (default 5): ").strip()
                    n = int(n) if n else 5
                    results = analyze_centrality(G, n)
                    for metric, nodes in results.items():
                        print(f"\nTop {n} {metric}:")
                        for node, value in nodes.items():
                            print(f"{node}: {value:.4f}")
                    break
                except Exception as e:
                    print(e)
                    print("Please try again.\n")

        # elif choice == '7':
        #     filename = input("Enter output filename (e.g. graph.png): ").strip() or "graph.png"
        #     prog = input("Enter layout program [dot/neato/fdp/sfdp/circo/twopi] (default=dot): ").strip() or "dot"
        #     node_color = input("Enter node color (default=lightblue): ").strip() or "lightblue"
        #     node_shape = input("Enter node shape (default=circle): ").strip() or "circle"
        #     show_weights_input = input("Show weights? [y/n] (default=y): ").strip().lower()
        #     show_weights = (show_weights_input != "n")
        #
        #     file_path = draw_graph(G, filename=filename, prog=prog, node_color=node_color,node_shape=node_shape, show_weights=show_weights)
        #     print(f"Graph visualization saved to {file_path}")

        elif choice == '8':
            file_path = show_graph(G, "remote")
            print(f"\nGraph saved to {file_path}")

        else:
            print("Invalid input. Please enter a number between 1 and 8.")
            continue

        input("\nPress any key to continue...")

def main():
    while True:
        file_path = input("Please enter the path to the graph CSV file (or press Enter to use the default): ")
        while True:
            is_directed_input = input("Is the graph directed? (y/n): ").lower()
            if is_directed_input == "y":
                is_directed = True
                break
            elif is_directed_input == "n":
                is_directed = False
                break
            else:
                print("Please enter either 'y' or 'n': ")

        try:
            G = build_graph(is_directed, file_path) if file_path.strip() else build_graph(is_directed)
            break
        except RuntimeError as e:
            print(e)
            print("Graph loading failed. Try again.\n")

    print(f"{'Weighted' if weight_status(G) else 'Unweighted'} {'DiGraph' if direct_status(G) else 'Graph'} detected")

    graph_analyze(G)

if __name__ == "__main__":
    main()
