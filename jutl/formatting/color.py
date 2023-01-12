__all__ = ['TextColor', 'BackgroundColor']


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

    options = ['BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'LIGHTGRAY', 'DARKGRAY', 'LIGHTRED', 'LIGHTGREEN', 'LIGHTYELLOW', 'LIGHTBLUE', 'LIGHTMAGENTA', 'LIGHTCYAN', 'WHITE']

    def test():
        print(f"\nTesting {__name__}.TextColor...\n")
        print(f"{TextColor.DEFAULT}█████{TextColor.BLACK}█████{TextColor.DARKGRAY}█████{TextColor.LIGHTGRAY}█████{TextColor.WHITE}█████{TextColor.DEFAULT}")
        print(f"{TextColor.RED}█████{TextColor.GREEN}█████{TextColor.YELLOW}█████{TextColor.BLUE}█████{TextColor.MAGENTA}█████{TextColor.CYAN}█████{TextColor.DEFAULT}")
        print(f"{TextColor.LIGHTRED}█████{TextColor.LIGHTGREEN}█████{TextColor.LIGHTYELLOW}█████{TextColor.LIGHTBLUE}█████{TextColor.LIGHTMAGENTA}█████{TextColor.LIGHTCYAN}█████{TextColor.DEFAULT}\n")

    def apply(text: str, color: str) -> str:
        if color.upper() in color_names:
            match color.upper():
                case "BLACK":
                    return TextColor.BLACK + text + TextColor.DEFAULT
                case "RED":
                    return TextColor.RED + text + TextColor.DEFAULT
                case "GREEN":
                    return TextColor.GREEN + text + TextColor.DEFAULT
                case "YELLOW":
                    return TextColor.YELLOW + text + TextColor.DEFAULT
                case "BLUE":
                    return TextColor.BLUE + text + TextColor.DEFAULT
                case "MAGENTA":
                    return TextColor.MAGENTA + text + TextColor.DEFAULT
                case "CYAN":
                    return TextColor.CYAN + text + TextColor.DEFAULT
                case "LIGHTGRAY":
                    return TextColor.LIGHTGRAY + text + TextColor.DEFAULT
                case "DARKGRAY":
                    return TextColor.DARKGRAY + text + TextColor.DEFAULT
                case "LIGHTRED":
                    return TextColor.LIGHTRED + text + TextColor.DEFAULT
                case "LIGHTGREEN":
                    return TextColor.LIGHTGREEN + text + TextColor.DEFAULT
                case "LIGHTYELLOW":
                    return TextColor.LIGHTYELLOW + text + TextColor.DEFAULT
                case "LIGHTBLUE":
                    return TextColor.LIGHTBLUE + text + TextColor.DEFAULT
                case "LIGHTMAGENTA":
                    return TextColor.LIGHTMAGENTA + text + TextColor.DEFAULT
                case "LIGHTCYAN":
                    return TextColor.LIGHTCYAN + text + TextColor.DEFAULT
                case "WHITE":
                    return TextColor.WHITE + text + TextColor.DEFAULT
        else:
            raise Exception("Please specify a supported color.")


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

    options = ['BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'LIGHTGRAY', 'DARKGRAY', 'LIGHTRED', 'LIGHTGREEN', 'LIGHTYELLOW', 'LIGHTBLUE', 'LIGHTMAGENTA', 'LIGHTCYAN', 'WHITE']

    def test():
        print(f"\nTesting {__name__}.BackgroundColor...\n")
        print(f"{BackgroundColor.DEFAULT}|||||{BackgroundColor.BLACK}|||||{BackgroundColor.DARKGRAY}|||||{BackgroundColor.LIGHTGRAY}|||||{BackgroundColor.WHITE}|||||{BackgroundColor.DEFAULT}")
        print(f"{BackgroundColor.RED}|||||{BackgroundColor.GREEN}|||||{BackgroundColor.YELLOW}|||||{BackgroundColor.BLUE}|||||{BackgroundColor.MAGENTA}|||||{BackgroundColor.CYAN}|||||{BackgroundColor.DEFAULT}")
        print(f"{BackgroundColor.LIGHTRED}|||||{BackgroundColor.LIGHTGREEN}|||||{BackgroundColor.LIGHTYELLOW}|||||{BackgroundColor.LIGHTBLUE}|||||{BackgroundColor.LIGHTMAGENTA}|||||{BackgroundColor.LIGHTCYAN}|||||{BackgroundColor.DEFAULT}\n")
    
    def apply(text: str, color: str) -> str:
        if color.upper() in color_names:
            match color.upper():
                case "BLACK":
                    return BackgroundColor.BLACK + text + BackgroundColor.DEFAULT
                case "RED":
                    return BackgroundColor.RED + text + BackgroundColor.DEFAULT
                case "GREEN":
                    return BackgroundColor.GREEN + text + BackgroundColor.DEFAULT
                case "YELLOW":
                    return BackgroundColor.YELLOW + text + BackgroundColor.DEFAULT
                case "BLUE":
                    return BackgroundColor.BLUE + text + BackgroundColor.DEFAULT
                case "MAGENTA":
                    return BackgroundColor.MAGENTA + text + BackgroundColor.DEFAULT
                case "CYAN":
                    return BackgroundColor.CYAN + text + BackgroundColor.DEFAULT
                case "LIGHTGRAY":
                    return BackgroundColor.LIGHTGRAY + text + BackgroundColor.DEFAULT
                case "DARKGRAY":
                    return BackgroundColor.DARKGRAY + text + BackgroundColor.DEFAULT
                case "LIGHTRED":
                    return BackgroundColor.LIGHTRED + text + BackgroundColor.DEFAULT
                case "LIGHTGREEN":
                    return BackgroundColor.LIGHTGREEN + text + BackgroundColor.DEFAULT
                case "LIGHTYELLOW":
                    return BackgroundColor.LIGHTYELLOW + text + BackgroundColor.DEFAULT
                case "LIGHTBLUE":
                    return BackgroundColor.LIGHTBLUE + text + BackgroundColor.DEFAULT
                case "LIGHTMAGENTA":
                    return BackgroundColor.LIGHTMAGENTA + text + BackgroundColor.DEFAULT
                case "LIGHTCYAN":
                    return BackgroundColor.LIGHTCYAN + text + BackgroundColor.DEFAULT
                case "WHITE":
                    return BackgroundColor.WHITE + text + BackgroundColor.DEFAULT
        else:
            raise Exception("Please specify a supported background color.")
