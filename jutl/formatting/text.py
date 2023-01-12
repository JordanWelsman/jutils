__all__ = ['Typography', 'Reset']


class Typography:
    # Text typography constants
    DEFAULT         =       '\033[0m'

    BOLD            =       '\033[1m'
    DIM             =       '\033[2m'
    ITALIC          =       '\033[3m'
    UNDERLINED      =       '\033[4m'
    BLINKING1       =       '\033[5m'
    BLINKING2       =       '\033[6m'
    INVERTED        =       '\033[7m'
    HIDDEN          =       '\033[8m'
    STRIKETHROUGH   =       '\033[9m'

    typography_types = ['BOLD', 'DIM', 'ITALIC', 'UNDERLINED', 'BLINKING1', 'BLINKING2', 'INVERTED', 'HIDDEN', 'STRIKETHROUGH']

    def test():
        print(f"\nTesting {__name__}.Typography...\n")
        print(f"{Typography.DEFAULT}Default{Reset.ALL}, {Typography.BOLD}Bold{Reset.ALL}, {Typography.DIM}Dim{Reset.ALL}, {Typography.ITALIC}Italic{Reset.ALL}, {Typography.UNDERLINED}Underlined{Reset.ALL},")
        print(f"{Typography.BLINKING1}Blinking{Reset.ALL}, {Typography.BLINKING2}Blinking{Reset.ALL}, {Typography.INVERTED}Inverted{Reset.ALL}, {Typography.HIDDEN}Hidden{Reset.ALL}, {Typography.STRIKETHROUGH}Strikethrough{Reset.ALL}\n")

    def apply(text: str, typography: str) -> str:
        if typography.upper() in typography_types:
            match typography.upper():
                case "BOLD":
                    return Typography.BOLD + text + Typography.DEFAULT
                case "DIM":
                    return Typography.DIM + text + Typography.DEFAULT
                case "ITALIC":
                    return Typography.ITALIC + text + Typography.DEFAULT
                case "UNDERLINED":
                    return Typography.UNDERLINED + text + Typography.DEFAULT
                case "BLINKING1":
                    return Typography.BLINKING1 + text + Typography.DEFAULT
                case "BLINKING2":
                    return Typography.BLINKING2 + text + Typography.DEFAULT
                case "INVERTED":
                    return Typography.INVERTED + text + Typography.DEFAULT
                case "HIDDEN":
                    return Typography.HIDDEN + text + Typography.DEFAULT
                case "STRIKETHROUGH":
                    return Typography.STRIKETHROUGH + text + Typography.DEFAULT
        else:
            raise Exception("Please specify a supported typography type.")


class Reset:
    # Reset typography constants
    ALL             =       '\033[0m'

    BOLD            =       '\033[21m'
    DIM             =       '\033[22m'
    ITALIC          =       '\033[23m'
    UNDERLINED      =       '\033[24m'
    BLINKING1       =       '\033[25m'
    BLINKING2       =       '\033[26m'
    INVERTED        =       '\033[27m'
    HIDDEN          =       '\033[28m'
    STRIKETHROUGH   =       '\033[29m'
