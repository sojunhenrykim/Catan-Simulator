import random
print("Welcome to the Number Guessing Game! You have 3 lives for each level")
n = 1
while n < 20:
    x = [i for i in range (1, 5*n+1 )]
    x = random.choice(x)
    s = 3
    while s > 0:
        print("Level ", n, " ------------------ Guess a number between 1 and ", 5*n )
        guess = int(input("Guess here: "))
        if guess == x:
            n += 1
            if n == 21:
                break
            else: print("Your guess is correct, you are now in level ", n)
            break
        else:
            s += -1
            if s == 0:
                print("GAME OVER")
            else:
                print("Your guess is incorrect, try again. You have ", s, " lives left.")
    if s == 0:
        n = 22
if n == 21:
    print('Congratulations, you have completed the game') 

        

