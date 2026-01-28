#gas station circuit problem
def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    total_gas = 0
    start = 0
    for i in range(len(gas)):
        total_gas += gas[i] - cost[i]
        if total_gas < 0:
            total_gas = 0
            start = i + 1

    return start

# Example usage
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

start_station = can_complete_circuit(gas, cost)
print("Starting gas station index:", start_station)  # Output: Starting gas station index: 3
