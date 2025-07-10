from collections import deque

class Treenode():
    def __init__(self,data):
        self.data=data
        self.children=[]


root = Treenode(1)
child1 = Treenode(2)
child2 = Treenode(3)
child3 = Treenode(4)



root.children.extend([child1,child2,child3])

child2.children.extend([Treenode(7),Treenode(8)])


def print_tree(root):
    if root is None:
        return
    print("Tree val is ",root.data)
    for child in root.children:
        print_tree(child)

    
print_tree(root)

def take_Input_level():
    data = int(input("Enter the root data:"))
    root = Treenode(data)

    queue = deque([root])

    while len(queue) != 0 :
        current_node = queue.popleft()
        num_children = int(input("erter the nunber of chlIdren for " + str(current_node.data)))

        for i in range(num_children):
            child_data = int(input(f"enter the data for {i+1} of node {current_node.data}:"))
            child_node = Treenode(child_data)
            current_node.children.append(child_node)
            queue.append(child_node)
    return root
take_Input_level()