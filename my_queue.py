'''
my_queue.py - Implementation of a Queue data structure.

This module defines the Queue and Queue_object classes for implementing a queue using Queue_objects.

Classes:
    Queue_object: Represents an element in the queue.
    Queue: Implementation of a queue using Queue_objects.
'''


class Queue_object:
    '''Class representing an element in the queue.'''

    def __init__(self, value, left, right) -> None:
        '''
        Initialize a Queue_object.

        :param value: The value of the element.
        :param left: Reference to the previous element.
        :param right: Reference to the next element.
        '''
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        '''
        Return a string representation of the Queue_object.

        :return: String representation of the value.
        '''
        return str(self.value)


class Queue:
    '''Implementation of a queue using Queue_objects.'''

    def __init__(self, first: Queue_object = None, last: Queue_object = None, limit=None) -> None:
        '''
        Initialize a Queue.

        :param first: The first element of the queue.
        :param last: The last element of the queue.
        :param limit: Maximum limit of elements in the queue. Setting a limit changes insertion time complexity from O(1) to O(n).
        '''
        self.first = first
        self.last = last
        self.limit = limit

    def append(self, value) -> None:
        '''
        Append an element to the queue.

        :param value: The value to append.
        '''
        if self.limit is None or self.limit > len(self):
            if self.first is None:
                self.first = Queue_object(value, None, None)
            elif self.last is None:
                self.last = Queue_object(value, None, self.first)
                self.first.left = self.last
            else:
                temp = self.last
                self.last = Queue_object(value, None, self.last)
                temp.left = self.last

    def pop(self) -> None:
        '''Remove the first element from the queue.'''
        if self.first is not None:
            self.first = self.first.left
            if self.first is not None:
                self.first.right = None

    def get_first(self) -> Queue_object:
        '''
        Get the first element of the queue.

        :return: The first element of the queue.
        '''
        return self.first

    def get_last(self) -> Queue_object:
        '''
        Get the last element of the queue.

        :return: The last element of the queue.
        '''
        return self.last

    def add_limit(self, limit: int) -> None:
        '''
        Set the maximum limit of elements in the queue.

        :param limit: The maximum limit of elements.
        '''
        self.limit = limit

    def __len__(self) -> int:
        '''
        Return the number of elements in the queue.

        :return: The number of elements in the queue.
        '''
        count = 0
        if self.first is not None:
            obj = self.first
            count += 1
            while True:
                if obj.left is not None:
                    obj = obj.left
                    count += 1
                else:
                    break
        return count

    def __str__(self) -> str:
        '''
        Return a string representation of the queue.

        :return: String representation of the queue.
        '''
        queue_items = []
        if self.first is not None:
            obj = self.first
            while True:
                queue_items.append(obj)
                if obj.left is not None:
                    obj = obj.left
                else:
                    break
        return str(queue_items)


if __name__ == '__main__':

    deque_orders = Queue(limit=3)
    for i in range(3):
        deque_orders.append(i)

    # elem = deque_orders.get_last()
    # for i in range(3):
    #     print(elem.value)
    #     elem = elem.right

    deque_orders.pop()
    deque_orders.pop()
    deque_orders.pop()


    # print('first:', deque_orders.first.value)
    # print('last:', deque_orders.last.value)

    print(len(deque_orders))

    print(deque_orders)
