# External class visibility
__all__ = ['Text', 'Background']


class Text:
    # Text color dictionary
    colors = {
        'DEFAULT':          '\033[39m',

        'BLACK':            '\033[30m',
        'RED':              '\033[31m',
        'GREEN':            '\033[32m',
        'YELLOW':           '\033[33m',
        'BLUE':             '\033[34m',
        'MAGENTA':          '\033[35m',
        'CYAN':             '\033[36m',
        'LIGHTGRAY':        '\033[37m',
        'DARKGRAY':         '\033[90m',
        'LIGHTRED':         '\033[91m',
        'LIGHTGREEN':       '\033[92m',
        'LIGHTYELLOW':      '\033[93m',
        'LIGHTBLUE':        '\033[94m',
        'LIGHTMAGENTA':     '\033[95m',
        'LIGHTCYAN':        '\033[96m',
        'WHITE':            '\033[97m'
        }

    def test() -> None:
        print(f"\nTesting {__name__}.Text...\n")
        print(f"{Text.colors['DEFAULT']}█████{Text.colors['BLACK']}█████{Text.colors['DARKGRAY']}█████{Text.colors['LIGHTGRAY']}█████{Text.colors['WHITE']}█████{Text.colors['DEFAULT']}")
        print(f"{Text.colors['RED']}█████{Text.colors['GREEN']}█████{Text.colors['YELLOW']}█████{Text.colors['BLUE']}█████{Text.colors['MAGENTA']}█████{Text.colors['CYAN']}█████{Text.colors['DEFAULT']}")
        print(f"{Text.colors['LIGHTRED']}█████{Text.colors['LIGHTGREEN']}█████{Text.colors['LIGHTYELLOW']}█████{Text.colors['LIGHTBLUE']}█████{Text.colors['LIGHTMAGENTA']}█████{Text.colors['LIGHTCYAN']}█████{Text.colors['DEFAULT']}\n")


class Background:
    # Background color dictionary
    colors = {
        'DEFAULT':          '\033[49m',

        'BLACK':            '\033[40m',
        'RED':              '\033[41m',
        'GREEN':            '\033[42m',
        'YELLOW':           '\033[43m',
        'BLUE':             '\033[44m',
        'MAGENTA':          '\033[45m',
        'CYAN':             '\033[46m',
        'LIGHTGRAY':        '\033[47m',
        'DARKGRAY':         '\033[100m',
        'LIGHTRED':         '\033[101m',
        'LIGHTGREEN':       '\033[102m',
        'LIGHTYELLOW':      '\033[103m',
        'LIGHTBLUE':        '\033[104m',
        'LIGHTMAGENTA':     '\033[105m',
        'LIGHTCYAN':        '\033[106m',
        'WHITE':            '\033[107m'
    }
    
    def test() -> None:
        print(f"\nTesting {__name__}.Background...\n")
        print(f"{Background.colors['DEFAULT']}|||||{Background.colors['BLACK']}|||||{Background.colors['DARKGRAY']}|||||{Background.colors['LIGHTGRAY']}|||||{Background.colors['WHITE']}|||||{Background.colors['DEFAULT']}")
        print(f"{Background.colors['RED']}|||||{Background.colors['GREEN']}|||||{Background.colors['YELLOW']}|||||{Background.colors['BLUE']}|||||{Background.colors['MAGENTA']}|||||{Background.colors['CYAN']}|||||{Background.colors['DEFAULT']}")
        print(f"{Background.colors['LIGHTRED']}|||||{Background.colors['LIGHTGREEN']}|||||{Background.colors['LIGHTYELLOW']}|||||{Background.colors['LIGHTBLUE']}|||||{Background.colors['LIGHTMAGENTA']}|||||{Background.colors['LIGHTCYAN']}|||||{Background.colors['DEFAULT']}\n")
