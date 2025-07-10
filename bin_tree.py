class bin_tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = bin_tree(1)
root.left = bin_tree(2)
root.right = bin_tree(3)
root.left.left = bin_tree(4)
root.left.right = bin_tree(5)
root.right.left = bin_tree(6)
root.right.left.left = bin_tree(7)
root.right.left.right = bin_tree(8)
root.right.left.left.left = bin_tree(11)

def print_tree(root):
    if root is None:
        return
    left = f"L -> {root.left.data}" if root.left else "L -> None"
    right = f"R -> {root.right.data}" if root.right else "R -> None"
    print(f"{root.data}: {left}, {right}")

    print_tree(root.left)
    print_tree(root.right)

  
print_tree(root)