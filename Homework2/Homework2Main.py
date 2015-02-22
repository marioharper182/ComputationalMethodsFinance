__author__ = 'HarperMain'

import numpy as np
from numpy import random as rand
from scipy.stats import binom
from numpy import zeros

class EuropeanOption(object):
    def __init__(self, strike, X, rate, volatility, T, n):
        self.strike = strike
        self.X = X
        self.rate = rate
        self.volatility = volatility
        self.T = T
        self.n = float(n)
        h = self.T/self.n
        # self.spot = self.CalcSpot()

        u = np.exp((self.rate * h) + self.volatility * np.sqrt(h))
        d = np.exp((self.rate * h) - self.volatility * np.sqrt(h))
        nodes = self.T+1
        P = (np.exp(self.rate*h) - d) / (u - d)
        Pc = 1-P

        Call = []
        Put = []

        for i in range(0, nodes):
            spot = self.strike * (u ** (nodes-i))* (d ** i)
            callvar = self.CallPayOff(spot, X) * binom.pmf(self.T - i, self.T, P)
            PutTvar = self.PutPayOff(spot, X) * binom.pmf(self.T - i, self.T, Pc)
            Call.append(callvar)
            Put.append(PutTvar)

        self.callPrice = sum(Call) / (np.exp(self.rate*self.T))
        self.putPrice = sum(Put) / (np.exp(self.rate*self.T))



    def GetStrike(self):
        return self.strike

    def SetStrike(self, strike):
        self.strike = strike

    def GetPrice(self):
        return (self.callPrice, self.putPrice)

    def CallPayOff(self, spot, strike):
        return max(spot-strike, 0.0)

    def PutPayOff(self, spot, strike):
        return max(strike-spot, 0.0)

def main():
    EuropeanOption(100, 100, .03, .25, 5, 1)
if __name__ == '__main__':
    main()