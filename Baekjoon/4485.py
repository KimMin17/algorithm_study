from heapq import heappush, heappop

INF = 100000000

count = 1

while True:
    
    n = int(input())
    if n == 0: break
    
    arr = [[INF for _ in range(n+2)] for _ in range(n+2)]
    dist = [[INF for _ in range(n+2)] for _ in range(n+2)]
    visited = [[False for _ in range(n+2)] for _ in range(n+2)]

    for i in range(1, n+1):
        arr_input = list(map(int, input().split(" ")))
        for j in range(0, n):
            arr[i][j+1] = arr_input[j]

    for i in range(n+2):
        for j in range(n+2):
            if arr[i][j] == INF:
                visited[i][j] = True

    #pq = PriorityQueue()
    pq = []
    dist[1][1] = 0

    #pq.put((arr[1][1], 1, 1))
    heappush(pq, (arr[1][1], 1, 1))

    gaps = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    
    #while pq.empty() == False:
    while pq:
        #cur_dist, cur_x, cur_y = pq.get()
        cur_dist, cur_x, cur_y = heappop(pq)
        if cur_x == n and cur_y == n:
            print("Problem {}: {}".format(count, cur_dist))
            break
        for gap in gaps:
            new_x = cur_x + gap[0]
            new_y = cur_y + gap[1]

            if visited[new_x][new_y] == True: continue
            
            if cur_dist + arr[new_x][new_y] < dist[new_x][new_y]:
                dist[new_x][new_y] = cur_dist + arr[new_x][new_y]
                heappush(pq, (dist[new_x][new_y], new_x, new_y))

        visited[cur_x][cur_y] = True
    
    count += 1