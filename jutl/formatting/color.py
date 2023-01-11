class TextColor:
    # TextColor constants
    DEFAULT =       '\033[39m'
    BLACK =         '\033[30m'
    RED =           '\033[31m'
    GREEN =         '\033[32m'
    YELLOW =        '\033[33m'
    BLUE =          '\033[34m'
    MAGENTA =       '\033[35m'
    CYAN =          '\033[36m'
    LIGHTGRAY =     '\033[37m'
    DARKGRAY =      '\033[90m'
    LIGHTRED =      '\033[91m'
    LIGHTGREEN =    '\033[92m'
    LIGHTYELLOW =   '\033[93m'
    LIGHTBLUE =     '\033[94m'
    LIGHTMAGENTA =  '\033[95m'
    LIGHTCYAN =     '\033[96m'
    WHITE =         '\033[97m'

    def test():
        print(f"{TextColor.DEFAULT}█{TextColor.BLACK}█{TextColor.DARKGRAY}█{TextColor.LIGHTGRAY}█{TextColor.WHITE}█")
        print(f"{TextColor.RED}█{TextColor.GREEN}█{TextColor.YELLOW}█{TextColor.BLUE}█{TextColor.MAGENTA}█{TextColor.CYAN}█")
        print(f"{TextColor.LIGHTRED}█{TextColor.LIGHTGREEN}█{TextColor.LIGHTYELLOW}█{TextColor.LIGHTBLUE}█{TextColor.LIGHTMAGENTA}█{TextColor.LIGHTCYAN}█{TextColor.DEFAULT}")