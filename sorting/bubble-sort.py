from pathlib import Path
import sys

current_folder = Path(__file__).resolve().parent
sys.stdout = open(current_folder / 'output.txt', 'w')
sys.stdin = open(current_folder / 'input.txt', 'r')


def bubble_sort(nums: list[int]): 
    n = len(nums)
    for i in range(0, n - 1): 
        for j in range(0, n - 1 - i): 
            if nums[j] > nums[j + 1]: 
                # Swap both Consecutive Elements
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def solution() -> None:
    nums = list(map(int, input().split(' ')))
    bubble_sort(nums)

    # Print the sorted array
    print("Sorted Array:", nums)

    print()






if __name__ == "__main__":
    solution()