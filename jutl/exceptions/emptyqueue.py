# Module imports
from .jutlexception import JutilsException

# External class visibility
__all__ = ['EmptyQueueError']

class EmptyQueueError(JutilsException):
    pass