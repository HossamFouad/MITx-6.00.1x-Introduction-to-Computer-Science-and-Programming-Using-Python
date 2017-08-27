def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE (download ps4a.py to see)

    total_score=0
    list1=[]
    while True :
        for i in hand:
            for j in range(hand[i]):
                list1.append(i)
        list1.sort()        
        print ("Current Hand: "," ".join([k for k in list1]))
        word=input(' Enter word, or a "." to indicate that you are finished:')
        if word==".":
            print('Goodbye! Total score:',total_score,'points.')
            break
        elif not isValidWord(word, hand, wordList):
            print('Invalid word, please try again.')
            continue
        hand = updateHand(hand, word)
        total_score+=getWordScore(word, n)
        print( word,'earned', getWordScore(word, n) ,'points. Total:',total_score,'points')
        if calculateHandlen(hand) ==0 :
            print('Run out of letters. Total score:',total_score,'points.')
            break        
        
            

