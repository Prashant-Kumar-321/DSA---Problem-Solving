from pathlib import Path
import sys

current_folder = Path(__file__).resolve().parent
sys.stdout = open(current_folder / 'output.txt', 'w')
sys.stdin = open(current_folder / 'input.txt', 'r')


def linear_search(nums: list[int], target: int) -> bool: 
    for num in nums: 
        if num == target: 
            return True 

    return False


def solution() -> None:
    nums = list(map(int, input().split(' ')))
    target = int(input())

    if linear_search(nums, target): 
        print(f'Element {target} is found in array')
    else: 
        print(f'Element {target} Not found in array')


if __name__ == "__main__":
    solution()