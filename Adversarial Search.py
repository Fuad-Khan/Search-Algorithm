# Define infinity as a large enough value.
INF = float('inf')


# Minimax function to calculate the best move
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Base case: Leaf node is reached
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -INF
        # Recur for left and right children
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = INF
        # Recur for left and right children
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


# Example leaf node values (evaluation function results)
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Perform Minimax from root with depth 0
best_move = minimax(0, 0, True, values, -INF, INF)
print("The best value is:", best_move)
