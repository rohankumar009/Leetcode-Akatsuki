class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
         # If the root is None
        if root is None:
            return TreeNode(val)
        
        # If the value is less than the current node val
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        # If the value is greater than the current nod val
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
