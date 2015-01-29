__author__ = 'Mario'

def Guessengine(A):
    print(A)
    A = int(A)

    low = 0
    high = 101

    guess = [50]
    g = 0
    counter = 0
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

        guess.append(g)
        counter = counter +1
        print(guess[-1])

    if guess[-1] == A:
        print("Success! Took", counter+1, "tries")