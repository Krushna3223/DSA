# s=6
# Q=[None]*s
# print(Q)
# f=-1
# r=-1

# def insert(data):
#     global r,f
#     if r==(len(Q)-1):
#         print("Full")
#     else:
#         r+=1
#         Q[r]=data
#         if f==-1:
#             f+=1

# def delete():
#     global r,f
#     if f==-1 or f>r:
#         print("Empty")
#     else:
#         x=Q[f]
#         f+=1
#         print("Deleted",x)

# def display():
#     global r,f
#     if f==-1 or f>r:
#         print("Empty")
#     else:
#         print("[",end="")
#         for i in range(f,len(Q)):
#             print(Q[i],end=",")
#         print("]")

# insert('A')
# insert('B')
# insert('C')
# insert('D')
# insert('E')
# insert('F')
# print(Q)
# insert('G')
# print(Q)
# delete()
# delete()
# delete()
# delete()
# delete()
# delete()
# print(Q)
# display()


# stack=[]
# def push( data ):
#     stack.append(data)
#     print(data,"Pushed")

# def pop():
#     if len(stack)>0:
#         x=stack.pop()
#         print(x,"Popped")
#         return x
#     else:
#         print ("Empty")


# Name :- Payal Anil Bhosale
# Roll No :- AI 2104
# from collections import deque
# def bfs(graph,start):
#     visited=set()
#     queue=deque([start])
#     visited.add(start)
#     while queue:
#         node=queue.popleft()
#         print(node,end=" ")
#         if node not in graph:
#             continue
#         for neighbour in graph[node]:
#             if neighbour not in visited:
#                  visited.add(neighbour)
#                  queue.append(neighbour)      
# graph={
#    'A':['M','N'],
#    'M':['P','E'],
#    'N':['S','T','U'],
#    'P':['Q','R'],
#    }
# print("output of above graph")
# bfs(graph,'A')



# Name :- Payal Anil Bhosale
# Roll No :- AI 2104
# def dfs_trav(graph, node, visited=None):
#     if visited is None:
#         visited = set()
#         if node not in visited:
#             print(node, end="")
#             visited.add(node)
#             for neigh in graph[node]:
#                 dfs_trav(graph, neigh, visited)
# graph = {
#     'P': ['A', 'Y'],
#     'A': ['Y', 'L'],
#     'Y': ['B'],
#     'Y': [],
#     'L': ['B'],
#     'B': []
# }
# print("Depth First Search starting from P:")

# def dfs_trav(graph, start):
#     visited = set()
#     stack = [start]

#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             visited.add(node)
#             print(node, end = " ")
#             stack.extend(reversed(graph[node]))

# dfs_trav(graph, 'P')


# Name :- Payal Anil Bhosale
# Roll No :- AI 2104
# from collections import deque
# def get_neighbours(state):
#     moves = []
#     idx = state.index('0')
#     r, c = divmod(idx, 3) 
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     for dr, dc in directions:
#         nr, nc = r + dr, c + dc
#         if 0 <= nr < 3 and 0 <= nc < 3:
#             new_idx = nr * 3 + nc
#             new_state = list(state)
#             new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
#             moves.append(''.join(new_state))
#     return moves

# def bfs(start, goal):
#     queue = deque([(start, [])])
#     visited = set([start])

#     while queue:
#         state, path = queue.popleft()
#         if state == goal:
#             return path

#         for neighbour in get_neighbours(state):
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 queue.append((neighbour, path + [neighbour]))
#     return None


# start = "123047568"
# goal = "123456780"

# result = bfs(start, goal)

# if result:
#     print(f"Solution found in {len(result) - 1} moves!\n")
#     for step in result:
#         for i in range(0, 9, 3):
#             print(step[i:i+3])
#         print()
#     print(end="")
# else:
#     print("No solution found.")
# print("Number of moves = ",len(result) - 1)



# Name :- Payal Anil Bhosale
# Roll No :- AI 2104
# def is_safe(board,row,col):
#     for i in range(row):
#         if (board[i] == col or
#             board[i] - i == col - row or 
#             board[i] + i == col + row):
#             return False
#     return True 

# def solve(board,row,n):
#     if row == n:
#         print_board(board,n)
#         return
#     for col in range(n):
#         if is_safe(board,row,col):
#             board[row] = col
#             solve(board,row + 1,n)
#             board[row] = -1
            
# def print_board(board,n):
#     for i in range(n):
#         row = ['.'] * n 
#         row[board[i]] = 'Q'
#         print(' '.join(row))
#     print()
    
# n = 8
# board = [-1] * n 
# print("Solutions for the 8 Queens problem:")
# solve(board, 0, n)



# Name :- Payal Anil Bhosale
# Roll No :- AI 2104
# from itertools import permutations

# def calculate_distance(route , distance_matrix):
#   total_distance = 0
#   for i in range(len(route) - 1):
#     total_distance += distance_matrix[route[i]][route[i + 1]]
#   total_distance += distance_matrix[route[-1]][route[0]]
#   return total_distance

# def tsp_brute_force(distance_matrix):
#   n = len(distance_matrix)
#   cities = list(range(n))
#   all_routes = permutations(cities)
  
#   min_distance = float('inf')
#   best_route = None
  
#   for route in all_routes:
#     distance = calculate_distance(route, distance_matrix)
#     if distance < min_distance:
#       min_distance = distance
#       best_route = route
#   return best_route, min_distance

# distance_matrix = [
#   [0, 13, 18, 30],
#   [13, 0, 45, 25],
#   [18, 45, 0, 50],
#   [30, 25, 50, 0],
# ]

# best_route, min_distance = tsp_brute_force(distance_matrix)
# print("Best route:", best_route)
# print("Minimum distance:", min_distance)



# Name :- Payal Anil Bhosale
# Roll No :- AI 2104

# def display_board(board):
#     for row in board:
#         print(" | ".join(row))
#     print("-" * 8)

# def check_winner(board,player):
#     win_conditions = [
#         [(0,0), (0,1), (0,2)], [(1,0), (1,1), (1,2)], [(2,0), (2,1), (2,2)],
#         [(0,0), (1,0), (2,0)], [(0,1), (1,1), (2,1)], [(0,2), (1,2), (2,2)], 
#         [(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)],      
#     ]   
#     return any(all(board[r][c] == player for r,c in condition) for condition in win_conditions)

# def is_full(board):
#     return all(cell != " " for row in board for cell in row)

# def play_game():
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     current_player = "X"
#     while True:
#         display_board(board)
#         move = int(input(f"Player {current_player}, enter your move (1-9):")) - 1
#         row,col = divmod(move,3)
#         if move < 0 or move > 8:
#             print("Invalid input! Choose a number between 1 and 9")
#             continue
#         if board[row][col] == " ":
#             board[row][col] = current_player
#         else:
#             print("That spot is already taken! Try again.")
#             continue
#         if check_winner(board,current_player):
#             display_board(board)
#             print(f"Player {current_player} wins!")
#             break
#         if is_full(board):
#             display_board(board)
#             print("It's a tie!")
#             break
#         current_player = "O" if current_player == "X" else "X"
# play_game()




# Name :- Payal Anil Bhosale
# Roll No :- AI 2104
# def is_safe(region, color, assignment, neighbors):
#     for neighbor in neighbors[region]:
#         if assignment.get(neighbor) == color:
#             return False
#     return True

# def solve_map_coloring(assignment, regions, colors, neighbors):
#     if len(assignment) == len(regions):
#         return assignment
#     region = select_unassigned_region(assignment, regions)
#     for color in colors:
#         if is_safe(region, color, assignment, neighbors):
#             assignment[region] = color
#             result = solve_map_coloring(assignment, regions, colors, neighbors)
#             if result:
#                 return result
#             del assignment[region]
#     return None

# def select_unassigned_region(assignment, regions):
#     for region in regions:
#         if region not in assignment:
#             return region

# if __name__ == "__main__":
#     regions = ["P", "Q", "R", "T"]

#     neighbors = {
#         "P": ["Q", "R"],
#         "Q": ["P", "T"],
#         "R": ["P", "T"],
#         "T": ["R", "Q"],
#     }
#     colors = ["Orange", "White", "Yellow"]

#     assignment = {}
#     solution = solve_map_coloring(assignment, regions, colors, neighbors)
#     if solution:
#         print("Solution found!")
#         for region, color in solution.items():
#             print(f"Region {region}: {color}")
#     else:
#         print("No solution exists.")



# Name :- Payal Anil Bhosale
# Roll No :- AI 2104
# import math

# def alphabeta(depth, nodeIndex, isMax, values, alpha, beta):
#     if depth == len(values).bit_length() - 1:
#         return values[nodeIndex]

#     if isMax:
#         maxEval = -math.inf
#         for i in range(2):
#             eval = alphabeta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
#             maxEval = max(maxEval, eval)
#             alpha = max(alpha, eval)
#             if beta <= alpha:
#                 break
#         return maxEval
#     else:
#         minEval = math.inf
#         for i in range(2):
#             eval = alphabeta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
#             minEval = min(minEval, eval)
#             beta = min(beta, eval)
#             if beta <= alpha:
#                 break
#         return minEval

# if __name__ == "__main__":
#     values = [-2, 7, 4, 1, 9, -6, 3, 0]

#     result = alphabeta(0, 0, True, values, -math.inf, math.inf)
#     print(f"The optimal value is: {result}")

