from pulp import LpVariable, LpProblem, LpStatus, value, LpMinimize

# Define variables
VFR = LpVariable("VFR", 0, None)
OMS = LpVariable("OMS", 0, None)
E = LpVariable("E", 0, None)
M = LpVariable("M", 0, None)
JC = LpVariable("JC", 0, None)

# Define the Problem
prob = LpProblem("problem", LpMinimize)

# Define Constraints
prob += 510*VFR + 290*OMS + 142*E + 130*M + 280*JC <= 35000
prob += 230*VFR + 110*OMS + 143*E + 130*M + 120*JC >= 14000
prob += 6*VFR + 2*OMS + 12.5*E + 8*M + 22*JC >= 350
prob += 2*E + 2.5*M >= 140
prob += 50*OMS + 56*E + 300*M +10*JC >= 9100
prob += 0.9*VFR + 0.8*OMS + 1.8*E + 0.6*JC >= 126
prob += 190*VFR + 280*OMS + 138*E + 400*M + 130*JC >= 32900

# Define Objective Function
prob += 1.05*VFR + 1.14*OMS + 1.17*E + 0.19*M + 1.80*JC

# Solve the Problem
status = prob.solve()
print(f"Problem")
print(f"status={LpStatus[status]}")

# Print the Results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")

print(f"Objective = {value(prob.objective)}")
print(f"")

##############################################################
# Define variables
VFR = LpVariable("VFR", 1, None)
OMS = LpVariable("OMS", 1, None)
E = LpVariable("E", 1, None)
M = LpVariable("M", 1, None)
JC = LpVariable("JC", 1, None)

# Define the Problem
prob = LpProblem("problem", LpMinimize)

# Define Constraints
prob += 510*VFR + 290*OMS + 142*E + 130*M + 280*JC <= 35000
prob += 230*VFR + 110*OMS + 143*E + 130*M + 120*JC >= 14000
prob += 6*VFR + 2*OMS + 12.5*E + 8*M + 22*JC >= 350
prob += 2*E + 2.5*M >= 140
prob += 50*OMS + 56*E + 300*M +10*JC >= 9100
prob += 0.9*VFR + 0.8*OMS + 1.8*E + 0.6*JC >= 126
prob += 190*VFR + 280*OMS + 138*E + 400*M + 130*JC >= 32900

# Define Objective Function
prob += 1.05*VFR + 1.14*OMS + 1.17*E + 0.19*M + 1.80*JC

# Solve the Problem
status = prob.solve()
print(f"Problem")
print(f"status={LpStatus[status]}")

# Print the Results
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")

print(f"Objective = {value(prob.objective)}")
print(f"")

#########################################################
# LLM Solution

import numpy as np
from scipy.optimize import linprog

# Cost vector (c)
cost = np.array([3.0, 0.5, 0.8, 1.2, 2.5, 0.7])  # Costs of food items

# Nutritional content matrix (A)
A = np.array([
    [-165, -130, -55, -103, -188, -23],  # Calories
    [-31, -2.7, -4.2, -8, -8, -2.9],    # Protein
    [-70, -1, -30, -98, -140, -24],     # Sodium
    [0, 0, -78, -100, 0, -40],          # Vitamin D
    [-12, -10, -47, -300, -17, -99],    # Calcium
    [-0.9, -0.2, -0.7, -0.1, -1.9, -2.7], # Iron
    [-256, -35, -288, -366, -208, -558] # Potassium
])

# Nutritional requirements (b)
b = np.array([-2000, -50, -1000, -400, -1000, -18, -3500])

# Solve the linear programming problem
result = linprog(c=cost, A_ub=A, b_ub=b, bounds=(0, None), method='highs')

# Display the results
if result.success:
    print("Optimal solution found!")
    print("Quantities of food items to purchase (units):")
    food_items = ["Chicken Breast", "Rice", "Broccoli", "Milk", "Peanut Butter", "Spinach"]
    for food, quantity in zip(food_items, result.x):
        print(f"{food}: {quantity:.2f} units")
    print(f"Minimum cost: ${result.fun:.2f}")
else:
    print("No solution found!")