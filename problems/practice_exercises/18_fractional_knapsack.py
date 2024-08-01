def fractional_knapsack(capacity, weights, values):
    index = list(range(len(values)))
    ratio = [v/w for v, w in zip(values, weights)]
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_value = 0
    for i in index:
        if weights[i] <= capacity:
            capacity -= weights[i]
            max_value += values[i]
        else:
            max_value += values[i] * (capacity / weights[i])
            break

    return max_value

if __name__ == "__main__":   
    capacity = 50
    values = [60, 100, 120] 
    weights = [20, 50, 30]
    print(fractional_knapsack(capacity, weights, values))

    capacity = 10
    values = [500] 
    weights = [30]
    print(fractional_knapsack(capacity, weights, values))
