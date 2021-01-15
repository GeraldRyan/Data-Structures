class Heap:
    def __init__(self):
        self.storage = []
        # self.comparator = comparator

        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        self.size += 1
        self._bubble_up(self.size - 1)

    def delete(self):
        if self.size == 0:
            raise("Empty Heap")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size-1]
        self.size -= 1
        self._sift_down(0)
        return data

    # def get_priority(self):
    #     pass

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        parent_index = self._get_parent_index(index)
        if parent_index < 0:
            return
        while (parent_index >= 0 and self.storage[index] > self.storage[parent_index]):
            self._swap(parent_index, index)
            index = parent_index
            parent_index = self._get_parent_index(index)

    def _sift_down(self, index):
        while self._has_leftchild(index):
            bigger_child_index = self._get_leftchild_index(index)
            if(self._has_rightchild(index) and self._get_rightchild_value(index) > self._get_leftchild_value(index)):
                bigger_child_index = self._get_rightchild_index(index)
            if (self.storage[index] > self.storage[bigger_child_index] ): # place to switch with comparator 
                break
            else:
                self._swap(index, bigger_child_index)
            index = bigger_child_index


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
        return (self._get_leftchild_index(index) < self.size)

    def _has_rightchild(self, index):
        return self._get_rightchild_index(index) < self.size

    def _swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    def _get_leftchild_value(self, index):
        return self.storage[self._get_leftchild_index(index)]
    def _get_rightchild_value(self, index):
        return self.storage[self._get_rightchild_index(index)]