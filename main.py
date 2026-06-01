import numpy as np
import matplotlib.pyplot as plt
import itertools

# -----------------------------
# Nodes
# -----------------------------
nodes = np.array([
    [0, 0],
    [2, 3],
    [4, 1],
    [6, 4],
    [8, 2]
])

n = len(nodes)

# -----------------------------
# Distance Function
# -----------------------------
def distance(i, j):
    return np.linalg.norm(nodes[i] - nodes[j])

# -----------------------------
# Traffic Matrix
# -----------------------------
traffic = np.array([
    [0,1,2,2,3],
    [1,0,2,3,2],
    [2,2,0,1,2],
    [2,3,1,0,1],
    [3,2,2,1,0]
])

# Cost Function
def cost(i, j):
    return distance(i, j) * traffic[i][j]

# -----------------------------
# PRINT EDGE DETAILS
# -----------------------------
print("\nEdge Details:\n")
print("Edge\tDistance\tTraffic\tCost")

for i in range(n):
    for j in range(i+1, n):
        d = round(distance(i, j), 2)
        t = traffic[i][j]
        c = round(cost(i, j), 2)
        print(f"{i} -> {j}\t{d}\t\t{t}\t{c}")

# -----------------------------
# Generate ALL paths
# -----------------------------
all_paths = list(itertools.permutations(range(1, n)))
all_paths = [[0] + list(p) for p in all_paths]

def path_cost(path):
    return sum(cost(path[i], path[i+1]) for i in range(len(path)-1))

path_costs = [(path, path_cost(path)) for path in all_paths]

# -----------------------------
# Best path
# -----------------------------
best_path, best_cost = min(path_costs, key=lambda x: x[1])

print("\nBest Path:", best_path)
print("Minimum Cost:", round(best_cost, 2))

x = nodes[:,0]
y = nodes[:,1]

# -----------------------------
# FUNCTION TO ADD LABELS
# -----------------------------
def add_labels():
    for i in range(n):
        for j in range(i+1, n):
            p1 = nodes[i]
            p2 = nodes[j]

            mid_x = (p1[0] + p2[0]) / 2
            mid_y = (p1[1] + p2[1]) / 2

            d = round(distance(i, j), 2)
            t = traffic[i][j]
            c = round(cost(i, j), 2)

            label = f"D:{d}\nT:{t}\nC:{c}"
            plt.text(mid_x, mid_y, label, fontsize=8)

# =============================
# GRAPH 1: ALL PATHS
# =============================
plt.figure()

for path, _ in path_costs:
    for i in range(len(path)-1):
        p1 = nodes[path[i]]
        p2 = nodes[path[i+1]]
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], alpha=0.2)

# highlight best path
for i in range(len(best_path)-1):
    p1 = nodes[best_path[i]]
    p2 = nodes[best_path[i+1]]
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], linewidth=3)

plt.scatter(x, y)

for i, (xi, yi) in enumerate(nodes):
    plt.text(xi, yi, f"{i}")

add_labels()

plt.title("All Paths + Best Path (with D, T, C)")
plt.show()

# =============================
# GRAPH 2: ONLY BEST PATH
# =============================
plt.figure()

for i in range(len(best_path)-1):
    p1 = nodes[best_path[i]]
    p2 = nodes[best_path[i+1]]
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], linewidth=4)

plt.scatter(x, y)

for i, (xi, yi) in enumerate(nodes):
    plt.text(xi, yi, f"{i}")
add_labels()

plt.title("Optimal Path Only (with D, T, C)")
plt.show()
