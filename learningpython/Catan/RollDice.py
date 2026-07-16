import random

def roll():
    return random.randint(1,6)+random.randint(1,6)

dice = roll()

print(f'You rolled {dice}!')