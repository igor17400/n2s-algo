# Reference:
# Introduction to Algorithms, Fourth edition
# Linda Xiao and Tom Cormen
# https://github.com/Ky-Ling/CLRS-Python-Implementation

class BTreeNode:
    def __init__(self, n, max_keys, leaf):
        """
        Initialize a node of B-tree with number of keys and a 
        boolean indicating whether it is a leaf.

        Arguments:

        n -- number of keys currently stored
        leaf -- True if the node is a leaf, False if not
        """

        self.n = n  # number of keys currently stored
        self.leaf = leaf  # boolean if node is a leaf
        self.key = [None] * max_keys  # the keys themselves
        if not leaf:
            seff.c = [None] * (max_keys + 1)  # internal nodes store pointers to children

    def disk_read(self):
        """
        Placeholder for code to read in the disk block containing this code.
        """
        pass

    def disk_write(self):
        """
        Placeholder for code to write out the disk block containing this node.
        """
        pass

    def search(self, k):
        """
        Search for a node with a given key k in the subtree rooted at this node.

        Returns:
        Tuple consisting of a node and index search that node.key[index] = k
        """
        # find the smallest index i such that k <= x.k[i] or else set i to x.n + 1
        i = 0
        while i < self.n and k > self.key[i]:
            i += 1

        # Have we discovered key k?
        if i < self.n and k == self.key[i]:
            return self, i
        # Either terminate the search unseccessfully or recursively search a subtree
        elif self.leaf:
            return None
        else:
            self.c[i].disk_read()
            return self.c[i].search(k)        	

    def find_greatest_in_subtree(self):
        """
        Find the greatest key in the subtree rooted at this node.
        """
        if self.leaf:
            return self.key[self.n - 1]  # return greatest key
        else:
            # Find the greatest key in the subtree of the greatest child.
            self.c[self.n].disk_read()
            return self.c[self.n].find_greatest_in_subtree()

    def find_smallest_in_subtree(self):
        """
        Find the smallest key in the subtree rooted at this node.
        """
        if self.leaf:
            return self.key[0]  # return smallest key
        else:
            # Find the smallest key in the subtree of the smallest child.
            self.c[self.n].disk_read()
            return self.c[0].find_smallest_in_subtree()


class BTree:
    def __init__(self, t):
        """
        Create an empty root node, based on B_Tree_Create
        """
        self.t = t 						# minimum degree of the B-tree
        self.max_keys = 2 * (t - 1) 	# maximum degree of the B-tree
        self.root = BTreeNode(0, self.max_keys, True)
        self.root.disk_write()
