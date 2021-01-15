from collections import deque


class Heap:
    def __init__(self):
        self.storage = []
        self.value = None
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, value):
        if self.value is None:
            self.value = value
            self.root = True
        new_parent = self.get_next_parent()
        if not new_parent.left:
            new_parent.left = Heap()
            new_parent.left.value = value
            new_parent.left.parent = new_parent
            new_parent.left._bubble_up()
        elif not new_parent.right:
            new_parent.right = Heap()
            new_parent.right.value = value
            new_parent.right.parent = new_parent
            new_parent.right._bubble_up()

    def delete(self):
        last_element = self.get_last_element()
        self.value = last_element.value # substitute value
        # nuke the node
        if last_element.parent.left == last_element:
            last_element.parent.left = None 
        if last_element.parent.right == last_element:
            last_element.parent.right = None
        self._sift_down()

    def get_max(self):
        # Should work as it's on top. This is more of a peek (vs pop)
        return self.value

    def get_size(self):
        size = 0
        if not self:
            return size
        queue = deque()
        queue.appendleft(self)
        # size += 1 # Not sure why this is wrong
        while(queue):
            p = queue.pop()
            if p.left:
                queue.appendleft(p.left)
                size += 1
            if p.right:
                size += 1
                queue.appendleft(p.right)
        return size

    def _bubble_up(self):  # index param removed as using actual binary tree not array
        cur_self = self
        cur_parent = self.parent
        while (cur_parent is not None and cur_self.value > cur_parent.value):
            tmp = cur_self.value
            cur_self.value = cur_parent.value
            cur_parent.value = tmp
            cur_self = cur_parent
            cur_parent = cur_parent.parent

    def _sift_down(self):
        if not self.left and not self.right:
            return True
        if self.left and not self.right and (self.value >= self.left.value):
            return True
        if (self.value >= self.left.value and self.value >= self.right.value):
            return True
        if self.value < self.left.value:
            temp = self.value
            self.value = self.left.value
            self.left.value = temp
            self.left._sift_down()
        elif self.value < self.right.value:
            temp = self.value
            self.value = self.right.value
            self.right.value = temp
            self.right._sift_down()
        self._sift_down()
            
    def get_next_parent(self):
        if not self:
            return False
        queue = deque()
        queue.appendleft(self)
        while True:
            p = queue.pop()
            if (p.left):
                queue.appendleft(p.left)
            else:
                return p
            if (p.right):
                queue.appendleft(p.right)
            else:
                return p

    def get_last_element(self):
        if not self:
            return False
        queue = deque()
        queue.appendleft(self)
        while queue:
            p = queue.pop()
            if (p.left):
                queue.appendleft(p.left)
            if (p.right):
                queue.appendleft(p.right)
            if len(queue) == 1 and queue[0].left is None and queue[0].right is None:
                return queue.pop() # last element. 