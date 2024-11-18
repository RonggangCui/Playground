import random
from functools import reduce
import operator

# Number of simulations
num_simulations = 10000

# Initialize counts and denominators for picks 1 to 10
counts = [0] * 10          # Counts of picks not greater than 50 at each pick
denominators = [0] * 10    # Number of simulations where pick n was made

for sim_num in range(1, num_simulations + 1):
    # Generate an array with contents 0-99 in a shuffled order
    arr = list(range(100))
    random.shuffle(arr)
    
    unused_indices = set(range(100))
    cycle_lengths = []
    
    # Continue until all numbers are divided into cycles
    while unused_indices:
        # Pick a random initial index not already used
        initial_index = random.choice(list(unused_indices))
        current_index = initial_index
        current_cycle = set()
    
        # Follow the mapping until the cycle is complete
        while True:
            current_cycle.add(current_index)
            unused_indices.remove(current_index)
            next_index = arr[current_index]
            if next_index == initial_index:
                break
            current_index = next_index
    
        # Record the length of the current cycle
        cycle_lengths.append(len(current_cycle))
    
    # Initialize flag to determine whether to continue picking
    continue_picking = True
    
    # For each pick from 1 to 10
    for n in range(10):
        if continue_picking:
            # Increment the denominator for this pick
            denominators[n] += 1
            
            # Pick a random cycle length with weights proportional to the lengths themselves
            weights = cycle_lengths  # Weights are proportional to the cycle lengths
            picked_length = random.choices(cycle_lengths, weights=weights, k=1)[0]
            
            # Check if the picked length is not greater than 50
            if picked_length <= 50:
                counts[n] += 1
                # Continue to next pick
            else:
                # Picked length is greater than 50, stop further picks
                continue_picking = False
        else:
            # Do not increment denominator or count if we have stopped picking
            pass

# Calculate and print the chance for each pick
print("Chances of the picked number not being greater than 50 at each pick position:")
chances = []  # List to store the chances for each pick
for n in range(10):
    if denominators[n] > 0:
        chance = counts[n] / denominators[n]
        chances.append(chance)
        print(f"Pick {n+1}: Chance = {chance:.4f}")
    else:
        # If denominator is zero, it means no simulations reached this pick
        chances.append(1.0)  # Since no picks were made, we can consider the chance as 1 for multiplication
        print(f"Pick {n+1}: No data (no simulations reached this pick)")

# Calculate the product of all chances
product_of_chances = reduce(operator.mul, chances, 1)

# Print the product of all chances
print(f"\nProduct of all chances: {product_of_chances:.4f}")

