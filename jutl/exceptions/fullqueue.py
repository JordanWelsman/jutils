# Module imports
from .jutlexception import JutilsException

# External class visibility
__all__ = ['FullQueueError']

class FullQueueError(JutilsException):
    pass