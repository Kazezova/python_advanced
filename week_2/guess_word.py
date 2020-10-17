import random
def guess_game():
    questions= {
        'colibri' : 'This bird can fly backwards.',
        'snail' : 'These animals, considered a delicacy in some countries, have teeth located on the tongue.',
        'crocodile' : 'The cubs of this animal acquire sex depending on the ambient temperature.'
    }
    data = {'1': {'point':0, 'prize':[]}, '2': {'point':0, 'prize':[]}}
    gain = [200, 100, 450, 400, 'prize', 150, 500, 350, 250, 50, 300]
    prize = ['car', 'toy', 'notebook', 'laptop', 'trip to Bali', 'guitar', 'headphones']
    secret_word = list(questions.keys())[random.randint(0, len(questions)-1)]
    board = list("*" * len(secret_word))
    print(f'\n{questions[secret_word]} What is it?')
    j = -1
    while True:
        if ''.join(board) == secret_word:
            print(f'\nCongratulations!\n{data}')
            if data['1']['point'] == data['2']['point']:
                print('Draw!')
                break
            else:
                print('Winner - player {}'.format([k for k, v in data.items() if v['point'] == max(data['1']['point'], data['2']['point'])][0]))
                break
        j += 1
        player = (j%2) + 1
        r = random.randint(0, len(gain)-1)
        if gain[r] == 'prize':
            #start trade
            print('\n*****SECTOR PRIZE ON THE DRUM*****')
            money = 0
            until = random.randint(5, 10)
            for i in range(0, until):
                if i == until-1:
                    user_gain = prize[random.randint(0, len(prize)-1)]
                    data[str(player)]['prize'].append(user_gain)
                    print(f'\nWell done! You get {user_gain}!')
                money += random.randrange(100, 200, 50)
                choise = input(f'Player {player}, prize or money? I\'ll give you {money}$!: ')
                if choise.lower() == 'prize':
                    continue
                else:
                    data[str(player)]['point'] = data[str(player)]['point'] + money
                    print(f'\nYou get {money}$.')
                    break
            continue
        else:
            point = gain[r]
        print(f"\n-------------------------------------------------\nPlayer {player}. {' '.join(board)}\n{point}$ at stake.")
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
            data[str(player)]['point'] = data[str(player)]['point'] + point
            print(f'Correct! You get {point}$.')
        else:
            if user_guess == secret_word:
                # unguess = sum([1 for each in board if each=='*'])
                data[str(player)]['point'] = data[str(player)]['point'] + point
                print(f"Correct! You get {point}$.\n\nCongratulations!\n{data}\nWinner - player {player}")
                break
            else:
                print("Incorrect! Next player.")
    return None

while True:
    choose = input("\nWant to guess the word? Y or N: ")
    if choose.upper() == 'Y':
        guess_game()
    else:
        print("Thanks for your game!")
        break