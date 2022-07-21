# Counting Islands

## Main Task
Given an ```m x n``` 2D grid which represents a map of ```'1'```s (land) and ```'0'```s (water), return *the number of islands*.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

#### Example 1:
```
[["1","1","1","1","0"],
 ["1","1","0","1","0"],
 ["1","1","0","0","0"],
 ["0","0","0","0","0"]]
 
-- Output: 1 --
```

#### Example 2:
```
[["1","1","0","0","0"],
 ["1","1","0","0","0"],
 ["0","0","1","0","0"],
 ["0","0","0","1","1"]]
 
-- Output: 3 --
```

#### Example 3:
```
[["1","1","0","0","0"],
 ["0","1","0","1","0"],
 ["1","0","0","1","1"],
 ["1","1","0","0","0"],
 ["0","0","1","1","0"]]

-- Output: 4 --
```

#### Example 4:
```
[["1","0","1","0","1"],
 ["0","1","0","1","0"],
 ["1","0","1","0","1"],
 ["0","1","0","1","0"]]

-- Output: 10 --
```

## Bonus Tasks
1. As well as returning the number of islands, also return the size of the largest island on the grid.

2. Now assume the map *wraps around* (i.e. going above the top of the map leads you to the bottom, and going off of one side takes you to the other). Adapt your code to calculate the number of islands with this new assumption.
    #### Example 1:
    ```
    [["0","0","0","0","0"],
     ["1","1","0","1","1"],
     ["1","1","0","1","1"],
     ["0","0","1","0","0"]]

    -- Output: 2 --
    ```
    
    #### Example 2:
    ```
    [["1","0","0","0","1"],
     ["0","0","0","0","0"],
     ["0","0","0","0","0"],
     ["1","0","0","0","1"]]

    -- Output: 1 --
    ```
    
    #### Example 3:
    ```
    [["1","0","0","0","0"],
     ["0","0","0","0","0"],
     ["0","0","0","0","0"],
     ["0","0","0","0","1"]]

    -- Output: 0 --
    ```
