#  Author of the initial template: CS1527 Course Team
#  Further changes to complete assessment mady by: Andrej Szalma
#  Date: 9 January 2020
#  Assessment 1:  10% of your overall mark for the course
#

from array_stack import ArrayStack
import unittest


class Full(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   # this is basically not neccessary, but I think its a good practice to call the parents __init__
        self._message = args[0] # When calling the exception, I want to send a message as well, this could be done only by writing a message in this class, but it is more flexible
        self._item = args[1]    # Passing the leaked item from our push function

    def __str__(self):
        return self._message + " " + str(self._item)    # after printing the exception, this will be the format
    
    
class Empty(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   # this is basically not neccessary, but I think its a good practice to call the parents __init__
        self._message = args[0] # When calling the exception, I want to send a message as well, this could be done only by writing a message in this class, but it is more flexible

    def __str__(self):
        return self._message    # after printing the exception, this will be the format

class MyLeakyStack(ArrayStack):
    """complete this class by adding more functions within the class"""
    def __init__(self, maxlen, capacity):
        """note: this function is partially completed"""
        self._maxlen = maxlen   # max length of the stack
        self._capacity = capacity   # size of the circular array
        self._storage = [None] * capacity  # initialise storage room, this is treated as a circular array
        self._stackItems = 0
        self._top = 0   # will be always the index of next possible position in the stack, so top item + 1
        self._end = 0   # will be always the index of the bottom item in our stack
        self._removedItem = None

    def push(self, item):
        if self._stackItems == self._maxlen:    # check if the stack has reached its max length, or for some unknown reason more than its max length
            self._removedItem = self._storage[self._end % self._capacity]   # as I need to return this item in the exception, I do need to save it somewhere first
            self._storage[self._end % self._capacity] = None    # replace the end == bottom of the stack with "None"
            self._storage[self._top % self._capacity] = item    # replace the element after the top of the stack with our input item
            self._end += 1
            self._top += 1
            raise Full("reach stack limit, forget element",self._removedItem)  # raise this exception only after we finish pushing, as everything after it is ignored
        else:   # if the stack is not full we need slightly different approach
            self._storage[self._top % self._capacity] = item    # replace the element after the top of the stack with our input item
            self._top += 1
            self._stackItems += 1   # of course here we need to increment our counter, as our stack is not full just yet

    def pop(self):
        if self._stackItems == 0:   # checking if stack is empty, if so raise Empty exception and ignore the rest
            raise Empty("Stack is empty")
        self._removedItem = self._storage[(self._top - 1) % self._capacity]  # as I am not using the pop function, I need to save the popped element before actually removing it
        self._storage[(self._top - 1) % self._capacity] = None  # replace the top element by "None"
        self._top -= 1
        self._stackItems -= 1
        return self._removedItem

    # Just overwriting functions from parent ArrayStack class, as my Stack works a bit differently 
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._storage[(self._top - 1) % self._capacity]    

    def is_empty(self):
        return len(self._stackItems) == 0   

    def __len__(self):
        return str(self._stackItems)

    def __str__(self):
        return str(self._storage)   # custom print


if __name__ == '__main__':

    S = MyLeakyStack(5, 10)   # stack size should be 5 and the capacity of the array should be 10

    for i in range(12):
        try:
            S.push(i)
            print("after push "+str(i), S._storage)
        except Exception as e:
            print(e)
            print("after push "+str(i), S._storage)

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
