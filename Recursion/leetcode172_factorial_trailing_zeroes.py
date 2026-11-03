from pathlib import Path
import sys

current_folder = Path(__file__).resolve().parent
sys.stdout = open(current_folder / 'output.txt', 'w')
sys.stdin = open(current_folder / 'input.txt', 'r')

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0: 
            return 0
        return n // 5 + self.trailingZeroes(n // 5)

    # TC = (logN)


def solution() -> None:
    n = int(input())
    sol = Solution()
    print(sol.trailingZeroes(n) )

if __name__ == "__main__":
    solution()