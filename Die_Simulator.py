import random

def main():
    player1_wins = 0
    player1 = 0
    player2_wins = 0
    player2 = 0
    rounds = 1

    print('Dice Simulator Project\n')


    while rounds != 11:
        print('Round' + str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        print('Player 1 Roll: ' + str(player1))
        print('Player 2 Roll: ' + str(player2))

        rounds += 1

        if player1 == player2:
            print('Draw\n')
        elif player1 > player2:
            player1_wins += 1
            print('Player 1 wins !\n')
        else:
            print('Player 2 wins !\n')
            player2_wins += 1

    if player1_wins == player2_wins:
        print('Draw\n')
    elif player1_wins > player2_wins:
        print('Player 1 Wins - Rounds won : ' + str(player1_wins))
    else:
        print('Player 2 Wins - Rounds won : ' + str(player2_wins))



def dice_roll():
    diceRoll = random.randint(1,6)
    return diceRoll

main()