from pathlib import Path
import sys

current_folder = Path(__file__).resolve().parent
sys.stdout = open(current_folder / 'output.txt', 'w')
sys.stdin = open(current_folder / 'input.txt', 'r')

import random

class Solution:
    def partition(self, nums: list[int], l: int, r: int) -> tuple[int, int]: 

        # Pick a random index between l and r
        ran = random.randint(l, r) 
        pivot = nums[ran]
        nums[ran], nums[r] = nums[r], nums[ran]

        g = l
        s = r
        i = l

        while i <= s: 
            if nums[i] > pivot: 
                nums[i], nums[g] = nums[g], nums[i]
                i += 1
                g += 1
            elif nums[i] < pivot: 
                nums[i], nums[s] = nums[s], nums[i]
                s -= 1
            else: 
                i += 1
            
        return [g, s]
        

    def quick_sort_variant(self, nums: list[int], l: int, r: int, k: int) -> int: 
        if l == r: 
            return nums[l]
        
        # g, s Partitioning array in 3 halves (greater, equal, smaller)
        g, s = self.partition(nums, l, r)

        if k - 1 < g: 
            # Bigger elements on left side 
            return self.quick_sort_variant(nums, l, g - 1, k)
        elif k - 1 > s: 
            # Smaller elements on right side
            return self.quick_sort_variant(nums, s + 1, r, k)   
        else: 
            return nums[g]

    def findKthLargest(self, nums: list[int], k: int) -> int:
        return self.quick_sort_variant(nums, 0, len(nums)-1, k)

    
    # TC -- O(log(N))


def solution() -> None:
    # Input 
    nums = list(map(int, input().split(",")))
    k = int(input())

    sol = Solution()
    print(sol.findKthLargest(nums, k))






if __name__ == "__main__":
    solution()