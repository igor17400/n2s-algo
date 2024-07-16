# Reference:
# Introduction to Algorithms, Fourth edition
# Linda Xiao and Tom Cormen
# https://github.com/Ky-Ling/CLRS-Python-Implementation

class Heap:
    def __init__(self, compare, array, get_key_func=None, dict=None):
        """Initialize a heap with an array and heap size.

        Arguments:
        compare -- comparison function: greater-than for a max-heap, less-than
        for a min-heap array -- array of heap elements.

        get_key_func -- an optional function that returns the key for the
        objects stored. If given, may be a static function in the object class.
        If omitted, then the identity function is used.

        dict -- an optional dictionary mapping objects in the max-heap to 
        indices.
        """
        self.compare = compare
        self.array = array

        # heap_size is the number of elements in the heap that are stored
        # in the array, defaults to all elements in array.
        self.heap_size = len(array)

        if get_key_func is None:
            self.get_key = lambda x: x
        else:
            self.get_key = get_key_func

        # If there is a dictionary mapping objects to indices, initialize it.
        # It should be empty to start.
        self.dict = dict
        if self.dict is not None:
            if len(self.dict) > 0:
                raise RuntimeError(
                    "Dictionary argument to constructor must be \
                    None or an empty dictionary."
                )
            for i in range(self.heap_size):
                dict[self.array[i]] = i

    def get_heap_size(self):
        """
        Return the size of this heap
        """
        return self.heap_size

    def is_full(self):
        """
        Return True if this heap is full, False if not full.
        """
        return self.heap_size >= len(self.array)

    def get_array(self):
        """
        Return the array implementation of this heap
        """
        return self.array

    def set_heap_size(self, size):
        """
        Set heap size to a given size
        """
        self.heap_size = size

    def parent(self, i):
        """
        Return the index of the parent node of i.
        """
        return (i - 1) // 2

    def left(self, i):
        """
        Return the index of the child to the left of i
        """
        return 2 * i + 1

    def right(self, i):
        """
        Return the index of the child to the right of i
        """
        return 2 * i + 2

    def swap(self, i, j):
        """
        Swap two elements in an array - O(1)
        """
        if self.dict is not None:
            self.dict[self.array[i]] = j
            self.dict[self.array[j]] = i

        self.array[i], self.array[j] = self.array[j], self.array[i]

    def heapify(self, i):  # inplace
        """
        Maintain the heap property - O(lg n) 

        Argument:
        i -- index of the element in the heap
        """
        left = self.left(i)
        right = self.right(i)

        if left < self.heap_size and self.compare(
            self.get_key(self.array[left]), self.get_key(self.array[i])
        ):
            swap_with = left
        else:
            swap_with = i

        if right < self.heap_size and self.compare(
            self.get_key(self.array[right]), self.get_key(
                self.array[swap_with])
        ):
            swap_with = right

        if swap_with != i:
            self.swap(i, swap_with)
            self.heapify(swap_with)

    def build_heap(self):
        """
        Convert list or numpy array into a heap

        Run heapify on all roots of the tree, from ((heap_size // 2) - 1) to 0
        Note how all the elements on the half ot the array will be roots/leafs.
        Running the algorithm like this give us timing effeciency.
        """
        self.heap_size = len(self.array)
        for i in range(len(self.array) // 2, -1, -1):
            self.heapify(i)

    def __str__(self):
        """
        Return the heap as an array.

        Note how the array can be larger then the heap.
        """
        return ", ".join(str(x) for x in self.array[:self.heap_size])

    def is_heap(self):
        """
        Verify that the array or list represents a heap.

        From root node to last internal node.
        Since we use our functions of left and right, we can iterate through
        half of the array.
        """
        for i in range(0, self.heap_size // 2):
            # Check the left child.
            if self.compare(
                self.get_key(self.array[self.left(i)]
                             ), self.get_key(self.array[i])
            ):
                return False
            # If there is a right child, check it.
            if self.right(i) < self.heap_size and \
                    self.compare(
                        self.get_key(self.array[self.right(i)]), self.get_key(
                            self.array[i])
            ):
                return False

        return True
