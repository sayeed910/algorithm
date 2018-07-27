

def match(text:str, pattern:str) -> int :
    pass

def prefixtable(text: str) -> list:
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

