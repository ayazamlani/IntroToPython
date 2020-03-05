import random


GUESS_VERIFIED = False
while not GUESS_VERIFIED:
    GUESS = input('Guess a Number between 4-17:\n\t++')
    try:
        GUESS = int(GUESS)
        if GUESS < 4:
            print('Number too low')
        elif GUESS > 17:
            print('Number too high')
        else:
            GUESS_VERIFIED = True

    except Exception as e:
        print(f'{e}\nTry Entering a number not words...')


# Create the Dice
DICE_1 = random.randint(1, 6)
DICE_2 = random.randint(1, 6)
DICE_3 = random.randint(1, 6)

DICE = [DICE_1, DICE_2, DICE_3]

# Add the Dice
DICE_SUM = sum(DICE)

# See if Dice rolled Trips
if DICE_1 == DICE_2 == DICE_3:
    DICE_TRIPLE = f"\n\tTRIP {DICE_1}'s\n\tTRIP {DICE_2}'s\n\tTRIP {DICE_3}'s\n"
else:
    DICE_TRIPLE = ""

# If not trips, Assign High/Low, Even/Odd
if DICE_TRIPLE == "":
    if DICE_SUM < 11:
        DICE_BIG_SMALL = "SMALL"
    else:
        DICE_BIG_SMALL = "BIG"

    if DICE_SUM % 2 == 0:
        DICE_EVEN_ODD = "EVEN"
    else:
        DICE_EVEN_ODD = "ODD"

# If trips Assign High/Low, Even/Odd as HOUSE WINS
else:
    DICE_BIG_SMALL = "HOUSE WINS"
    DICE_EVEN_ODD = "HOUSE WINS"


print(f'\n\t\
{DICE_TRIPLE}\n\t\
#{DICE_SUM}\n\t\
Big or Small: {DICE_BIG_SMALL}\n\t\
Even or Odd: {DICE_EVEN_ODD}\n\t\
\n\t\
DICE #1: {DICE_1}\n\t\
DICE #2: {DICE_2}\n\t\
DICE #3: {DICE_3}\n\t\
')


def win():
    print('YOU WIN')
    print('YOU WIN')
    print('YOU WIN')
    print('YOU WIN')
    print('YOU WIN')
    print('YOU WIN')


if int(GUESS) == DICE_SUM:
    print('YOU WIN')
    print('YOU WIN')
    print('YOU WIN')
    print('YOU WIN')
    print('YOU WIN')
    print('YOU WIN')
