# 📌 Social Network Graph Analysis (Graph Analyzer)

> **Objective:** Model and analyze a hypothetical/real social network using graphs and Python + NetworkX  
> **Deliverables:** Code, graph structure analysis, and visual outputs

---

## 🔹 Project Overview
This project is a **Graph Analyzer for social networks** that builds a graph from raw data (CSV) and performs the following analyses:
- Detect graph type: **Directed / Undirected / Weighted / Simple**
- Calculate **in-degree and out-degree** of each node
- Find **Connected Components**
- Run **BFS** and **DFS** traversals
- Compute **Shortest Path** between nodes using **Dijkstra**
- Perform **Centrality Analysis** (Degree, In-Degree, Out-Degree, Betweenness, Closeness, Eigenvector) to identify key nodes
- Graph visualization with **Graphviz (PNG)** and **PyVis (HTML)**
- [Test results](https://github.com/logTAHA/DMath_FinalProject_4032/blob/main/40318203-40326823-1/TESTS.md)  

---

## 🧰 Tools & Libraries
- Language: **Python 3.8+**
- Libraries: **NetworkX**, **PyVis**, **PyGraphviz**
- Optional: **Graphviz** system package (required by PyGraphviz)

```bash
pip install networkx pyvis pygraphviz
# Note: PyGraphviz requires Graphviz installed on the system.
```

---

## 📂 Input Data (CSV)
- **CSV** (edge list): columns should be `src, relation, tgt[, weight]`
    - Example:
      ```csv
      src,relation,tgt,weight
      A,follows,B,1
      B,follows,C,1
      C,mentions,A,2
      ```

> Default input file: `data/following.csv` (if input is left blank).

---

## 🚀 How to Run
1. Clone/download the repository and navigate into the project folder.  
2. Install dependencies (see "Tools & Libraries").  
3. Run the interactive program:
```bash
python main.py
```
4. After starting:
- Enter the path to the CSV file (or press **Enter** to use `data/following.csv`).  
- Specify whether the graph is **Directed** (y/n).  
- Use the interactive menu to perform different analyses.

---

## 🧭 Interactive Menu Guide
Once the graph is loaded, the following menu is displayed:
```
1. Calculate Node Degrees               -> Degree calculation (for directed graphs: in/out)
2. Find Connected Components            -> Strongly connected (directed) or connected (undirected)
3. Run BFS Traversal                    -> BFS with direction (in/out/both) and start node
4. Run DFS Traversal                    -> DFS with direction (in/out/both) and start node
5. Find Shortest Path Between Two Nodes -> Dijkstra shortest path (weight optional)
6. Analyze Centrality (Find Key Nodes)  -> Centrality analysis with top-N results
7. Draw Graph                           -> Save PNG using Graphviz
8. Show Graph HTML                      -> Save interactive HTML with PyVis
0. Exit
```
- Outputs:
  - **`graph.html`** → interactive visualization (PyVis)  
  - **`graph.png`** → static image (Graphviz)  

---

## 🔍 Feature Mapping to Code
- Graph building from CSV: `build_graph()` in `graph_util.py`
- Adding nodes/edges: `add_edge()`
- Graph properties: `direct_status()`, `weight_status()`
- Degree calculation: `degree_calculator()`
- Connected Components: `find_connected_components()`
- Traversals: `bfs()` and `dfs()` (with `in/out/both` modes for directed graphs)
- Shortest Path (Dijkstra): `find_shortest_path()`
- Centralities: `analyze_centrality()`
- Visualization: `draw_graph()` (PNG via Graphviz), `show_graph()` (HTML via PyVis)
- CLI & menu handling: `main.py` → `graph_analyze()`

---

## 🧪 Example Usage
- **Degrees**: Option 1 → choose node or all  
- **Connected Components**: Option 2 → list of components  
- **BFS/DFS**: Options 3 & 4 → specify direction and start node  
- **Shortest Path**: Option 5 → source, target, weight (optional)  
- **Centrality**: Option 6 → specify top-N  
- **Visualization**: Options 7 & 8  

---

## 📊 Outputs
- `graph.html` → interactive visualization (color/size of nodes reflect analysis results)
- `graph.png` → static visualization with layout options (`dot`, `neato`, `fdp`, `sfdp`, `circo`, `twopi`)
- Centrality scores, paths, and analysis results printed in terminal

---

## 👥 Team Members & Contributions

| Name | Role | Responsibilities |
|------|------|------------------|
| Taha Amini | Team Leader | Extracting Data Set, Graph Building, BFS, DFS, Graph Drawing and Test |
| Eiliya Yavari | Collaborator | Degree Calculating, Finding Shortest Path, Connected Components, Centrality Analysis, CLI and Documentation|

---

## 📦 Project Structure
```
40318203-40326823-1 (project-root)/
│── data/
│    └── select-data/
│        └── README.md
│        └── select-relations.py
│        └── select-users.py
│        └── select-users-detail.py
│    └── following.csv   # Sample data (optional)
│    └── users.txt
│    └── users-detail.json
│── src/
│    └── main.py              # Interactive CLI program
│    └── graph_util.py        # Graph algorithms and utility functions
│    └── main.ipynb           # Jupyter notebook for experiments
│── README.md            # Project documentation
```
---

## 📝 Notes & Tips
- For large graphs, visualization (PNG/HTML) may take time. Filtering subgraphs is recommended.  
- For directed graphs, traversal direction (`in/out/both`) can be specified.  
- To use weighted edges in Dijkstra, provide the weight attribute name (e.g., `weight`).  

---
