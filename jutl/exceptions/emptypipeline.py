# Module imports

# External class visibility
__all__ = ['EmptyPipelineError']

class EmptyPipelineError(Exception):
    def __init__(self, message):
        self.message = message