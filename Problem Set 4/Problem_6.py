def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    # TO DO ... <-- Remove this comment when you code this function
    hand={}
    while True:
        select=input('Enter n to deal a new hand, r to replay the last hand, or e to end game:')
        if select == 'n':
            hand=dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        elif select == 'r':
            if len(hand)==0:
                print('You have not played a hand yet. Please play a new hand first!')
            else:
                playHand(hand, wordList, HAND_SIZE)
        elif select == 'e':    
            break
        else:
            print('Invalid command.')
