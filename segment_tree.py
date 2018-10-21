class SegmentTreeNode:
    """
    Tree Node (for interval max)
    """
    def __init__(self, start, end, max):
        self.start = start
        self.end = end
        self.max = max
        self.left = self.right = None
        

class SegmentTree:
    """
    Segment Tree datastructure,
    Alternative to Binary Indexed Tree supporting
    interval sums, and offers more operations in interval (max operation here).
    O(log(N)) query and O(log(N)) modify time complexity
    """
    def __init__(self, A):
        self.root = self.build(A, 0, len(A)-1)
    
    def build(self, A, start, end):
        if start > end:
            return None
        root = SegmentTreeNode(start, end, A[start])
        if start == end:
            return root
        root.left = self.build(A, start, (start + end) // 2)
        root.right = self.build(A, (start + end) // 2 + 1, end)
        root.max = max(root.left.max, root.right.max)
        return root

    def modify(self, index, value):
        return self._modify(self.root, index, value)
    
    def _modify(self, root, index, value):
        if root.start == root.end and root.start == index: # find the leaf to be modified
            root.max = value # modify the leaf node value
            return
        mid = (root.start + root.end) // 2 # split the interval into two halves
        if index <= mid: # if the target index is in the left interval
            self._modify(root.left, index, value) # recurse operation
            root.max = max(root.right.max, root.left.max) # ensure the modification is synchronized backward
        else:           # if the target index is in the right interval
            self._modify(root.right, index, value) # recurse operation
            root.max = max(root.left.max, root.right.max)# ensure the modification is synchronized backward
        return

    def query(self, start, end):
        return self._query(self.root, start, end)
    
    def _query(self, root, start, end):
        if start <= root.start and root.end <= end:
            # it the result is in the current interval, return the result
            return root.max
        mid = (root.start + root.end) // 2 # split the interval
        ans = float('-inf') # initialize the answer
        if mid >= start:  # if the queried interval intercects with the left interval, query left interval
            ans = max(ans, self._query(root.left, start, end))
        if mid + 1 <= end: # if the queried interval intercects with the right interval, query right interval
            ans = max(ans, self._query(root.right, start, end))
        return ans # return the result
        
if __name__ == "__main__":
    A = [1,3,4,-4,2,9,10,140,22,18]
    segment_tree = SegmentTree(A)
    assert(max(A) == segment_tree.query(0, len(A)-1))
    assert(max(A[1:5]) == segment_tree.query(1, 4))
    segment_tree.modify(4, 999)
    A[4] = 999
    assert(max(A[1:5]) == segment_tree.query(1, 4))
    
