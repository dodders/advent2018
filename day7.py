from anytree import Node, RenderTree


j = Node('j')
g = Node('g', parent=j)
print(j)
