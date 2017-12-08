import numpy as np
# My solutions to homework from Digital Audio Processing Coursera class
# These functions are used by other functions in this repo

def genComplexSine(k, N):
    """
    Inputs:
        k (integer) = frequency index of the complex sinusoid of the DFT
        N (integer) = length of complex sinusoid in samples
    Output:
        The function should return a numpy array
        cSine (numpy array) = The generated complex sinusoid (length N)
    """
    ## Your code here
    cSine = np.array([])
    n = np.arange(N)
    cSine = np.exp(-2j * np.pi * k * n / N)

    return cSine

def DFT(x):
    """
    Input:
        x (numpy array) = input sequence of length N
    Output:
        The function should return a numpy array of length N
        X (numpy array) = The N point DFT of the input sequence x
    """
    ## Your code here
    N = x.size
    X = np.array([])

    for k in range (0,N):
        s = sum(x * genComplexSine(k,N))
        X = np.append(X, s)
        
    return X
    
def IDFT(X):
    """
    Input:
        X (numpy array) = frequency spectrum (length N)
    Output:
        The function should return a numpy array of length N 
        x (numpy array) = The N point IDFT of the frequency spectrum X
    """
    ## Your code here
    N = X.size
    x = np.array([])

    for k in range (0,N):
        s = (1.0/N)*sum(X * np.conjugate(genComplexSine(k,N)))
        x = np.append(x, s)
        
    return x