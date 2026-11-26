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

# Recursive Solution:
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

# Iterative Solution
class Solution:

    # BFS Algorithm
    def isSymmetric(self, root: TreeNode | None) -> bool:

        # Check Tree is not empty 
        if not root:
            return True

        # Check if either child missing
        elif (root.left and not root.right) or (not root.left and root.right): 
            return False
        
        # No Child 
        elif not root.left and not root .right: 
            return True 

        # Level Set Data Structue 
        # Add Root of left subtree 
        # Add Root of right subtree
        lsl = [root.left]   # Level Set left 
        lsr = [root.right]  # Level Set right
        nlsl = []
        nlsr = []  

        while lsl and lsr:
            # Point to current node of both level set 
            i = 0

            for i in range(len(lsl)):
                # Get the Symmetric node from left and right sub-tree
                left = lsl[i] 
                right = lsr[i]

                # Check value are same
                if left.val != right.val: 
                    return False 


                # Two branches

                # left.left and right.right
                if (not left.left and right.right) or (left.left and not right.right): 
                    return False

                elif left.left and right.right: 
                    nlsl.append(left.left)
                    nlsr.append(right.right) 

                # left.right and right.left
                if (not left.right and right.left) or (left.right and not right.left): 
                    return False 

                elif left.right and right.left: 
                    nlsl.append(left.right)
                    nlsr.append(right.left) 


            # Transfer next level set array to current level set and intializing the next level set
            lsl = nlsl 
            lsr = nlsr
            nlsl = list()
            nlsr = list()


        return True 



def solution() -> None:
    ...



if __name__ == "__main__":
    solution()