def car_fueling(d, m, stops):
    """
    Calculate the minimum number of refills needed to reach the destination.

    :param d: int - Total distance between the starting point and the destination.
    :param m: int - Maximum distance a car can travel on a full tank.
    :param stops: list of int - Distances of gas stations from the starting point.
    :return: int - Minimum number of refills needed or -1 if not possible.
    """
    # We add the starting point 0 and the destination d to the list of stops. 
    # This helps in simplifying the logic, as we treat the start and the end as 
    # gas stations.
    stops = [0] + stops + [d]
    num_refills, current_refill = 0, 0

    
    # This loop runs until the car reaches the last stop (which is the destination).
    # current_refill < len(stops) - 1 ensures we are not beyond the last stop.
    while current_refill < len(stops) - 1:
        last_refill = current_refill

        # This loop moves current_refill to the farthest stop we can reach 
        # without refueling, starting from last_refill.
        while (
            current_refill < len(stops) - 1
            and stops[current_refill + 1] - stops[last_refill] <= m
        ):
            current_refill += 1

        # If current_refill did not move forward, it means we cannot reach the next 
        # stop from last_refill, making it impossible to reach the destination. 
        # Hence, return -1.
        if current_refill == last_refill:
            return -1

        # If current_refill has moved forward and we haven't reached the destination yet, 
        # increment the num_refills.
        if current_refill < len(stops) - 1:
            num_refills += 1

    return num_refills


# Example 1
d = 950
m = 400
stops = [200, 375, 550, 750]
print(f"Minimum stops: {car_fueling(d, m, stops)}")

# Example 2
d = 10
m = 3
stops = [1, 2, 5, 9]
print(f"Minimum stops: {car_fueling(d, m, stops)}")

# Example 3
d = 200
m = 250
stops = [100, 150]
print(f"Minimum stops: {car_fueling(d, m, stops)}")