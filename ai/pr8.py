# Traveling Salesman Problem (TSP) - Brute-Force Solution

# Imports permutations, which generate all orderings of cities
from itertools import permutations

def calculate_distance(route, distance_matrix): 
    """
    Calculates the total distance of a given route (cycle).
    The route must return to the starting city.
    
    Args:
        route (tuple/list): The sequence of cities (e.g., (0, 1, 3, 2)).
        distance_matrix (list of lists): The cost matrix for travel between cities.
        
    Returns:
        int: The total distance of the closed route.
    """
    total_distance = 0
    
    # Add distance between consecutive cities
    # Loop goes up to the second-to-last city (i.e., range(len(route) - 1))
    for i in range(len(route) - 1):
        current_city = route[i]
        next_city = route[i + 1]
        total_distance += distance_matrix[current_city][next_city]
    
    # Add distance from the last city (route[-1]) back to the starting city (route[0])
    last_city = route[-1]
    first_city = route[0]
    total_distance += distance_matrix[last_city][first_city]
    
    return total_distance

def tsp_brute_force(distance_matrix):
    """
    Solves the Traveling Salesman Problem using the brute-force method
    by checking the distance of every possible route (permutation).
    
    Args:
        distance_matrix (list of lists): The cost matrix for travel between cities.
        
    Returns:
        tuple: A tuple containing the best route (tuple) and the minimum distance (int).
    """
    n = len(distance_matrix)  # Number of cities
    cities = list(range(n))  # Creates a list of city indices: [0, 1, ..., n-1]
    
    # Generates every ordering of cities (permutations of all city indices)
    all_routes = permutations(cities)
    
    min_distance = float('inf')  # Initialize minimum distance to infinity
    best_route = None  # Stores the route corresponding to the minimum distance

    # Iterate through all possible routes
    for route in all_routes:
        distance = calculate_distance(route, distance_matrix)
        
        # Check if the current route is better than the minimum found so far
        if distance < min_distance:
            min_distance = distance
            best_route = route

    return best_route, min_distance

# --- Execution Block ---

# Distance matrix for 4 cities (0, 1, 2, 3)
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Run the brute-force search
best_route, min_distance = tsp_brute_force(distance_matrix)

# Print the final results
print("Distance Matrix:")
for row in distance_matrix:
    print(row)
print("-" * 30)
print(f"Number of cities: {len(distance_matrix)}")
print(f"Total routes checked: {len(distance_matrix) - 1}!") # (n-1)! routes are checked
print("Best Route:", best_route)
print("Minimum distance:", min_distance)