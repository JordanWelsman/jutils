#jutils/test/exceptions/test_emptyqueue.py
from jutl.exceptions import FullQueueError

test_message = "Test message"
def func():
    raise FullQueueError(test_message)

class TestException():
    def test_message(self):
        "Tests if the exception message is correct."
        exception = FullQueueError(test_message)
        assert exception.message == test_message
