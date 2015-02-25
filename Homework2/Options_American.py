__author__ = 'HarperMain'
import numpy as np
from scipy.stats import binom

class AmericanOption(object):

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

        CallMatrix = []
        PutMatrix = []

        for j in range(0, T):
            Call = []
            Put = []
            # jnodes = nodes-(T-j)
            for i in range(0, j):
                spot = self.strike * (u ** (j-i))* (d ** i)
                callvar = self.CallPayOff(spot, X) * binom.pmf(self.T - i, self.T, P)
                PutTvar = self.PutPayOff(spot, X) * binom.pmf(self.T - i, self.T, Pc)
                Call.append(callvar)
                Put.append(PutTvar)

            CallMatrix.append(Call)
            PutMatrix.append(Put)

        print('Loop Completed')
        print(CallMatrix)
        print(PutMatrix)

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
    AmericanOption(100, 80, .03, .25, 5, 1)
if __name__ == '__main__':
    main()