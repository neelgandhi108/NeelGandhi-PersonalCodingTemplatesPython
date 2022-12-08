# Tree Traversal 

#Python - DFS

def preorder(root: TreeNode) -> None:
    if not root: return
    print(root.val)
    preorder(root.left)
    preorder(root.right)
	
	
def inorder(root: TreeNode) -> None:
    if not root: return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
	
	
def postorder(root: TreeNode) -> None:
    if not root: return
    postorder(root.left)
    postorder(root.right)
    print(root.val)
	
#Python - BFS

def levelorder(root: TreeNode) -> None:
    if not root: return
    q = deque([root])
    
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            print(str(node.val), end = " ")
            if node.left: 
                q.append(node.left)
            if node.right: 
                q.append(node.right)

        print()