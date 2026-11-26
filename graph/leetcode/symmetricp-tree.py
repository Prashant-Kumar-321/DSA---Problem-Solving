from pathlib import Path
import sys

current_folder = Path(__file__).resolve().parent
sys.stdout = open(current_folder / 'output.txt', 'w')
sys.stdin = open(current_folder / 'input.txt', 'r')



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive Symmetricity check of Given Tree
    def is_symmetric_internal(self, left, right): 
        if (not left and right) or (left and not right): 
            return False 

        elif not left and not right: 
            return True 

        else : 
            # left and right both exist
            if left.val != right.val: 
                return False
            
        return self.is_symmetric_internal(left.left, right.right) and self.is_symmetric_internal(left.right, right.left)


    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root: 
            return True

        return self.is_symmetric_internal(root.left, root.right)




def solution() -> None:
    ...






if __name__ == "__main__":
    solution()