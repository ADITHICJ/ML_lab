import random

def objective_function(x):
    return -x**2 + 5

def hill_climbing(start_x, step_size, max_iterations):
    current_x = start_x
    current_score = objective_function(current_x)

    for i in range(max_iterations):
        new_x = current_x + random.uniform(-step_size, step_size)
        new_score = objective_function(new_x)

        if new_score > current_score:
            current_x = new_x
            current_score = new_score

        print(f"Iteration {i + 1}: x = {current_x:.4f}, f(x) = {current_score:.4f}")

    print("\nFinal Solution:")
    print(f"x = {current_x:.4f}, f(x) = {current_score:.4f}")


hill_climbing(start_x=3, step_size=0.5, max_iterations=20)





# # User Input
# start = int(input("Enter starting point: "))
# step_size = int(input("Enter step size: "))
# max_iterations = int(input("Enter maximum iterations: "))

# # Run algorithm
# best_x, best_value = hill_climbing(
#     start,
#     step_size,
#     max_iterations
# )

# # Display final answer
# print("\nBest Solution :", best_x)
# print("Maximum Value :", best_value)

# The scatter plot visualizes the relationship between two dimensions (X and Y) of an n-dimensional dataset.

"""
Iteration 1: x = 2.7594, f(x) = -2.6143
Iteration 2: x = 2.7594, f(x) = -2.6143
Iteration 3: x = 2.5147, f(x) = -1.3237
Iteration 4: x = 2.2006, f(x) = 0.1574
Iteration 5: x = 1.8372, f(x) = 1.6259
Iteration 6: x = 1.8372, f(x) = 1.6259
Iteration 7: x = 1.4875, f(x) = 2.7873
Iteration 8: x = 1.4875, f(x) = 2.7873
Iteration 9: x = 1.1104, f(x) = 3.7670
Iteration 10: x = 0.7898, f(x) = 4.3762
Iteration 11: x = 0.5235, f(x) = 4.7259
Iteration 12: x = 0.5235, f(x) = 4.7259
Iteration 13: x = 0.3028, f(x) = 4.9083
Iteration 14: x = 0.3028, f(x) = 4.9083
Iteration 15: x = 0.1786, f(x) = 4.9681
Iteration 16: x = 0.0912, f(x) = 4.9917
Iteration 17: x = 0.0524, f(x) = 4.9973
Iteration 18: x = 0.0189, f(x) = 4.9996
Iteration 19: x = 0.0189, f(x) = 4.9996
Iteration 20: x = 0.0065, f(x) = 5.0000

Final Solution:
x = 0.0065
f(x) = 5.0000
"""