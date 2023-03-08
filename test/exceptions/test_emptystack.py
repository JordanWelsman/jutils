#jutils/test/exceptions/test_emptyqueue.py
from jutl.exceptions import EmptyStackError

test_message = "Test message"
def func():
    raise EmptyStackError(test_message)

class TestException():
    def test_message(self):
        "Tests if the exception message is correct."
        exception = EmptyStackError(test_message)
        assert exception.message == test_message
