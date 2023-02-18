#jutils/test/exceptions/test_emptypipeline.py
from jutl.exceptions import EmptyPipelineError

test_message = "Test message"
def func():
    raise EmptyPipelineError(test_message)

class TestException():
    def test_message(self):
        "Tests if the exception message is correct."
        exception = EmptyPipelineError(test_message)
        assert exception.message == test_message
