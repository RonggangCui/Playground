import random
from collections import Counter

# Number of simulations
num_simulations = 1000

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

# Flatten the list of lists into a single list of cycle lengths
total_cycle_lengths = [length for sublist in all_cycle_lengths for length in sublist]

# Calculate the frequency of each cycle length
length_counts = Counter(total_cycle_lengths)

# Prepare the list of cycle lengths and their corresponding weights
cycle_lengths = list(length_counts.keys())
weights = list(length_counts.values())

# Normalize the weights to create probabilities
total_counts = sum(weights)
probabilities = [w / total_counts for w in weights]

# Simulate picking a random number 1000 times based on the weights
num_picks = 1000
random_picks = random.choices(cycle_lengths, weights=weights, k=num_picks)

# Calculate the chance of the picked numbers being greater than 50
count_greater_than_50 = sum(1 for pick in random_picks if pick > 50)
chance = count_greater_than_50 / num_picks

# Print the chance
print(f"The chance of the picked number being greater than 50 is approximately {chance:.4f}")
