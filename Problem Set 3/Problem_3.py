def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    i="abcdefghijklmnopqrstuvwxyz"
    j=""
    for string in i:
        if string not in lettersGuessed:
            j+=string
    return j
