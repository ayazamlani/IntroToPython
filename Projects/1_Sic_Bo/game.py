import random

# Create the Dice
DICE_1 = random.randint(1,6)
DICE_2 = random.randint(1,6)
DICE_3 = random.randint(1,6)

# Add the Dice
DICE_SUM = sum([DICE_1, DICE_2, DICE_3])

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
    DICE_BIG_SMALL = "BIG/SMALL: HOUSE WINS"
    DICE_EVEN_ODD = "HOUSE WINS"


print(f'\n\t\
{DICE_TRIPLE}\n\t\
{DICE_SUM}\n\t\
{DICE_BIG_SMALL}\n\t\
{DICE_EVEN_ODD}\n\t\
\n\t\
DICE #1: {DICE_1}\n\t\
DICE #2: {DICE_2}\n\t\
DICE #3: {DICE_3}\n\t\
')
