class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root
    
    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _inorder_traversal(self, root, result):

        if root:
            print(root.key)
            self._inorder_traversal(root.left, result)
            result.append(root.key)
            self._inorder_traversal(root.right, result)
            
    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result
    def preorder_traversal(self):
        result = []
        self._preorder_traversal(self.root, result)
        return result

    def _preorder_traversal(self, root, result):
        if root:
            result.append(root.key)                # Visit current node
            self._preorder_traversal(root.left, result)  # Traverse left subtree
            self._preorder_traversal(root.right, result) # Traverse right subtree

    def postorder_traversal(self):
        result = []
        self._postorder_traversal(self.root, result)
        return result

    def _postorder_traversal(self, root, result):
        if root:
            self._postorder_traversal(root.left, result)  # Traverse left subtree
            self._postorder_traversal(root.right, result) # Traverse right subtree
            result.append(root.key)                # Visit current node
    def _height(self, root):
        if root is None:
            return 0
        return max(self._height(root.left), self._height(root.right)) + 1

    def _is_balanced(self, root):
        if root is None:
            return True
        left_height = self._height(root.left)
        right_height = self._height(root.right)
        return abs(left_height - right_height) <= 1 and self._is_balanced(root.left) and self._is_balanced(root.right)

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        return y

    def rebalance(self):
        while not self._is_balanced(self.root):
            self.root = self._rebalance(self.root)

    def _rebalance(self, root):
        # Calculate balance factor
        left_height = self._height(root.left)
        right_height = self._height(root.right)
        balance_factor = left_height - right_height

        # Left heavy
        if balance_factor > 1:
            # Left-right case
            if self._height(root.left.right) > self._height(root.left.left):
                root.left = self._rotate_left(root.left)
            # Left-left case
            root = self._rotate_right(root)

        # Right heavy
        elif balance_factor < -1:
            # Right-left case
            if self._height(root.right.left) > self._height(root.right.right):
                root.right = self._rotate_right(root.right)
            # Right-right case
            root = self._rotate_left(root)

        return root

# balancing function 

# Example usage:
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(4)

print("Inorder traversal:", bst.inorder_traversal())
print("Search for 3:", bst.search(3))
print("Search for 6:", bst.search(6))

    

# Example usage:
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

bst.rebalance()

