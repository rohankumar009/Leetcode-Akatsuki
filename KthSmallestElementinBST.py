class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        kth_smallest = None

        current = root
        while current is not None:

            if current.left is None:
                count += 1
                if count == k:
                    kth_smallest = current.val
                current = current.right
            else:

                pre = current.left
                while pre.right is not None and pre.right != current:
                    pre = pre.right
                
                if pre.right is None:
                    pre.right = current
                    current = current.left
                else:

                    pre.right = None
                    count += 1
                    if count == k:
                        kth_smallest = current.val
                    current = current.right
        
        return kth_smallest
