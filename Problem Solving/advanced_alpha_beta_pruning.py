class Node:
    def __init__(self, name, value=None, children=None):
        self.name = name          # Identifier for the node
        self.value = value        # Evaluation score (only for leaf nodes)
        self.children = children if children is not None else []

    def is_terminal(self):
        # A node is terminal if it has no children or holds a leaf value
        return len(self.children) == 0 or self.value is not None

    def evaluate(self):
        return self.value

    def get_children(self):
        return self.children


def alpha_beta_search(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate()

    if maximizing_player:
        best_val = -float('inf')
        for child in node.get_children():
            val = alpha_beta_search(child, depth - 1, alpha, beta, False)
            best_val = max(best_val, val)
            alpha = max(alpha, best_val)
            if beta <= alpha:
                print(f"  [Pruned] Maximizer skipped remaining branches at {node.name}")
                break  
        return best_val
    else:
        best_val = float('inf')
        for child in node.get_children():
            val = alpha_beta_search(child, depth - 1, alpha, beta, True)
            best_val = min(best_val, val)
            beta = min(beta, best_val)
            if beta <= alpha:
                print(f"  [Pruned] Minimizer skipped remaining branches at {node.name}")
                break  
        return best_val


# --- Building an Example Game Tree ---
# Leaf Nodes (Values at the bottom of the tree)
leaf_a = Node("Leaf A", value=3)
leaf_b = Node("Leaf B", value=5)
leaf_c = Node("Leaf C", value=6)
leaf_d = Node("Leaf D", value=9)
leaf_e = Node("Leaf E", value=1)
leaf_f = Node("Leaf F", value=2)
leaf_g = Node("Leaf G", value=0)
leaf_h = Node("Leaf H", value=-1)

# Middle Layer (Minimizer nodes)
min_node_1 = Node("Min 1", children=[leaf_a, leaf_b])
min_node_2 = Node("Min 2", children=[leaf_c, leaf_d])
min_node_3 = Node("Min 3", children=[leaf_e, leaf_f])
min_node_4 = Node("Min 4", children=[leaf_g, leaf_h])

# Root Layer (Maximizer node)
root = Node("Root", children=[min_node_1, min_node_2, min_node_3, min_node_4])


# --- Running the Algorithm ---
print("Starting Alpha-Beta Search...")
initial_alpha = -float('inf')
initial_beta = float('inf')

# We start at the Root, depth 2, maximizing player's turn
optimal_score = alpha_beta_search(root, depth=2, alpha=initial_alpha, beta=initial_beta, maximizing_player=True)

print(f"\nThe optimal score the maximizer can guarantee is: {optimal_score}")
