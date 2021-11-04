import re

def check_included(word, included):
    """
    Check if word is included in included

    Parameters
    ----------
    word : str
        Word to check
    included : str
        Included string

    Returns
    -------
    bool  : True if word is included in included, False otherwise
    """
    for i in included:
        if i in word:
            return True
    return False
