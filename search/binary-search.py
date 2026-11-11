from pathlib import Path
import sys

current_folder = Path(__file__).resolve().parent
sys.stdout = open(current_folder / 'output.txt', 'w')
sys.stdin = open(current_folder / 'input.txt', 'r')

def binary_search(nums: list[int], target: int) -> bool: 
    l = 0 
    r = len(nums) - 1

    while r >= l: 
        mid = l + (r - l) // 2 

        if nums[mid] == target: 
            return True 

        if target < nums[mid]: 
            r = mid - 1
        else: 
            l = mid + 1

    return False
    

def solution() -> None:
    nums = list(map(int, input().split()))

    target = int(input())

    if binary_search(nums, target): 
        print(f'Element Found')
    else: 
        print(f'Element not Found')






if __name__ == "__main__":
    solution()