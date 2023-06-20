# External class visibility
__all__ = ['pluralize']


def pluralize(criteria: int, single_string: str, plural_string: str, zero_string: str = None) -> str:
    """
    Returns one of two passed strings depending on if
    the iterable contains one or more than 1 element.
    """
    if criteria < -1 or criteria > 1: # if absoolute(0) > 1
        return plural_string
    elif criteria in {-1, 1}: # if absolute(0) == 1 or -1
        return single_string
    elif criteria == 0: # if absolute(0) == 0
        return zero_string if zero_string else plural_string
