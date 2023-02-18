# Module imports

# External class visibility
__all__ = ['MissingInputError']

class MissingInputError(Exception):
    def __init__(self, message):
        self.message = message