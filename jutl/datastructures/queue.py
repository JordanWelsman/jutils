# Module imports
from __future__ import annotations
from typing import Any
from jutl.exceptions import EmptyQueueError, FullQueueError
from jutl.formatting import apply

# External class visibility
__all__ = ['Queue']


class Queue(object):
    """
    Class which implements a
    first-in-first-out queue object
    with queue methods.
    """
    def __init__(self, name: str = None, capacity: int = None) -> None:
        "Initialization method."
        self.name: str = name
        self._queue : list = []
        self._capacity: int = capacity

    def __repr__(self) -> str:
        """
        Tells the interpreter how
        to represent this class.
        """
        string = f"{self.__class__.__name__}("
        if self.name is not None:
            string += f"{self.name}"
        if len(self._queue) > 0:
            string += f", " if self.name is not None else ""
            string += f"{len(self._queue)}"
        if self._capacity is not None:
            string += f"/" if len(self) > 0 else ", " if self.name is not None else ""
            string += f"{self._capacity}"
        string += ")"
        return string

    def __call__(self) -> list:
        """
        Tells the interpreter what to
        do when an object of this
        class is called directly.
        """
        return self._queue

    def __len__(self) -> int:
        """
        Tells the interpreter what to
        consider this class' length.
        """
        return len(self._queue)

    def __iter__(self) -> iter:
        """
        Tells the interpreter what to
        iterate over when iterator methods
        are called on this class.
        """
        raise NotImplementedError("Queues are not iterable.")

    def __eq__(self, other) -> bool:
        """
        Tells the interpreter how this class
        handles equal operators.
        """
        return self._queue == other._queue

    def __ne__(self, other) -> bool:
        """
        Tells the interpreter how this class
        handles not equal operators.
        """
        return self._queue != other._queue

    def __gt__(self, other) -> bool:
        """
        Tells the interpreter how this class
        handles greater than operators.
        """
        return len(self) > len(other)

    def __ge__(self, other) -> bool:
        """
        Tells the interpreter how this class
        handles greater or equal operators.
        """
        return len(self) >= len(other)

    def __lt__(self, other) -> bool:
        """
        Tells the interpreter how this class
        handles less than operators.
        """
        return len(self) < len(other)

    def __le__(self, other) -> bool:
        """
        Tells the interpreter how this class
        handles less than or equal operators.
        """
        return len(self) <= len(other)

    def __add__(self, other) -> list:
        """
        Tells the interpreter how to sum these objects.
        """
        return self.extend(other=other)


    def enqueue(self, *args: object) -> None:
        """
        Adds an item to the back of the queue.
        """
        for item in args:
            if self.is_full:
                raise FullQueueError("The queue is full.")
            else:
                self._queue.append(item)


    def dequeue(self) -> Any:
        """
        Removes the item from at front of the queue.
        """
        if self.is_empty:
            raise EmptyQueueError("The queue is empty.")
        else:
            dequeued = self.front
            self._queue.pop(0)
            return dequeued
        

    def clear(self) -> None:
        """
        Clears the queue.
        """
        self._queue.clear()


    @property
    def front(self) -> Any:
        """
        Returns the item at the front of
        the queue without dequeueing it.
        """
        if self.is_empty:
            raise EmptyQueueError("The queue is empty.")
        else:
            return self._queue[0]


    @property
    def rear(self) -> Any:
        """
        Returns the item at the rear of
        the queue without dequeueing it.
        """
        if self.is_empty:
            raise EmptyQueueError("The queue is empty.")
        else:
            return self._queue[-1]


    @property
    def is_empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self) <= 0:
            return True
        else:
            return False


    @property
    def is_full(self) -> bool:
        """
        Returns whether the queue is full.
        """
        if self._capacity is not None:
            if len(self) >= self._capacity:
                return True
            else:
                return False
        else:
            return False


    def extend(self, other: Queue) -> Queue:
        """
        Extends this queue with another queue.
        """
        for item in other._queue:
            self.enqueue(item)
        return self
    