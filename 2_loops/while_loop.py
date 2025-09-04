# You want to simulate human walking by taking steps until a certain distance is covered.
# Your goal is to walk 30 steps. Also print the distance covered after every step. Assume each step covers 0.7 meter.

# TO DO : use while loop to simulate walking, keep increasing the step count until it reaches 30. Also keep printing the distance covered after each step.

steps = 0
distance_per_step = 0.7  # in meters
target_steps = 30

while steps < target_steps:
    steps += 1
    distance_covered = steps * distance_per_step
    print(f"Step {steps}: Distance covered = {distance_covered} meters")

print("You have reached your target of 30 steps!")
