grid = [
    ["W", "L", "W", "W", "L", "W"],
    ["L", "L", "W", "W", "L", "W"],
    ["W", "L", "W", "W", "W", "W"],
    ["W", "", "W", "L", "L", "W"],
    ["W", "L", "W", "L", "L", "W"],
    ["W", "W", "W", "W", "W", "W"],
]

# 4

visited = set()

a = 0
b = 0

def largest_island(graph):
    biggest = 0

    for row in range(len(graph)):
        for col in range(len(graph[row])):
            size = explore(grid, row, col, visited)
            if size > biggest:
                biggest = size

    print(biggest)
    return biggest


def explore(grid, r, c, visited) -> bool:
    rowInBounds = 0 <= r and r < len(grid)
    colInBounds = 0 <= c and c < len(grid[0])

    if not rowInBounds or not colInBounds:
        return 0

    if (grid[r][c]) == "W":
        return 0

    pos = (r, c)

    if pos in visited:
        return 0

    visited.add(pos)
    size = 1

    size += explore(grid, r - 1, c, visited)
    size += explore(grid, r + 1, c, visited)
    size += explore(grid, r, c - 1, visited)
    size += explore(grid, r, c + 1, visited)

    return size


largest_island(grid)