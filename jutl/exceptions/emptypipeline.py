# Module imports
from .jutlexception import JutilsException

# External class visibility
__all__ = ['EmptyPipelineError']

class EmptyPipelineError(JutilsException):
    pass