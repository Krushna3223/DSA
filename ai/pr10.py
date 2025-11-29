# Function to check if the current color assignment is safe for a region
def is_safe(region, color, assignment, neighbors):
    for neighbor in neighbors[region]:
        if assignment.get(neighbor) == color:
            return False
    return True

# Helper function to select the next unassigned region
def select_unassigned_region(assignment, regions):
    for region in regions:
        if region not in assignment:
            return region
    return None 

# Backtracking function to solve the map coloring problem
def solve_map_coloring(assignment, regions, colors, neighbors):
    if len(assignment) == len(regions):
        return assignment
    
    region = select_unassigned_region(assignment, regions)
    
    for color in colors:
        if is_safe(region, color, assignment, neighbors):
            assignment[region] = color
            
            result = solve_map_coloring(assignment, regions, colors, neighbors)
            
            if result:
                return result
            
            del assignment[region]
            
    return None

# --- NEW INPUT VALUES ---
if __name__ == "__main__":
    # Define the regions: A, B, C, D
    regions = ["A", "B", "C", "D"]
    
    # Define the neighbors (A-B-C-D chain graph)
    neighbors = {
        "A": ["B"],
        "B": ["A", "C"],
        "C": ["B", "D"],
        "D": ["C"]
    }
    
    # Define the available colors: Red and Green (M=2)
    colors = ["Red", "Green"]
    
    assignment = {}
    
    solution = solve_map_coloring(assignment, regions, colors, neighbors)
    
    if solution:
        print("Solution found!")
        for region, color in solution.items():
            print(f"Region {region}: {color}")
    else:
        print("No solution exists with the available colors.")