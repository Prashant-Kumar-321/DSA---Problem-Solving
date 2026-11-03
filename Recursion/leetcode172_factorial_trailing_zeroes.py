from pathlib import Path
import sys

current_folder = Path(__file__).resolve().parent
sys.stdout = open(current_folder / 'output.txt', 'w')
sys.stdin = open(current_folder / 'input.txt', 'r')

class Solution:
    def freq_factor_x(self, x, num) -> tuple[int, int]: 
        counter = 0
        while num % x == 0: 
            counter += 1
            num //= x
        
        return counter, num


    def trailingZeroes(self, n: int) -> int:
        counter_5 = 0
        counter_2 = 0
        
        for i in range(n, 0, -1): 
            freq_5, rem = self.freq_factor_x(5, i)
            freq_2, _ = self.freq_factor_x(2, rem)

            counter_5 += freq_5
            counter_2 += freq_2 

        return min(counter_5, counter_2)



    # TC = O(n)


def solution() -> None:
    n = int(input())
    sol = Solution()
    print(sol.trailingZeroes(n) )

if __name__ == "__main__":
    solution()