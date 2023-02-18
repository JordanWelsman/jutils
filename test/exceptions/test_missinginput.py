#jutils/test/exceptions/missinginput.py
from jutl.exceptions import MissingInputError

test_message = "Test message"
def func():
    raise MissingInputError(test_message)

class TestException():
    def test_message(self):
        "Tests if the exception message is correct."
        exception = MissingInputError(test_message)
        assert exception.message == test_message
