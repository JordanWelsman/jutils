# Module imports
from .jutlexception import JutilsException

# External class visibility
__all__ = ['MissingInputError']

class MissingInputError(JutilsException):
    pass