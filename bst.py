class Node:
    def __init__(self, index, val, left=None, right=None):
        self.index = index
        self.val = val
        self.left = left
        self.right = right
        self.parent = None


class Tree:
    def __init__(self, root):
        self.root = root

    def insert(self, root, new_node):
        '''
        Take a node and check if we can insert to the left or right
        based on the nodes val, recursive if not
        '''
        if new_node.index > root.index:
            # go right
            if root.right:
                # if it exists we go a layer deeper
                self.insert(root.right, new_node)
            else:
                new_node.parent = root
                root.right = new_node
                print("success, entered {} right of ".format(new_node.index), root.index)
        else:
            # go left
            if root.left:
                # again recursive if we have a node
                self.insert(root.left, new_node)
            else:
                # end of, time to insert
                new_node.parent = root
                root.left = new_node
                print("success, entered node left of root")

    def in_order_successor(self, n):
        current = n 
        # loop down to find the leftmost leaf 
        while(current.left is not None): 
            current = current.left  
        return current  


    def print_tree_lr(self, root):
        if root:
            self.print_tree_lr(root.left)
            print("v-{} (l{})".format(root.index, root.val))
            self.print_tree_lr(root.right)

    def search_via_n(self, node, index):
        '''
        Find some node with given index
        '''
        print("comparing node i with i ", node.index, index)
        if node.index == index:
            return node

        if node.index > index:
            # go left
            if node.left:
                return self.search_via_n(node.left, index)
            else:
                return "not found"
        else:
            # go right
            if node.right:
                return self.search_via_n(node.right, index)
            else:
                return "not found"

    
    def dfs(self, node, v):
        # search tree for some val v
        if node:
            if node.index == v:
                print("found node")
                return node
            n = self.dfs(node.left, v)
            if n:
                node = n
            if node.index == v:
                print("My node %s" % node)
                return node
            n = self.dfs(node.right, v)
            return n
 

if __name__ == "__main__":
    ml = [ 89214, 26671, 75144, 32445, 13656, 66289, 21951, 10265, 59857, 59133, 63227, 86121, 37411, 54628, 25859, 43510, 63756, 54763, 30852, 53243, 76238, 96885, 33074, 17745, 81814, 43436, 79172, 92819, 30001, 68442, 54021, 35566, 95113, 29164, 84362, 25120, 11804, 6313, 51736, 71661, 81797, 14962, 57781, 35560, 85941, 99991, 95421, 66048, 54754, 26272, 35642, 47343, 39508, 85068, 65087, 21321, 28503, 60611, 30491, 58503, 29052, 84512, 94069, 40516, 13675, 78430, 65635, 25479, 1094, 17370, 13491, 99243, 48683, 71271, 34802, 34624, 87613, 46574, 671, 42366, 89197, 36313, 89708, 28704, 21380, 54795, 66376, 49882, 15405, 96867, 24737, 60808, 81378, 35157, 1324, 11404, 29938, 66958, 53234, 47384]
    qs = [80]
    root = int(len(ml)/2)
    rnode = Node(root, ml[root])
    import random
    t = Tree(rnode)
    #new_nodes = [Node(random.randint(0,200)) for _ in range(0, 29)]
    [t.insert(t.root, Node(i, x)) for i, x in enumerate(ml[:root])]
    [t.insert(t.root, Node(i, x)) for i, x in enumerate(ml[root:])]

    t.print_tree_lr(t.root)
    foo = t.search_via_n(t.root, 80)
    import pdb; pdb.set_trace()

    t.print_tree_lr(t.root)

