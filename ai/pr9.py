import math

def alphabeta(depth, nodeIndex, isMax, values, alpha, beta):
    if depth == len(values).bit_length() - 1:
        return values[nodeIndex]
    
    if isMax:
        maxEval = -math.inf
        for i in range(2):
            eval = alphabeta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
        
    else:
        minEval = math.inf
        for i in range(2):
            eval = alphabeta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

if __name__ == "__main__":
    values = [7, 2, 4, 9, 8, 1, 5, 3] 
    result = alphabeta(0, 0, True, values, -math.inf, math.inf)
    print(f"The optimal value is: {result}")