from .color import Text, Background
from .text import Typography, Reset

__all__ = ['apply', 'test']

def apply(text: str, text_color: str = None, background_color: str = None, typography: str = None) -> str:
    formatting = ""

    if text_color is not None:
        formatting += Text.colors[text_color.upper()]
    if background_color is not None:
        formatting += Background.colors[background_color.upper()]
    if typography is not None:
        formatting += Typography.types[typography.upper()]
    return formatting + text + Reset.types['ALL']

def test():
    """
    Test function which executes test
    functions from formatting classes.
    """
    Text.test()
    Background.test()
    Typography.test()
