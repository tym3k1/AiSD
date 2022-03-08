from TreeNode import *

class Tree:
    def __init__(self, root: TreeNode):
        self.root = root

    def add(self, value:Any, parent:Any):
        parent.children.append(TreeNode(value))

    def for_each_level_order(self):
        if type(self) is Tree:
            for x in self.root.children:
                print(x)
                Tree.for_each_level_order(x)
        for x in self.children:
            print(x)
            Tree.for_each_level_order(x)

    def show(self):
        s = "c==3 "

        if type(self) is Tree:
            print(self.root.value)
            for x in self.root.children:
                print(s*x.depth()+x.value)
                Tree.show(x)
        if type(self) is TreeNode:
            for x in self.children:
                print(s*x.depth()+x.value)
                Tree.show(x)










tf = TreeNode("F")
tb = TreeNode("B") #2
tg = TreeNode("G")#2
ta = TreeNode("A")#3b
td = TreeNode("D")#3b
ti = TreeNode("I")#3g
tc = TreeNode("C")#4d
te = TreeNode("E")#4d
th = TreeNode("H")#ti
tree = Tree(tf)

tf.add(tb)
tf.add(tg)
tb.add(ta)
tb.add(td)
tg.add(ti)
td.add(tc)
td.add(te)
ti.add(th)
# tree.add(69, ti)

# tree.show()
# tree.for_each_deep_first()
tree.show()