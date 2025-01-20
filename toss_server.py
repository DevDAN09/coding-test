import ast

input_str = "[[1,2],[2,3],[2,4],[2,5],[5,6],[5,7],[6,8],[2,9]]"
list_of_pairs = ast.literal_eval(input_str)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = [] 
    
    def add_child(self, child_node):
        self.children.append(child_node)

class NaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)
    
    def add(self, parent_value, child_value):
        parent_node = self._find(self.root, parent_value)
        if parent_node:
            parent_node.add_child(TreeNode(child_value))

    def _find(self, node, value):
        if node.value == value:
            return node
        for child in node.children:
            found_node = self._find(child, value)
            if found_node:
                return found_node
        return None
    
    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print('  ' * level + str(node.value))
        for child in node.children:
            self.print_tree(child, level + 1)

tree = NaryTree(list_of_pairs[0][0]) 
tree.add(list_of_pairs[0][0], list_of_pairs[0][1])

for pair in list_of_pairs[1:]:
    tree.add(pair[0], pair[1])

print("트리 구조:")
tree.print_tree()

print("\n각 노드와 자식들:")
def print_node_children(node):
    print(f"Node {node.value}: children = {[child.value for child in node.children]}")
    for child in node.children:
        print_node_children(child)

print_node_children(tree.root)