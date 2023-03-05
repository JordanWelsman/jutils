# Module imports
from __future__ import annotations
from jutl.formatting import apply

# External class visibility
__all__ = ['Stack']


class Stack(object):
    """
    Class which implements a
    first-in; first-out stack object
    with stack methods.
    """
    def __init__(self, name: str = None):
        "Initialization method."
        self.name = name
        self._stack = []

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


    def push(self, *args: object):
        """
        Pushes an item onto the stack.
        """
        for item in args:
            self._stack.append(item)


    def pop(self) -> object:
        """
        Removes the last added item from the stack.
        """
        popped = self.top
        self._stack.remove(self.top)
        return popped


    @property
    def top(self) -> object:
        if len(self) > 0:
            return self._stack[-1]
        else:
            raise IndexError("Stack is empty.")


    def extend(self, other: Stack) -> Stack:
        """
        Extends this stack with another stack.
        """
        for item in other._stack:
            self.push(item)
        return self
    