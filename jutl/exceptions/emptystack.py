# Module imports
from .jutlexception import JutilsException

# External class visibility
__all__ = ['EmptyStackError']

class EmptyStackError(JutilsException):
    pass