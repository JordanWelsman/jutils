class TextColor:
    # Text color constants
    DEFAULT         =       '\033[39m'

    BLACK           =       '\033[30m'
    RED             =       '\033[31m'
    GREEN           =       '\033[32m'
    YELLOW          =       '\033[33m'
    BLUE            =       '\033[34m'
    MAGENTA         =       '\033[35m'
    CYAN            =       '\033[36m'
    LIGHTGRAY       =       '\033[37m'
    DARKGRAY        =       '\033[90m'
    LIGHTRED        =       '\033[91m'
    LIGHTGREEN      =       '\033[92m'
    LIGHTYELLOW     =       '\033[93m'
    LIGHTBLUE       =       '\033[94m'
    LIGHTMAGENTA    =       '\033[95m'
    LIGHTCYAN       =       '\033[96m'
    WHITE           =       '\033[97m'

    def test():
        print(f"\nTesting {__name__}.TextColor...\n")
        print(f"{TextColor.DEFAULT}█████{TextColor.BLACK}█████{TextColor.DARKGRAY}█████{TextColor.LIGHTGRAY}█████{TextColor.WHITE}█████{TextColor.DEFAULT}")
        print(f"{TextColor.RED}█████{TextColor.GREEN}█████{TextColor.YELLOW}█████{TextColor.BLUE}█████{TextColor.MAGENTA}█████{TextColor.CYAN}█████{TextColor.DEFAULT}")
        print(f"{TextColor.LIGHTRED}█████{TextColor.LIGHTGREEN}█████{TextColor.LIGHTYELLOW}█████{TextColor.LIGHTBLUE}█████{TextColor.LIGHTMAGENTA}█████{TextColor.LIGHTCYAN}█████{TextColor.DEFAULT}\n")


class BackgroundColor:
    # Background color constants
    DEFAULT         =       '\033[49m'

    BLACK           =       '\033[40m'
    RED             =       '\033[41m'
    GREEN           =       '\033[42m'
    YELLOW          =       '\033[43m'
    BLUE            =       '\033[44m'
    MAGENTA         =       '\033[45m'
    CYAN            =       '\033[46m'
    LIGHTGRAY       =       '\033[47m'
    DARKGRAY        =       '\033[100m'
    LIGHTRED        =       '\033[101m'
    LIGHTGREEN      =       '\033[102m'
    LIGHTYELLOW     =       '\033[103m'
    LIGHTBLUE       =       '\033[104m'
    LIGHTMAGENTA    =       '\033[105m'
    LIGHTCYAN       =       '\033[106m'
    WHITE           =       '\033[107m'

    def test():
        print(f"\nTesting {__name__}.BackgroundColor...\n")
        print(f"{BackgroundColor.DEFAULT}|||||{BackgroundColor.BLACK}|||||{BackgroundColor.DARKGRAY}|||||{BackgroundColor.LIGHTGRAY}|||||{BackgroundColor.WHITE}|||||{BackgroundColor.DEFAULT}")
        print(f"{BackgroundColor.RED}|||||{BackgroundColor.GREEN}|||||{BackgroundColor.YELLOW}|||||{BackgroundColor.BLUE}|||||{BackgroundColor.MAGENTA}|||||{BackgroundColor.CYAN}|||||{BackgroundColor.DEFAULT}")
        print(f"{BackgroundColor.LIGHTRED}|||||{BackgroundColor.LIGHTGREEN}|||||{BackgroundColor.LIGHTYELLOW}|||||{BackgroundColor.LIGHTBLUE}|||||{BackgroundColor.LIGHTMAGENTA}|||||{BackgroundColor.LIGHTCYAN}|||||{BackgroundColor.DEFAULT}\n")
