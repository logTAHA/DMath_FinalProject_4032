import networkx as nx

def degree_calculator(G):
    if G is None or G.number_of_nodes() == 0:
        print("Please load a graph first.")
        return

    if nx.is_directed(G):
        print("--- 2. Calculate In-Degree And Out-Degree ---\n")
        choice = input("Do you want the degree of a specific node or all nodes (specific/all)? ").lower()
        if choice == "all":
            print("\n--- In-degree and Out-degree of all nodes ---")
            for node in G.nodes():
                print(f"Node {node}: In_Degree = {G.in_degree(node)}, Out_Degree = {G.out_degree(node)}")
        elif choice == "specific":
            node = input("Enter the desired node name: ")
            if G.has_node(node):
                print(f"Node {node}: In_Degree = {G.in_degree(node)}, Out_Degree = {G.out_degree(node)}")
            else:
                print(f"Node {node} doesn't exist in the graph.")
        else:
            print("Invalid choice.")
            return

    else:
        print("--- 2. Calculate Degree ---\n")
        choice = input("Do you want the degree of a specific node or all nodes (specific/all)? ").lower()
        if choice == "all":
            print("\n--- Degree of all nodes ---")
            for node in G.nodes():
                print(f"Node {node}: Degree = {G.degree(node)}")
        elif choice == "specific":
            node = input("Enter the desired node name: ")
            if G.has_node(node):
                print(f"Node {node}: Degree = {G.degree(node)}")
            else:
                print(f"Node {node} doesn't exist in the graph.")
        else:
            print("Invalid choice.")
            return

        print()