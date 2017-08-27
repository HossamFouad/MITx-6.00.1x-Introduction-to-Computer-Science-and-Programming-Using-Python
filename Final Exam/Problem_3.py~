def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    if not (word in wordList):
        return False
    k=getFrequencyDict(word)    
    
    try :
        for i in getFrequencyDict(word):
            if not(k[i]<=hand[i])  :
                return False
    except KeyError:
        return False
    return True        
