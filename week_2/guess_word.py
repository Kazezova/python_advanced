import random
what_word = random.randint(0,3)
guess_word = ['python', 'computer', 'telephone', 'mcm']
# hint = "What would you use to play Doom-2?"
the_word = guess_word[what_word]
game_over = False
board = list("*" * len(the_word))
data = {'1': 0, '2': 0}
j = -1
while not game_over:
    if ''.join(board) == the_word:
        print('WIN!')
        print(data)
        if data['1'] == data['2']:
            print('Draw!')
            break
        else:
            print('Winner {}'.format([k for k,v in data.items() if v == max(data['1'], data['2'])][0]))
            break
    print("")
    print("------------------------------")
    print(f"Guess a word: {' '.join(board)}")
    j += 1
    player = (j%2) + 1
    print(f"Player {player}.")
    user_guess = input("Enter a word or a letter: ")
    user_guess = user_guess.lower()
    if len(user_guess) == 1:
        if user_guess in board: 
            print('Already guessed!')
            continue
        for i in range(len(the_word)):
            if the_word[i] == user_guess:
                board[i] = user_guess
                point = random.randint(5, 10)
                data[str(player)] = data[str(player)] + point
        if user_guess not in board:
            print('Incorrect!')    
    else:
        if user_guess == the_word:
            unguess = 0
            for i in board:
                if i=='*':
                    unguess+=1
            print("Correct! Congratulations!")
            print(f'Winner {player}')
            point = random.randint(5, 10)
            data[str(player)] = data[str(player)] + point*unguess
            print(data)
            game_over = True
        else:
            print("Incorrect, think again.")
# if the letter is incorrect, show some message
# if the letter is already guessed, do not change anything
# randomly add some points if a letter is guessed
# Have a list of words, and randomly pick a word from a list
# Two players game. Player one's turn. Guess the word.