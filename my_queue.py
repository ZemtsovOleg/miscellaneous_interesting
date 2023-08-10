'''
my_queue.py - Implementation of a Queue data structure.

This module defines the Queue and Queue_object classes for implementing a queue using Queue_objects.

Classes:
    Queue_object: Represents an element in the queue.
    Queue: Implementation of a queue using Queue_objects.
'''

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class QueueObject:
    '''
    Class representing an element in the queue.

    :param value: The value of the element.
    :param left: Reference to the previous element.
    :param right: Reference to the next element.
    '''
    value: Any
    left: 'QueueObject'
    right: 'QueueObject'

    def __repr__(self) -> str:
        '''
        Return a string representation of the Queue_object.

        :return: String representation of the value.
        '''
        return str(self.value)


@dataclass(slots=True)
class Queue:
    '''
    Implementation of a queue using Queue_objects.

    :param first: The first element of the queue.
    :param last: The last element of the queue.
    :param limit: Maximum limit of elements in the queue. Setting a limit changes insertion time complexity from O(1) to O(n).
    '''
    first: QueueObject = None
    last: QueueObject = None
    limit: int = None

    def append(self, value) -> None:
        '''
        Append an element to the queue.

        :param value: The value to append.
        '''
        if self.limit is None or self.limit > len(self):
            if self.first is None:
                self.first = QueueObject(value, None, None)
            elif self.last is None:
                self.last = QueueObject(value, None, self.first)
                self.first.left = self.last
            else:
                temp = self.last
                self.last = QueueObject(value, None, self.last)
                temp.left = self.last

    def pop(self) -> None:
        '''Remove the first element from the queue.'''
        if self.first is not None:
            self.first = self.first.left
            if self.first is not None:
                self.first.right = None

    def add_limit(self, limit: int) -> None:
        '''
        Set the maximum limit of elements in the queue. Setting a limit changes insertion time complexity from O(1) to O(n).

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

    deque_orders = Queue(limit=7)
    for i in range(10):
        deque_orders.append(i)

    elem = deque_orders.last
    for i in range(4):
        print(elem.value)
        elem = elem.right

    deque_orders.pop()
    deque_orders.pop()
    deque_orders.pop()

    print('first:', deque_orders.first.value)
    print('last:', deque_orders.last.value)

    print(len(deque_orders))

    print(deque_orders)
