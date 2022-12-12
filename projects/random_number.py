import random as rn

a = input("type a number! ")
if a.isdigit():
    a = int(a)

if a <= 0:
    print("please give a number larger than zero  ")
    quit()
else:
    print("type another number: ")
    quit

    random_number = rn.randint(0, a)
    guesses =0
    
while True:
    guesses += 1
    user_guess = input("make a guess! ")
    if user_guess.isdigit():
        user_guess= int(user_guess)
    else:
        print("type a number next time ")
        continue
    
    if user_guess ==  rn:
        print("you got it")
        break
    
    print("you got it in", guesses, "guesses")






    