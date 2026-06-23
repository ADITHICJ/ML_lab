def minimax(depth, node, is_max, scores, max_depth):
    if depth == max_depth:
        return scores[node]

    left = minimax(depth + 1, node * 2, not is_max, scores, max_depth)
    right = minimax(depth + 1, node * 2 + 1, not is_max, scores, max_depth)

    return max(left, right) if is_max else min(left, right)


depth = int(input("Enter tree depth: "))

num_leaves = 2 ** depth
print(f"Enter {num_leaves} leaf node scores:")

scores = list(map(int, input().split()))

if len(scores) != num_leaves:
    print("Invalid number of scores")
else:
    result = minimax(0, 0, True, scores, depth)
    print("Optimal value using Minimax:", result)



"""Enter tree depth: 3
Enter 8 leaf node scores:
3 5 2 9 12 5 23 23
Optimal value using Minimax: 12


                    MAX
                /         \
              MIN         MIN
            /    \       /    \
          MAX    MAX   MAX    MAX
         / \     / \   / \    / \
        3   5   2   9 12  5 23 23
"""