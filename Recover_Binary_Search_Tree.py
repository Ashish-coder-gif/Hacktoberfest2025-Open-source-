class Solution(object):
    def recoverTree(self, root):
      
        nodes, vals = [], []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)

        vals.sort()
        for i in range(len(nodes)):
            nodes[i].val = vals[i]
