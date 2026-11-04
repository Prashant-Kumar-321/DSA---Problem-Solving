from pathlib import Path
import sys

current_folder = Path(__file__).resolve().parent
sys.stdout = open(current_folder / 'output.txt', 'w')
sys.stdin = open(current_folder / 'input.txt', 'r')

import random

class Solution:
    def partition(self, nums: list[int], l: int, r: int): 

        # Pick a random index between l and r
        ran = random.randint(l, r) 
        nums[ran], nums[r] = nums[r], nums[ran]


        i = l
        for j in range(l, r): 
            if nums[j] >= nums[r]: 
                nums[j], nums[i] = nums[i], nums[j]
                i += 1

        # Place pivot element at its correct position
        nums[i], nums[r] = nums[r], nums[i]
        return i            



    def quick_sort_variant(self, nums: list[int], l: int, r: int, k: int) -> int: 
        if l == r: 
            return nums[l]
        
        pivot = self.partition(nums, l, r)

        if pivot == k - 1: 
            return nums[pivot]
        elif k - 1 < pivot: 
            # Bigger elements on left side 
            return self.quick_sort_variant(nums, l, pivot - 1, k)
        else: 
            # Smaller elements on right side
            return self.quick_sort_variant(nums, pivot + 1, r, k)


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