# Exteernal visibility
__all__ = ['printlen']


def printlen(*items) -> int:
    """
    Prints the length of the passed item.
    Use this instead of `print(len(item))`.
    This is possibly the laziest function I've ever written.
    """
    assert all(hasattr(item, '__len__') for item in items)
    print(*[len(item) for item in items], sep=", ")
