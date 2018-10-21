class BinaryIndexedTree:
    """
    A toy Binary Indexed Tree data structure that caches element sums 
    (only numbers are considerred),
    for efficiently qurying/modifying subarray sums
    O(log(n)) modify and O(log(n)) query
    """
    def __init__(self, A):
        """
        :type A: list
        """
        self.C = [0] * (1+len(A))
        self.A = A
        for idx, a in enumerate(A):
            self.add(idx, a)
        
    def update(self, idx, val):
        """
        Update the value of the idx element in A
        Also results in updating cashed element sums
        :type idx: int
        :type val: number
        """
        diff = val - self.A[idx]
        self.A[idx] = val
        self.add(idx, diff)
        
    def sum_range(self, start_idx, end_idx):
        """
        query the sum of a subarray range
        :type start_idx: int
        :type end_idx:   int
        """
        return self.sum(end_idx) - self.sum(start_idx-1)
        
    def add(self, idx, val):
        """
        add numbers to the tree array
        :type idx: int
        :type val: number
        """
        i = idx + 1
        while i < len(self.C):
            self.C[i] += val
            i += self._lowbit(i)
        
    def sum(self, idx):
        """
        query the sum from start to idx
        :type idx: int
        """
        i = idx + 1
        res = 0
        while i > 0:
            res += self.C[i]
            i -= self._lowbit(i)
        return res
    
    def _lowbit(self, idx):
        """
        Convert idx to binary representation,
        return the last 1 represented number in 
        decimal representation e.g. (34)10 = (00100010)2
        the segment containing the last 1 is (10)2 = (2)10
        :type idx: int
        """
        return idx & -idx
        
        
if __name__ == "__main__":
    A = [1,2,34,9,4,-2,9.8,2, 89, 3.7]
    tree_arr = BinaryIndexedTree(A)
    assert(tree_arr.sum_range(3, 9) == sum(A[3:9+1]))
    tree_arr.update(5, 100)
    A[5] = 100
    assert(tree_arr.sum_range(3, 9) == sum(A[3:9+1]))
    print("\t",A)
    print(tree_arr.C)
    
    
