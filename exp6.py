# EXP-6 ALPHA BETA CLONNING

def alpha_beta(depth, node, maximizing_player, values, alpha, beta):
    # Base case: leaf node
    if depth == 3:
        return values[node]

    if maximizing_player:
        best = float('-inf')

        for i in range(2):
            val = alpha_beta(
                depth + 1,
                node * 2 + i,
                False,
                values,
                alpha,
                beta
            )

            best = max(best, val)
            alpha = max(alpha, best)

            # Beta pruning
            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = alpha_beta(
                depth + 1,
                node * 2 + i,
                True,
                values,
                alpha,
                beta
            )

            best = min(best, val)
            beta = min(beta, best)

            # Alpha pruning
            if beta <= alpha:
                break

        return best


# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

result = alpha_beta(
    0, 0, True, values,
    float('-inf'),
    float('inf')
)

print("Optimal value:", result)
'''---------OUTPUT--------
Optimal value: 5


'''