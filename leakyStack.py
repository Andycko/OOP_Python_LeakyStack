#  Author: CS1527 Course Team
#  Date: 9 January 2020
#  Assessment 1:  10% of your overall mark for the course
#

# from array_stack import ArrayStack
import unittest

class Full(Exception):
    pass
    


class Empty(Exception):
    pass

class MyLeakyStack():
    """complete this class by adding more functions within the class"""
    def __init__(self, maxlen, capacity):
        """note: this function is partially completed"""
        self._maxlen = maxlen
        self._capacity = capacity   # size of the circular array
        self._storage = [None] * capacity  # initialise storage room, this is treated as a circular array
        self._stackItems = 0
        self._top = 0
        self._end = 0

    def push(self, item):
        if self._stackItems == self._maxlen:
            # Full exception
            if self._top == 0:
                self._top = 1
            #if self._top == 2:
            #    self._end = 0
            self._storage.remove(self._storage[self._end])
            self._storage.insert(self._top,item)
            self._top = ((self._top + 1) % self._capacity) 
            self._end = ((self._end + 1) % self._capacity)
            if self._top != 2: 
                self._storage = self._storage[-1:] + self._storage[:-1]
#            print(str(self._storage), self._end, self._top)

        else:
            self._top = self._top % self._capacity
            if self._storage[self._top] == None:
                self._storage.insert(self._top, item)
                self._top = 1
            else:
                self._top += 1
                self._storage.insert(self._top, item)

            if self._top == self._capacity - 1:
                self._storage.pop((self._top + 1))
            else:
                self._storage.pop((self._top + 1) % self._capacity)

            self._stackItems += 1
#            print(str(self._storage))

    def pop(self):
        if self._stackItems == 1 and self._top == 1:
            poppedItem = self._storage.pop(0)
        else:
            poppedItem = self._storage.pop(self._top % self._capacity)
        self._storage.insert(self._top % self._capacity, None)
        self._top -= 1
        self._stackItems -= 1
        return poppedItem
#        print(str(self._storage))

    def __str__(self):
        return str(self._storage)

""" if __name__ == "__main__":
    S = MyLeakyStack(3, 5)

    for x in range(1,9):
        S.push(x)

 """

if __name__ == '__main__':

    S = MyLeakyStack(5, 10)   # stack size should be 5 and the capacity of the array should be 10

    for i in range(12):
        try:
            S.push(i)
            print("after push "+str(i), S._storage)
        except Exception as e:
            print(e)

    for i in range(6):
        try:
            a=S.pop()
            print("after pop "+str(a), S._storage)
        except Exception as e:
            print(e, S._storage)

    for i in range(5):
        try:
            S.push(i+100)
            print("after push " + str(i+100), S._storage)
        except Exception as e:
            print(e, S._storage)
