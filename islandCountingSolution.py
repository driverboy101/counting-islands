class Solution(object):

    #function that returns the number of islands in a given grid
    def numIslands(self, grid):
        
        self.grid = grid        #stores our full map grid
        self.count = 0          #stores the running total number of islands
        self.visited = []       #stores a list of visited positions on our grid

        #iterates through grid, counting unique islands
        for x in range(0, len(self.grid)):          
            for y in range(0, len(self.grid[x])):
                if (self.grid[x][y] == "1" and (x, y) not in self.visited):
                    self.count = self.count + 1
                    self.findIsland(x, y)
                    
        return self.count


    #helper function - checks all spaces around a spot to find the full size of one island
    def findIsland(self, x, y):         
        self.visited.append((x, y))
        if (self.grid[x][y]) == "0":
            return
        if (x > 0 and (x-1, y) not in self.visited):
            self.findIsland(x-1, y)
        if (x < len(self.grid)-1 and (x+1, y) not in self.visited):
            self.findIsland(x+1, y)
        if (y > 0 and (x, y-1) not in self.visited):
            self.findIsland(x, y-1)
        if (y < len(self.grid[x])-1 and (x, y+1) not in self.visited):
            self.findIsland(x, y+1)


solution = Solution()

#returns 1
print(solution.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))

#returns 3
print(solution.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

#returns 4
print(solution.numIslands([["1","1","0","0","0"],["0","1","0","1","0"],["1","0","0","1","1"],["1","1","0","0","0"],["0","0","1","1","0"]]))

#returns 10
print(solution.numIslands([["1","0","1","0","1"],["0","1","0","1","0"],["1","0","1","0","1"],["0","1","0","1","0"]]))
    
