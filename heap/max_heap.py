class Heap:
    def __init__(self, comparator):
        self.storage = []
        self.comparator = comparator

        self.size = 0

    def insert(self, value):
        pass

    def delete(self):
        pass

    def get_priority(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass

    # HELPER METHODS
    def _get_parent_index(self, index):
        return (index-1) // 2
    def _get_leftchild_index(self, index):
        return 2*index + 1
    def _get_rightchild_index(self, index):
        return 2*index + 2
    def _has_parent(self, index):
        return self.getParentIndex >= 0
    def _has_leftchild(self, index):
        return self._get_leftchild_index < self.size
    def _has_rightchild(self, index):
        return self._get_rightchild_index < self.size
    def _swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]      
        self.storage[index2] = temp      
        
