from pathlib import Path
import sys

current_folder = Path(__file__).resolve().parent
sys.stdout = open(current_folder / 'output.txt', 'w')
sys.stdin = open(current_folder / 'input.txt', 'r')

class Solution:
    # Compute n factorial
    def fact(self, n) -> int: 
        if n == 0: 
            return 1

        return self.fact(n-1) * n
    

    def trailingZeroes(self, n: int) -> int:
        n_fact = self.fact(n) # O(n)
        print(n_fact)

        counter = 0 
        while n_fact > 0: 
            last_digit = n_fact % 10
            n_fact //= 10 
            if (last_digit != 0): 
                break
            
            counter += 1
        
        return counter

    # TC = O(n)


def solution() -> None:
    n = int(input())
    sol = Solution()
    print(sol.trailingZeroes(n) )

if __name__ == "__main__":
    solution()