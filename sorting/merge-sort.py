from pathlib import Path
import sys

current_folder = Path(__file__).resolve().parent
sys.stdout = open(current_folder / 'output.txt', 'w')
sys.stdin = open(current_folder / 'input.txt', 'r')

def merge(nums: list[int], l: int, mid: int, r: int) -> None: 
    i = l 
    j = mid + 1 
    tmp = list()

    # Merge Left Array and Right Array
    while i <= mid and j <= r: 
        if nums[i] < nums[j]: 
            tmp.append(nums[i])
            i += 1
        else: 
            tmp.append(nums[j])
            j += 1

        k += 1 

    # Merge Leftover elements 
    while i <= mid: 
        tmp.append(nums[i])
        k += 1
        i += 1

    while j <= r: 
        tmp.append(nums[j])
        k += 1
        j += 1 

    # Transfer Back, from tmp to original array
    i = l 
    for k in range(0, len(tmp)): 
        nums[i] = tmp[k] 
        i += 1

def merge_sort(nums: list[int], l: int, r: int) -> None: 
    if l >= r: 
        return

    mid = l + (r - l) / 2
    merge_sort(nums, l, mid)
    merge_sort(nums, mid + 1, r)
    merge(nums, l, mid, r)


def solution() -> None:
    ...






if __name__ == "__main__":
    solution()