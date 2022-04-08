grid = [
    ["W", "L", "W", "W", "L", "W"],
    ["L", "L", "W", "W", "L", "W"],
    ["W", "L", "W", "W", "W", "W"],
    ["W", "W", "W", "L", "L", "W"],
    ["W", "L", "W", "L", "L", "W"],
    ["W", "W", "W", "W", "W", "W"],
]

visited = set()

a = 0
b = 0

def island_count(graph):
    count = 0

    for row in range(len(graph)):
        for col in range(len(graph[row])):
            if explore(grid, row, col, visited):
                count += 1

    print(count)
    return count


def explore(grid, r, c, visited) -> bool:
    rowInBounds = 0 <= r and r < len(grid)
    colInBounds = 0 <= c and c < len(grid[0])

    if not rowInBounds or not colInBounds:
        return False

    if (grid[r][c]) == "W":
        return False

    pos = (r, c)

    if pos in visited:
        return False

    visited.add(pos)

    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)

    return True


island_count(grid)
