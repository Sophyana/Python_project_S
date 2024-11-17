class Maze:
    def __init__(self, N):
        self.N = N
        self.grid = [["█" for _ in range(2 * N + 1)] for _ in range(2 * N + 1)]
        for i in range(1, 2 * N, 2):
            for j in range(1, 2 * N, 2):
                self.grid[i][j] = "·"

    def __str__(self):
        return "\n".join("".join(row) for row in self.grid)

    def __setitem__(self, key, value):
        (x0, y0), (x1, y1) = (key[0], key[1].start), (key[1].stop, key[2])
        if value not in {"·", "█"}:
            return

        if x0 == x1:
            for j in range(min(y0, y1), max(y0, y1) + 1):
                self.grid[2 * x0 + 1][2 * j + 1] = value
                if j < max(y0, y1):
                    self.grid[2 * x0 + 1][2 * j + 2] = value

        elif y0 == y1:
            for i in range(min(x0, x1), max(x0, x1) + 1):
                self.grid[2 * i + 1][2 * y0 + 1] = value
                if i < max(x0, x1):
                    self.grid[2 * i + 2][2 * y0 + 1] = value

    def __getitem__(self, key):
        (x0, y0), (x1, y1) = (key[0], key[1].start), (key[1].stop, key[2])
        visited = set()
        return self._explore(2 * x0 + 1, 2 * y0 + 1, 2 * x1 + 1, 2 * y1 + 1, visited)

    def _explore(self, x, y, target_x, target_y, visited):
        if (x, y) == (target_x, target_y):
            return True
        visited.add((x, y))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.grid[0]) and 0 <= ny < len(self.grid):
                if self.grid[ny][nx] == "·" and (nx, ny) not in visited:
                    if self._explore(nx, ny, target_x, target_y, visited):
                        return True
        return False


import sys
exec(sys.stdin.read())
