# Module imports

# External class visibility
__all__ = ['InvalidFormattingError']

class InvalidFormattingError(Exception):
    def __init__(self, message):
        self.message = message