


def prefixtable(text: str) -> list:
    """
    Return the prefixtable for text

    Return a list containing the length of the largest proper prefix that is also a sufix
    for each length of text. prefixtable[i] contains the length of lps for text[:i+1].

    Example: 
    text = 'AAAB'
    prefixtable = [0, 1, 2, 0]

    @param text str The text for which prefix table should be found. Can not be None
    @return prefixtable list 
    """

    i, j = 1, 0

    textlen = len(text)
    prefixtable = [0] * textlen

    while i < textlen:

        if text[i] == text[j]:
            j += 1
            prefixtable[i] = j
            i += 1
        else:
            if j > 0:
                j = prefixtable[j - 1]
            else:
                i += 1

    return prefixtable



def match(text:str, pattern:str) -> int :
    """Return the index of first occurence of pattern in text"""
    
    lps = prefixtable(pattern)

    textidx, patternidx = 0, 0

    while textidx < len(text):
        if text[textidx] == pattern[patternidx]:
            textidx += 1
            patternidx += 1

        else:
            if patternidx > 0:
                patternidx = lps[patternidx - 1]
            else:
                textidx += 1


        if patternidx == len(pattern):
            return textidx - patternidx


    return -1
