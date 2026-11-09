from pathlib import Path
import sys

current_folder = Path(__file__).resolve().parent
sys.stdout = open(current_folder / 'output.txt', 'w')
sys.stdin = open(current_folder / 'input.txt', 'r')

def selection_sort(nums: list[int]) -> None: 
    n = len(nums)

    for i in range(0, n): 
        # Find Smallest element in nums[i:]
        min_i = i
        for j in range(i + 1, n): 
            if nums[j] < nums[min_i]: 
                min_i = j

        # Swap the Smalleste element with nums[min_i]
        nums[min_i], nums[i] = nums[i], nums[min_i]


def solution() -> None:
    nums = list(map(int, input().split()))

    selection_sort(nums)
    print("Sorted Array: ", nums)






if __name__ == "__main__":
    solution()