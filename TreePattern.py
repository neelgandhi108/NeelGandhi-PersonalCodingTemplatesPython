#Tree Tricks


Bottom up solution with arguments for min, max

def maxAncestorDiff(self, root: TreeNode) -> int:
    if not root:
        return 0
    self.ans = 0
    def dfs(node, minval, maxval):
        if not node:
            self.ans = max(self.ans, abs(maxval - minval))
            return
        dfs(node.left, min(node.val, minval), max(node.val, maxval))
        dfs(node.right, min(node.val, minval), max(node.val, maxval))
    dfs(root, float('inf'), float('-inf'))
    return self.ans
Building a path through a tree

def binaryTreePaths(self, root: TreeNode) -> List[str]:
    rtn = []
    if root is None: return []
    stk = [(root, str(root.val))]
    while stk:
        node, path = stk.pop()
        if node.left is None and node.right is None:
            rtn.append(path)
        if node.left:
            stk.append((node.left, path + "->" + str(node.left.val)))
        if node.right:
            stk.append((node.right, path + "->" + str(node.right.val)))
    return rtn
Using return value to sum

def diameterOfBinaryTree(self, root: TreeNode) -> int:
    self.mx = 0
    def dfs(node):
        if node:
            l = dfs(node.left)
            r = dfs(node.right)
            total = l + r
            self.mx = max(self.mx, total)
            return max(l, r) + 1
        else:
            return 0
    dfs(root)
    return self.mx
Change Tree to Graph

def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
    adj = collections.defaultdict(list)

    def dfsa(node):
        if node.left:
            adj[node].append(node.left)
            adj[node.left].append(node)
            dfsa(node.left)
        if node.right:
            adj[node].append(node.right)
            adj[node.right].append(node)
            dfsa(node.right)

    dfsa(root)

    def dfs(node, prev, d):
        if node:
            if d == K:
                rtn.append(node.val)
            else:
                for nei in adj[node]:
                    if nei != prev:
                        dfs(nei, node, d+1)

    rtn = []
    dfs(target, None, 0)
    return rtn