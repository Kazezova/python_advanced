import random
def guess_game():
    questions= {
        'colibri' : 'This bird can fly backwards.',
        'snail' : 'These animals, considered a delicacy in some countries, have teeth located on the tongue.',
        'crocodile' : 'The cubs of this animal acquire sex depending on the ambient temperature.'
    }
    data = {'1': 0, '2': 0}
    secret_word = list(questions.keys())[random.randint(0, len(questions)-1)]
    board = list("*" * len(secret_word))
    print(f'\n{questions[secret_word]} What is it?')
    j = -1
    while True:
        if ''.join(board) == secret_word:
            print(f'\nCongratulations!\n{data}')
            if data['1'] == data['2']:
                print('Draw!')
                break
            else:
                print('Winner - player {}'.format([k for k,v in data.items() if v == max(data['1'], data['2'])][0]))
                break
        j += 1
        player = (j%2) + 1
        point = random.randint(5, 10)
        print(f"\n-------------------------------------------------\nPlayer {player}. {' '.join(board)}\n{point} points at stake.")
        user_guess = input("Enter a word or a letter: ").lower()
        if len(user_guess) == 1:
            if user_guess in board: 
                print('This letter already guessed! Next player.')
                continue
            for i in range(len(secret_word)):
                if secret_word[i] == user_guess:
                    board[i] = user_guess
            if user_guess not in board:
                print('Incorrect! Next player.')
                continue
            data[str(player)] = data[str(player)] + point
            print(f'Correct! You get {point} points.')
        else:
            if user_guess == secret_word:
                unguess = sum([1 for each in board if each=='*'])
                data[str(player)] = data[str(player)] + point*unguess
                print(f"Correct! You get {point*unguess} points.\n\nCongratulations!\n{data}\nWinner - player {player}")
                break
            else:
                print("Incorrect! Next player.")
    return None

while True:
    choose = input("\nWant to guess the word? Y or N: ")
    if choose == 'Y':
        guess_game()
    else:
        print("Thanks for your game!")
        break