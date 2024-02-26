"""
Time Space Complexity 

In the naive case, the find function will result in O(n) because it's
possible that the tree is just a chain like a linked list and we have
to traverse every single node. With path compression, since we are 
updating the parent to be the grandparent each time, we can reduce
the complexity down to O(log n).

If we combine it with the union function, we get a time complexity called
inverse Ackermann, alpha(n), which can be simplified to constant time O(1).
So, if m is the number of edges we have, then the time complexity of
Union-Find is O(m * log n)
"""


class UnionFind:
    def __init__(self, n):
        self.par = [0] * n
        self.rank = [0] * n
        self.time = [0] * n

        for i in range(0, n):
            self.par[i] = i
            self.rank[i] = 0

    # Find parent of n, with path compression.
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            # Path compression: Update parent pointer to root
            self.par[p] = self.par[self.par[p]] 
            p = self.par[p]
        return p

    # Find parent of n recursively, with path compression.
    def find_rec(self, n):
        p = self.par[n]
        if n != p:
            p = self.find_rec(p)

        return p

    # Union by height / rank.
    # Return false if already connected, true otherwise.
    def union(self, t, n1, n2):
        """
        t: time when the two objects were unioned
        """
        # p1, p2 = self.find(n1), self.find(n2)
        p1, p2 = self.find_rec(n1), self.find_rec(n2)

        if p1 == p2:
            print("Not possible to union: {} and {}".format(n1, n2))
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1

        self.time[n2] = t  # save the time when the union happened

        print("--- parents array ---")
        print(self.par)
        print("--- time array ---")
        print(self.time)
        print("---------------------")
        return True

    def find_time(self, n1, n2):
        par_a = self.find(n1)  # O (log n)
        par_b = self.find(n2)

        # Check if the two elements are currently in the same connected component
        if par_a == par_b:
            return max(self.time[par_a], self.time[par_b])
        else:
            return None


uf = UnionFind(6)

uf.union(1, 0, 3)
uf.union(2, 4, 2)
uf.union(3, 1, 5)
uf.union(4, 0, 1)
uf.union(5, 2, 1)

print(uf.find_time(1, 5))
