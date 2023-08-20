class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        stack = []
        prev_val = float("-inf")  

        while stack or root:
            while root:

                stack.append(root)
                root = root.left
            
            root = stack.pop()
            if root.val <= prev_val:
                return False
            
            prev_val = root.val

            root = root.right
        
        return True
