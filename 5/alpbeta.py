def alphabeta(depth, node, is_max, scores, max_depth, alpha, beta):
    if depth == max_depth:
        return scores[node]

    value = float('-inf') if is_max else float('inf')

    for i in range(2):
        child = alphabeta(
            depth + 1,
            node * 2 + i,
            not is_max,
            scores,
            max_depth,
            alpha,
            beta
        )

        if is_max:
            value = max(value, child)
            alpha = max(alpha, value)
        else:
            value = min(value, child)
            beta = min(beta, value)

        if beta <= alpha:
            break

    return value


depth = int(input("Enter tree depth: "))

num_leaves = 2 ** depth
print(f"Enter {num_leaves} leaf node scores:")

scores = list(map(int, input().split()))

if len(scores) == num_leaves:
    print("Optimal value:", 
        alphabeta(0, 0, True, scores, depth, float('-inf'), float('inf')
    ))
else:
    print("Invalid number of scores")




"""
Enter tree depth: 3
Enter leaf scores: 3 5 2 9 12 5 23 23
Optimal value: 12
"""
