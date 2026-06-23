import random

def objective_function(x):
  return -x ** 2 + 5

def hill_climbing(start_x, step_size, max_iterations):
  current_x = start_x
  current_score = objective_function(current_x)

  for i in range(max_iterations):
    new_x = current_x + random.uniform(-step_size, step_size)
    new_score = objective_function(new_x)

    print(f"Iteration {i + 1}: x = {current_x:.4f}, f(x) = {current_score:.4f}")

    if new_score > current_score:
      current_x = new_x
      current_score = new_score
    else:
      pass
  
  print("\nFinal Solution:")
  print(f"x = {current_x:.4f}, f(x) = {current_score:.4f}")
  return current_x, current_score

best_x, best_score = hill_climbing(start_x=0.1, step_size=0.05, max_iterations=5)






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
           X         Y         Z Category
0   0.496714 -1.415371  0.357787        A
1  -0.138264 -0.420645  0.560785        B
2   0.647689 -0.342715  1.083051        A
3   1.523030 -0.802277  1.053802        A
4  -0.234153 -0.161286 -1.377669        C
..       ...       ...       ...      ...
95 -1.463515  0.385317 -0.692910        C
96  0.296120 -0.883857  0.899600        C
97  0.261055  0.153725  0.307300        A
98  0.005113  0.058209  0.812862        B
99 -0.234587 -1.142970  0.629629        C

[100 rows x 4 columns]
Iteration 1: x = 0.1000, f(x) = 4.9900
Iteration 2: x = 0.1000, f(x) = 4.9900
Iteration 3: x = 0.1000, f(x) = 4.9900
Iteration 4: x = 0.0905, f(x) = 4.9918
Iteration 5: x = 0.0894, f(x) = 4.9920

Final Solution:
x = 0.0807, f(x) = 4.9935"""