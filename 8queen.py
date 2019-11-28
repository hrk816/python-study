import sys
import time


class NQueen:
    def __init__(self, size=8):
        self.size = size
        self.fundamental = set()
        self.distinct = set()

    def solve(self):
        for x in range(self.size):
            self._backtrack(x, 0, [])

    def _backtrack(self, x, y, queens):
        if self._is_colision(queens, (x, y)):
            return
        queens.append((x, y))
        if y + 1 == self.size:
            solution = tuple(queens)
            if solution not in self.distinct:
                self.fundamental.add(solution)
                self._add_distinct_solutions(queens)
            queens.pop()
            return
        for x in range(self.size):
            self._backtrack(x, y+1, queens)
        queens.pop()

    def _is_colision(self, queens, candidate):
        for queen in queens:
            dx = queen[0] - candidate[0]
            dy = queen[1] - candidate[1]
            if dx == 0 or dy == 0 or dx == dy or dx == -dy:
                return True
        return False

    def _add_distinct_solutions(self, solution):
        max_index = self.size - 1
        distinct_solutions = [
            solution,
            [(x, max_index - y) for x, y in solution],  # 上下反転
            [(max_index - x, y) for x, y in solution],  # 左右反転
            [(max_index - y, max_index - x) for x, y in solution],  # y = x反転
            [(y, x) for x, y in solution],  # y = -x反転
            [(max_index - y, x) for x, y in solution],  # 90度回転
            [(max_index - x, max_index - y) for x, y in solution],  # 180度回転
            [(y, max_index - x) for x, y in solution]  # 270度回転
        ]
        for distinct_solution in distinct_solutions:
            distinct_solution.sort(key=lambda t: t[1])
            self.distinct.add(tuple(distinct_solution))


def pretty_print(solutions):
    for i, solution in enumerate(solutions, start=1):
        print(f'solution #{i}')
        for x, _ in solution:
            print('- ' * x + 'Q ' + '- ' * (len(solution) - x - 1))
        print()


if __name__ == '__main__':
    print('size, fundamental,    distinct,    time[us]')
    for size in range(1, int(sys.argv[1]) + 1):
        nQueen = NQueen(size)
        start = time.time_ns()
        nQueen.solve()
        end = time.time_ns()
        fund = len(nQueen.fundamental)
        dist = len(nQueen.distinct)
        duration = (end-start) // 1000
        print(f'{size:4d}, {fund:11d}, {dist:11d}, {duration:11,}')
