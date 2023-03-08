#jutils/test/exceptions/test_emptyqueue.py
from jutl.exceptions import EmptyQueueError

test_message = "Test message"
def func():
    raise EmptyQueueError(test_message)

class TestException():
    def test_message(self):
        "Tests if the exception message is correct."
        exception = EmptyQueueError(test_message)
        assert exception.message == test_message
