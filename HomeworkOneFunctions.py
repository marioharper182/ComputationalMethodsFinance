__author__ = 'mario'

def main():
    useinput = input("Would you like to excecute the chicken nugget simulation [0] or guessing game [1]? " )

    if useinput is '0' or 'y':
        chickennugget_main()
    else:
        guessinggame_main()


def chickennugget_main():

    clst = [6, 9, 20]

    dumplist = [clst[0]*x+clst[1]*y+clst[2]*z for x in range(0,40) for y in range(0, 30) for z in range(0, 15)]
    setlist = list(set(dumplist))
    keyvalues = [setlist[x] for x in range(1,(len(setlist)-1)) if setlist[x]+1 != setlist[x+1] and setlist[x]<100]

    answer = [max(keyvalues)+1]
    print("The highest integer of chicken nuggets purchasable is:", answer[0])

def guessinggame_main():
    import random

    usernum = random.randint(1,100)
    print("To save you the hassle, you choose to pick the number:", usernum)
    print("The computer will now guess this number.")

    guess = 50
    guesslist = [guess]
    upperbound = 100
    lowerbound = 1
    counter = 1

    # for guess != usernum:
        # if

    while guesslist[-1] != usernum:
        if guesslist[-1] > usernum:
            guess = upperbound/guesslist[-1]
            guess = guesslist[-1] - guess//(counter*2)
            if guess == guesslist[-1]:
                guess = guesslist[-1]-1
        if guesslist[-1] < usernum:
            guess = guesslist[-1] + guess//(counter*2)
            if guess == guesslist[-1]:
                guess = guesslist[-1]+1

        guesslist.append(guess)
        counter = counter+1

    if guess == usernum:
        print("Found it: ", guess, "in {} tries", counter)

if __name__ == '__main__':
    main()