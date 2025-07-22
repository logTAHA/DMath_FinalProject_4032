import csv
import random
import sys
from collections import defaultdict


def best_node(candidates, relations, selected):
    best = None
    max_relations = -1

    for n in candidates:
        temp_relations = len(relations[n] & selected)

        if temp_relations > max_relations:
            max_relations = temp_relations
            best = n

    return best


def main():
    # load sample file
    relations = defaultdict(set)
    with open('following.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        # skip first line (source_id,relation,target_id)
        next(reader)
        for src, _, tgt in reader:
            relations[src].add(tgt)
            relations[tgt].add(src)

    all_nodes = set(relations.keys())

    # select 3 nodes that related to each others
    node1 = random.choice(list(all_nodes))

    neighbors1 = list(relations[node1])
    if not neighbors1:
        print(f"node [{node1}] has no relations")
        sys.exit()
    node2 = random.choice(neighbors1)

    neighbors2 = []
    for n in relations[node2]:
        if n != node1:
            neighbors2.append(n)

    if not neighbors2:
        print(f"node [{node2}] has no relations")
        sys.exit()
    node3 = random.choice(neighbors2)

    selected = {node1, node2, node3}

    while len(selected) < 50:
        # set of nodes that we can select
        candidates = set()
        for u in selected:
            candidates |= relations[u]
        candidates -= selected

        if candidates:
            best = best_node(candidates, relations, selected)
        else:
            remaining = all_nodes - selected
            best = best_node(remaining, relations, selected)

        selected.add(best)

    # save selected users
    with open('selected-users.txt', 'w', encoding='utf-8') as f:
        for uid in selected:
            f.write(uid + '\n')

main()