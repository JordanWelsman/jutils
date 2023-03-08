# Module imports
from __future__ import annotations
from typing import Any
from jutl.exceptions import EmptyStackError, FullStackError
from jutl.formatting import apply

# External class visibility
__all__ = ['Stack']


class Stack(object):
    """
    Class which implements a
    first-in-last-out stack object
    with stack methods.
    """
    def __init__(self, name: str = None, capacity: int = None) -> None:
        "Initialization method."
        self.name: str = name
        self._stack: list = []
        self._capacity: int = capacity

    def __repr__(self) -> str:
        """
        Tells the interpreter how
        to represent this class.
        """
        if self.name is None:
            if len(self) == 0:
                return "Stack()"
            else:
                return f"Stack({self._stack})"

        else:
            if len(self) == 0:
                return f"Stack({self.name})"
            else:
                return f"Stack({self.name}, {self._stack})"
        
    def __call__(self) -> list:
        """
        Tells the interpreter what to
        do when an object of this
        class is called directly.
        """
        return self._stack
    
    def __len__(self) -> int:
        """
        Tells the interpreter what to
        consider this class' length.
        """
        return len(self._stack)
    
    def __iter__(self) -> iter:
        """
        Tells the interpreter what to
        iterate over when iterator methods
        are called on this class.
        """
        raise NotImplementedError("Stacks are not iterable.")
    
    def __eq__(self, other) -> bool:
        """
        Tells the interpreter how this class
        handles equal operators.
        """
        return self._stack == other._stack
    
    def __ne__(self, other) -> bool:
        """
        Tells the interpreter how this class
        handles not equal operators.
        """
        return self._stack != other._stack

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


    def push(self, *args: object) -> None:
        """
        Pushes an item onto the stack.
        """
        for item in args:
            if self.is_full:
                raise FullStackError("The stack is full.")
            else:
                self._stack.append(item)


    def pop(self) -> Any:
        """
        Removes the item at the top of the stack.
        """
        if self.is_empty:
            raise EmptyStackError("The stack is empty.")
        else:
            popped = self.top
            self._stack.pop(-1)
            return popped
    

    def clear(self) -> None:
        """
        Clears the stack.
        """
        self._stack.clear()


    @property
    def top(self) -> Any:
        """
        Returns the item at the top of
        the stack without popping it.
        """
        if self.is_empty:
            raise EmptyStackError("The stack is empty.")
        else:
            return self._stack[-1]
        
    
    @property
    def bottom(self) -> Any:
        """
        Returns the item at the bottom
        of the stack without popping it.
        """
        if self.is_empty:
            raise EmptyStackError("The stack is empty.")
        else:
            return self._stack[0]


    @property
    def is_empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self) == 0:
            return True
        else:
            return False


    @property
    def is_full(self) -> bool:
        """
        Returns whether the stack is full.
        """
        if self._capacity is not None:
            if len(self) >= self._capacity:
                return True
            else:
                return False
        else:
            return False


    def extend(self, other: Stack) -> Stack:
        """
        Extends this stack with another stack.
        """
        for item in other._stack:
            self.push(item)
        return self
    