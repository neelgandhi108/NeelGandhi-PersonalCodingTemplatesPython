class BinaryTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.root = data

    def insert_left(self, value):
        if self.left is None:
            self.left = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, value):
        if self.right is None:
            self.right = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right = self.right
            self.right = new_node

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def set_root_value(self, value):
        self.root = value

    def get_root_value(self):
        return self.root