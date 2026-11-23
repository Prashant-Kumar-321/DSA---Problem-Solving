# Problem: https://leetcode.com/problems/same-tree/?envType=problem-list-v2&envId=breadth-first-search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Loop BFS solution
class Solution:

    # Non Recursive BFS
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        curr_level1 = [p]
        curr_level2 = [q] 

        # Compare Root values
        if p and q and p.val != q.val: 
            return False
        elif (not p and q) or (p and not q): 
            return False
        elif not p and not q: 
            # p and q both are None 
            return True

        while curr_level1 and curr_level2:
            next_level1 = list()
            next_level2 = list() 

            for i in range(len(curr_level1)): 
                right1 = curr_level1[i].right 
                right2 = curr_level2[i].right 

                left1 = curr_level1[i].left 
                left2 = curr_level2[i].left

                # Right Child
                if right1 and right2: 
                    if right1.val != right2.val: 
                        return False 

                    next_level1.append(right1)
                    next_level2.append(right2)

                elif (right1 and not right2) or (not right1 and right2): 
                    return False
                
                # Left Child 
                if left1 and left2:
                    if left1.val != left2.val: 
                        return False
                        
                    next_level1.append(left1)
                    next_level2.append(left2)
                    
                elif (left1 and not left2) or (not left1 and left2): 
                    return False


            if len(next_level1) != len(next_level2): 
                return False

            curr_level1 = next_level1 
            curr_level2 = next_level2 
        
            next_level1 = list()
            next_level2 = list()
            

        return True                      

# Recursive Solution
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # Compare root of current Tree / Sub-Tree
        if p and q and p.val != q.val: 
            return False
        elif (not p and q) or (p and not q): 
            return False
        elif not p and not q: 
            return True 

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)              


