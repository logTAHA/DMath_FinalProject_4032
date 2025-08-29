# 🐦 TwiBot-22 Dataset Sampling

This project focuses on selecting a **smaller but meaningful subset** of the **TwiBot-22** dataset.

---

## 📌 Original Dataset Overview

The **TwiBot-22** dataset was created by an international research team led by **Shangbin Feng** and consists of three main parts:

- **User information (users)**  
- **Tweets (tweets)**  
- **User relations** such as follow, like, etc.  

[GitHub link to TwiBot-22 project](https://github.com/LuoUndergradXJTU/TwiBot-22)  
[Google Drive link to dataset](https://drive.google.com/drive/folders/1YwiOUwtl8pCd2GD97Q_WEzwEUtSPoxFs?usp=sharing)  

---

## 🎯 Project Goal

Since the original dataset is very large, we needed to extract a **smaller but still meaningful sample** suitable for graph analysis and experiments.  

---

## 🛠 Dataset Preparation Process

### 1. Selecting initial users

- We started from the `following.csv` file (follow relations).  
- A subset of users was chosen and stored in `selected-users.txt`.  

### 2. Filtering relations

- From all existing relations, we kept only those where **both source and target users** were included in `selected-users.txt`.  

### 3. Extracting user details

- User details for the selected accounts were extracted from the original `user.json`.  
- Only key fields were kept:  
  `id`, `username`, `name`, `description`, `location`, `verified`, `protected`, `created_at`  
- These were stored in `selected-users-detail.json`.  

---

## ⚡ Challenge in selecting users

If we picked 100 users completely at random, the likelihood of having meaningful connections between them was low, resulting in a fragmented, unconnected sample.  

### First approach (and its issue)

- Start with one high-degree node chosen randomly.  
- Expand using **DFS or BFS** until 100 nodes were reached.  
- **Problem:** This reduced graph diversity, creating long chain-like structures instead of richer connections.  

---

## ✅ Final approach for user selection

### Step 1: Build an undirected graph

- The `following.csv` file was converted into an **undirected graph**.  
- If `a → b`, then `b` is added to neighbors of `a` and `a` to neighbors of `b`.  
- This graph was stored in the variable `relations`.  

### Step 2: Pick three initial nodes

1. Randomly select a node → **node1**  
2. Select one neighbor of `node1` → **node2**  
3. Select one neighbor of `node2` (excluding `node1`) → **node3**  

These three nodes were added to the set `selected`.  

### Step 3: Expanding the `selected` set

While the size of `selected` was less than 50:  
- Create an empty set called `candidate`.  
- For each node in `selected`, add its neighbors to `candidate`.  
- Remove nodes already in `selected` to avoid duplication.  

If `candidate` was not empty:  
- Use the `best_node` function to pick the node with the **highest overlap of connections with already selected nodes**.  

If `candidate` was empty:  
- From `remaining = all_nodes - selected`, pick the best node.  

### Step 4: Run the process twice for diversity

- The whole process was repeated twice to select two relatively independent subgraphs.  
- Each run produced 50 users.  
- Finally, 4 high-degree users (with excessive connections but little analytical value) were removed to keep the graph balanced.  

---

## 📊 Final Result

- **96 users** were stored in `data/users.txt`.  
- A total of **414 follow relations** between them were saved in `data/following.csv`.  
- Detailed user information (name, username, description, location, etc.) was stored in `data/users-detail.json`.  
