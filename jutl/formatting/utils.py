from .color import TextColor, BackgroundColor
from .text import Typography, Reset

__all__ = ['apply']

def apply(text: str, text_color: str = None, background_color: str = None, typography: str = None) -> str:
    formatting = ''
    if text_color is not None and text_color in TextColor.options:
        formatting += TextColor.str(text_color.upper())
    if background_color is not None and background_color in BackgroundColor.options:
        formatting += BackgroundColor.str(background_color.upper())
    if typography is not None and typography in Typography.options:
        formatting += Typography.str(typography.upper())
    
    return formatting + text + Reset.ALL
