# https://leetcode.com/problems/number-of-islands/?envType=study-plan-v2&envId=top-interview-150

from typing import Dict, List


LAND = "1"
WATER = "0"


class Solution:

    def _getNodeTag(self, x, y) -> str:
        return f"{x},{y}"

    def findAdjacents(self, grid, visited, cur) -> List[Dict[str, int]]:
        res = []
        x, y = cur[0], cur[1]
        for n in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
            if n[0] < 0 or n[0] >= len(grid):
                continue
            if n[1] < 0 or n[1] >= len(grid[cur[0]]):
                continue
            tag = self._getNodeTag(n[0], n[1])
            if tag in visited:
                continue
            res.append(n)
        return res
    
    def walkIsland(self, grid, visited, island_nr, x, y):
        q = [(x, y)]  # nodes to visit
        while len(q) > 0:
            cur = q.pop()  # last elem
            v = grid[cur[0]][cur[1]]
            tag = self._getNodeTag(cur[0], cur[1])
            if v == LAND and tag not in visited:
                visited[tag] = island_nr
                # find adjacent
                adj = self.findAdjacents(grid, visited, cur)
                q.extend(adj)

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {}  # if we visited a land we store the coordinates and
        # which land it belongs to
        island_nr = 0
        for r, _ in enumerate(grid):
            for c, _ in enumerate(grid[r]):
                tag = self._getNodeTag(r, c)
                if grid[r][c] == LAND and tag not in visited:
                    island_nr += 1
                    self.walkIsland(grid, visited, island_nr, r, c)

        return island_nr


