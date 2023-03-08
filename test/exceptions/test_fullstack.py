#jutils/test/exceptions/test_emptyqueue.py
from jutl.exceptions import FullStackError

test_message = "Test message"
def func():
    raise FullStackError(test_message)

class TestException():
    def test_message(self):
        "Tests if the exception message is correct."
        exception = FullStackError(test_message)
        assert exception.message == test_message
