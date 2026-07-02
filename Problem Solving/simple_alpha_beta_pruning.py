# Python Program for Alpha-Beta Pruning

import math

# Alpha-Beta Pruning Function
def alpha_beta(depth, node_index, maximizing_player, values, alpha, beta):

    # Terminal node
    if depth == 3:
        return values[node_index]

    if maximizing_player:
        best = -math.inf

        for i in range(2):
            value = alpha_beta(depth + 1,
                               node_index * 2 + i,
                               False,
                               values,
                               alpha,
                               beta)

            best = max(best, value)
            alpha = max(alpha, best)

            # Alpha-Beta Pruning
            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            value = alpha_beta(depth + 1,
                               node_index * 2 + i,
                               True,
                               values,
                               alpha,
                               beta)

            best = min(best, value)
            beta = min(beta, best)

            # Alpha-Beta Pruning
            if beta <= alpha:
                break

        return best


# Driver Code
values = [3, 5, 6, 9, 1, 2, 0, -1]

result = alpha_beta(
    depth=0,
    node_index=0,
    maximizing_player=True,
    values=values,
    alpha=-math.inf,
    beta=math.inf
)

print("Optimal Value:", result)