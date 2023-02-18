#jutils/test/exceptions/test_invalidformatting.py
from jutl.exceptions import InvalidFormattingError

test_message = "Test message"
def func():
    raise InvalidFormattingError(test_message)

class TestException():
    def test_message(self):
        "Tests if the exception message is correct."
        exception = InvalidFormattingError(test_message)
        assert exception.message == test_message
