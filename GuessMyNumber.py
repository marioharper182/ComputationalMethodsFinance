__author__ = 'Mario'

import numpy as np
import matplotlib.pyplot as plt
import itertools

def Guessengine(A):
    print(A)
    numbertoguess = int(A)

    low = 0
    high = 101

    matplotlist = [50]
    trieslist = [0]
    guess = [50]
    g = 0
    counter = 0
    # i = 50
    while guess[-1] != numbertoguess:
        if guess[-1] < numbertoguess:
            if high is not None:
                g = (high - guess[-1]) // 2 + guess[-1]
            else:
                g = (max(guess)-guess[-1]) // 2 + guess[-1]
        # if min(guess) == 0:
        #     guess.remove(0)
            if low != None:
                low = None
            if g == guess[-1]:
                g = g + 1

        if guess[-1] > numbertoguess:
            if low is not None:
                g = guess[-1] - (guess[-1] - low)// 2
            else: g = guess[-1] - (guess[-1] - min(guess)) // 2
            # if max(guess) == 101:
            #     guess.remove(101)
            if high != None:
                high = None
            if g == guess[-1]:
                g = g - 1

        if counter > 1:
            guess.pop(0)

        matplotlist.append(g)
        guess.append(g)
        counter = counter +1
        trieslist.append(counter)
        print(guess[-1])

    if guess[-1] == numbertoguess:
        print("Success! Took", counter+1, "tries")

        tuples = zip(trieslist, matplotlist)
        plt.figure(1)
        plt.plot(trieslist, matplotlist, 'bo',linestyle = '-', linewidth = 2.00)
        # plt.plot([guess[-1], 0 ], [guess[-1], len(trieslist)], 'r', linestyle = '-', linewidth = 1.00)
        # plt.plot(*zip(*itertools.chain.from_iterable(itertools.combinations(tuples, 2))), color = 'blue',marker = 'o', linewidth = 2.00)
        plt.show()

def Matplotwindow():
    pass

    # tries = trieslist