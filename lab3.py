# Hill Climbing Algorithm

# Objective function to maximize
def objective_function(x):
    return -(x * x) + 5  #-(x - 3) ** 2 + 10


# Hill Climbing Function
def hill_climbing(start, step_size, max_iterations):

    # Initial state
    current = start

    # Repeat until maximum iterations
    for i in range(max_iterations):

        # Calculate current state's value
        current_value = objective_function(current)

        # Generate neighbours
        left = current - step_size
        right = current + step_size

        # Calculate neighbour values
        left_value = objective_function(left)
        right_value = objective_function(right)

        # Display current state
        print(f"\nIteration {i+1}")
        print("Current State :", current)
        print("Current Value :", current_value)

        print("Left Neighbour :", left,
              "Value :", left_value)

        print("Right Neighbour :", right,
              "Value :", right_value)

        # Move to the best neighbour
        if left_value > current_value and left_value >= right_value:
            print("Moving to Left Neighbour")
            current = left

        elif right_value > current_value and right_value > left_value:
            print("Moving to Right Neighbour")
            current = right

        # Stop if no neighbour is better
        else:
            print("No better neighbour found")
            break

    # Return best solution
    return current, objective_function(current)


# User Input
start = int(input("Enter starting point: "))
step_size = int(input("Enter step size: "))
max_iterations = int(input("Enter maximum iterations: "))

# Run algorithm
best_x, best_value = hill_climbing(
    start,
    step_size,
    max_iterations
)

# Display final answer
print("\nBest Solution :", best_x)
print("Maximum Value :", best_value)


"""
Enter starting point: 3
Enter step size: 1
Enter maximum iterations: 10

Iteration 1
Current State : 3
Current Value : -4
Left Neighbour : 2 Value : 1
Right Neighbour : 4 Value : -11
Moving to Left Neighbour

Iteration 2
Current State : 2
Current Value : 1
Left Neighbour : 1 Value : 4
Right Neighbour : 3 Value : -4
Moving to Left Neighbour

Iteration 3
Current State : 1
Current Value : 4
Left Neighbour : 0 Value : 5
Right Neighbour : 2 Value : 1
Moving to Left Neighbour

Iteration 4
Current State : 0
Current Value : 5
Left Neighbour : -1 Value : 4
Right Neighbour : 1 Value : 4
No better neighbour found

Best Solution : 0
Maximum Value : 5
"""
