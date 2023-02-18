from .color import Text, Background
from .text import Typography, Reset
from jutl.exceptions import InvalidFormattingError

__all__ = ['apply', 'test']

def apply(text: str, text_color: str = None, background_color: str = None, typography: str = None) -> str:
    formatting = ""

    if text_color is not None:
        if text_color.upper() in Text.colors:
            formatting += Text.colors[text_color.upper()]
        else:
            raise InvalidFormattingError(f"Color not found: {text_color}")
    if background_color is not None:
        if background_color.upper() in Background.colors:
            formatting += Background.colors[background_color.upper()]
        else:
            raise InvalidFormattingError(f"Color not found: {background_color}")
    if typography is not None:
        if typography.upper() in Typography.types:
            formatting += Typography.types[typography.upper()]
        else:
            raise InvalidFormattingError(f"Type not found: {typography}")
    return formatting + text + Reset.types['ALL']

def test():
    """
    Test function which executes test
    functions from formatting classes.
    """
    Text.test()
    Background.test()
    Typography.test()
