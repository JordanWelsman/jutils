# External class visibility
__all__ = ['Typography', 'Reset']


class Typography:
    # Text typography dictionary
    types = {
        'DEFAULT':          '\033[0m',

        'BOLD':             '\033[1m',
        'DIM':              '\033[2m',
        'ITALIC':           '\033[3m',
        'UNDERLINED':       '\033[4m',
        'BLINKING1':        '\033[5m',
        'BLINKING2':        '\033[6m',
        'INVERTED':         '\033[7m',
        'HIDDEN':           '\033[8m',
        'STRIKETHROUGH':    '\033[9m'
    }

    def test() -> None:
        print(f"\nTesting {__name__}.Typogrddaphy...\n")
        print(f"{Typography.types['DEFAULT']}Default{Reset.types['ALL']}, {Typography.types['BOLD']}Bold{Reset.types['ALL']}, {Typography.types['DIM']}Dim{Reset.types['ALL']}, {Typography.types['ITALIC']}Italic{Reset.types['ALL']}, {Typography.types['UNDERLINED']}Underlined{Reset.types['ALL']},")
        print(f"{Typography.types['BLINKING1']}Blinking{Reset.types['ALL']}, {Typography.types['BLINKING2']}Blinking{Reset.types['ALL']}, {Typography.types['INVERTED']}Inverted{Reset.types['ALL']}, {Typography.types['HIDDEN']}Hidden{Reset.types['ALL']}, {Typography.types['STRIKETHROUGH']}Strikethrough{Reset.types['ALL']}\n")


class Reset:
    # Reset typography dictionary
    types = {
        'ALL':              '\033[0m',

        'BOLD':             '\033[21m',
        'DIM':              '\033[22m',
        'ITALIC':           '\033[23m',
        'UNDERLINED':       '\033[24m',
        'BLINKING1':        '\033[25m',
        'BLINKING2':        '\033[26m',
        'INVERTED':         '\033[27m',
        'HIDDEN':           '\033[28m',
        'STRIKETHROUGH':    '\033[29m'
    }
    
