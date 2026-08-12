class Solution:
    def kthLargestValue(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        temp = [[0]*m for _ in range(n)]
        temp[0][0] = grid[0][0]
        for j in range(1,m):
            temp[0][j] = temp[0][j-1] ^grid[0][j]
            
        for i in range(1,n):
            temp[i][0] = temp[i-1][0] ^grid[i][0]

        for i in range(1,n):
            for j in range(1,m):
                temp[i][j] =  grid[i][j]  ^ temp[i-1][j] ^temp[i][j-1] ^ temp[i-1][j-1]

        arr = []
        for row in temp:
            arr.extend(row)
        arr.sort(reverse = True)
        return arr[k-1]

        temp = [[0]*m for _ in range(n)]
        pq = []
        for i in range(n):
            for j in range(m):
                temp[i][j] = grid[i][j]
                
                if j>0:
                    temp[i][j] ^= temp[i][j-1] 

                
                if i>0:
                    temp[i][j] ^= temp[i-1][j] 
                
                if i>0 and j>0:
                    temp[i][j] ^= temp[i-1][j-1]

                heapq.heappush(pq, temp[i][j])
                while len(pq)>k:
                    heapq.heappop(pq)

        return pq[0]
