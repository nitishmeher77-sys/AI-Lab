# EXP-3 HILL CLIMBING ALGORITHEM


# objective function
def objective_function(x):
  return -(x**2)+10 # EXAMPLE OF FUNCTION

# HILL CLIMBING FUNCTION
def hill_climbing(start,step_size, max_iteration):
    current=start
    current_value=objective_function(current)
    for i in range (max_iteration):
        left=current-step_size
        right=current+step_size

        left_value=objective_function(left)
        right_value=objective_function(right)

        # Move to the better neighbour
        if left_value>current_value:
            current=left
            current_value=left_value
        elif right_value>current_value:
            current=right
            current_value=right_value
        else:
            break
    return current,current_value

# mAinprogram
start=float(input("enter the start value:"))
step_size=float(input("enter the step size:"))
max_iteration=int(input("enter the max iteration:"))
best_position,best_value=hill_climbing(start,step_size,max_iteration)
print("best position:",best_position)
print("best value:",best_value)

'''--------OUTPUT--------
enter the start value:1
enter the step size:2
enter the max iteration:3
best position: 1.0
best value: 9.0




'''