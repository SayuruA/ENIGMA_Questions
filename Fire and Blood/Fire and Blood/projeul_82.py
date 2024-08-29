import heapq

def dijkstra(matrix):
    n = len(matrix)
    # Create a 2D list to store the minimum path sum
    min_path_sum = [[float('inf')] * n for _ in range(n)]
    min_path_sum[0][0] = matrix[0][0]
    # Define directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Priority queue to store vertices to explore
    pq = [(matrix[0][0], 0, 0)]
    
    while pq:
        cost, i, j = heapq.heappop(pq)
        if cost > min_path_sum[i][j]:
            continue
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                new_cost = cost + matrix[ni][nj]
                if new_cost < min_path_sum[ni][nj]:
                    min_path_sum[ni][nj] = new_cost
                    heapq.heappush(pq, (new_cost, ni, nj))
    
    return min_path_sum[n-1][n-1]

# Example usage:
n = int(input())
M = [ input().split(',') for i in range(n) ]
M = [[ int(M[row][col]) for col in range(n)] for row in range(n)]

min_sum = dijkstra(M)
print(min_sum)

