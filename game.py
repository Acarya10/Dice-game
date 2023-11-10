import random

dice_art = [
    '''
    -------
    |     |
    |  •  |
    |     |
    -------
    ''',
    '''
    -------
    | •   |
    |     |
    |   • |
    -------
    ''',
    '''
    -------
    | •   |
    |  •  |
    |   • |
    -------
    ''',
    '''
    -------
    | • • |
    |     |
    | • • |
    -------
    ''',
    '''
    -------
    | • • |
    |  •  |
    | • • |
    -------
    ''',
    '''
    -------
    | • • |
    | • • |
    | • • |
    -------
    '''
]

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

def display_dice(dice1, dice2):
    print(dice_art[dice1 - 1])
    print(dice_art[dice2 - 1])

while True:
    input("Press Enter to roll the dice...")
    dice1, dice2 = roll_dice()
    print("Dice 1:")
    display_dice(dice1, 1)
    print("Dice 2:")
    display_dice(dice2, 1)
    
    total = dice1 + dice2
    print(f"Total: {total}")

    choice = input("Roll again? (y/n): ").lower()
    if choice != 'y':
        print("Thanks for playing! Goodbye!")
        break
