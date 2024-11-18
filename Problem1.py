import random

# Number of simulations
num_simulations = 10000
count_greater_than_50 = 0

# Store all cycle lengths from all simulations
all_cycle_lengths = []

for sim_num in range(1, num_simulations + 1):
    # Generate an array with contents 0-99 in a shuffled order
    arr = list(range(100))
    random.shuffle(arr)
    
    unused_indices = set(range(100))
    cycle_lengths = []
    
    # Continue until all numbers are divided into sets
    while unused_indices:
        # Pick a random initial index not already used
        initial_index = random.choice(list(unused_indices))
        current_index = initial_index
        current_cycle = set()
    
        # Follow the mapping until the value equals the initial index
        while True:
            current_cycle.add(current_index)
            unused_indices.remove(current_index)
            next_index = arr[current_index]
            if next_index == initial_index:
                break
            current_index = next_index
    
        # Record the length of the current cycle
        cycle_lengths.append(len(current_cycle))
    
    # Append the cycle lengths of the current simulation
    all_cycle_lengths.append(cycle_lengths)
    
    # Check if any cycle length is greater than 50
    if any(length > 50 for length in cycle_lengths):
        count_greater_than_50 += 1

    # if cycle_lengths[0] > 50:
    #     count_greater_than_50 += 1


    # Print the cycle lengths for the current simulation
    print(f"Simulation {sim_num}: Cycle Lengths = {cycle_lengths}")

# Calculate the chance
chance = count_greater_than_50 / num_simulations

print(f"\nOut of {num_simulations} simulations, {count_greater_than_50} had a set length greater than 50.")
print(f"The chance of any set length greater than 50 is approximately {chance:.4f}")

