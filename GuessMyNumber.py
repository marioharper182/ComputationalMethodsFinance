__author__ = 'Mario'

import matplotlib.pyplot as plt
import numpy as np
import itertools

def Guessengine(A):

    A = int(A)

    # Basic Parameters
    low = 0
    high = 101
    guess = [50]
    g = 0
    counter = 0

    # Plotting information is stored here:
    matplotlist = [50]
    trieslist = [0]

    while guess[-1] != A:
        if guess[-1] < A:
            if high is not None:
                g = (high - guess[-1]) // 2 + guess[-1]
            else:
                g = (max(guess)-guess[-1]) // 2 + guess[-1]
            if low != None:
                low = None
            if g == guess[-1]:
                g = g + 1

        if guess[-1] > A:
            if low is not None:
                g = guess[-1] - (guess[-1] - low)// 2
            else: g = guess[-1] - (guess[-1] - min(guess)) // 2
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
        # print(guess[-1])

    if guess[-1] == A:

        plt.figure(1)
        plt.plot(trieslist, matplotlist, 'bo',linestyle = '-', linewidth = 2.00)
        plt.xlabel("Guess Iteration")
        plt.ylabel("Guessed Value")
        plt.title("Path to guess")
        # plt.plot([guess[-1], 0 ], [guess[-1], len(trieslist)], 'r', linestyle = '-', linewidth = 1.00)
        # plt.plot(*zip(*itertools.chain.from_iterable(itertools.combinations(tuples, 2))), color = 'blue',marker = 'o', linewidth = 2.00)
        plt.show()

        return ("Success! Took", str(counter+1), "tries")
