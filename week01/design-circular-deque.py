class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.maxsize = k
        self.size = 0
        self.deque = []

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isEmpty():
            self.deque.append(value)
            self.size += 1
            return True
        else:
            if self.isFull():
                return False
            else:
                self.deque = [value] + self.deque
                self.size += 1
                return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isEmpty():
            self.deque.append(value)
            self.size += 1
            return  True
        else:
            if self.isFull():
                return False
            else:
                self.deque.append(value)
                self.size += 1
                return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.deque = self.deque[1:]
            self.size = self.size - 1
            return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.deque = self.deque[:-1]
            self.size -= 1
            return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.deque[0]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.deque[-1]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        if self.size == 0:
            return True
        else:
            return False

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        if self.size == self.maxsize:
            return True
        else:
            return False