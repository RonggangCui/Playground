import random

# Number of simulations
num_simulations = 10000
count_greater_than_50 = 0

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
    
    # Pick a random cycle length with weights proportional to the lengths themselves
    weights = cycle_lengths  # Weights are proportional to the cycle lengths
    picked_length = random.choices(cycle_lengths, weights=weights, k=1)[0]
    
    # Check if the picked length is greater than 50
    if picked_length > 50:
        count_greater_than_50 += 1

    # Print the picked number and all cycle lengths
    print(f"Simulation {sim_num}: Cycle Lengths = {cycle_lengths}, Picked Length = {picked_length}")

# Calculate the chance
chance = count_greater_than_50 / num_simulations

# Print the chance
print(f"\nThe chance of the picked number being greater than 50 is approximately {chance:.4f}")

