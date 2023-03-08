# Module imports

# External class visibility
__all__ = ['JutilsException']

class JutilsException(Exception):
    def __init__(self, message):
        self.message = message