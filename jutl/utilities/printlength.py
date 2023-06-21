# Exteernal visibility
__all__ = ['printlen']


def printlen(item) -> int:
    """
    Prints the length of the passed item.
    Use this instead of `print(len(item))`.
    This is possibly the laziest function I've ever written.
    """
    assert hasattr(item, '__len__')
    print(len(item))
