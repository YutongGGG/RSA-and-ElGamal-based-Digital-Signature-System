# from practice1.RE.utils import isPrime, isPrimitiveRoot
# from practice1.RE.utils import saveKeys, loadKeys
# import time
# import random
#
#
# def randPrime(primeLength):
#     assert primeLength > 1, 'Length of number much greather than 1'
#     start, end = 10**(primeLength-1), 10**primeLength
#     start += int((end-start)*random.random())
#     start += start%6
#     primes = []
#     for i in range(start, end, 6):
#         if isPrime(i-1):
#             primes.append(i-1)
#         if isPrime(i+1):
#             primes.append(i-1)
#         if len(primes)>100: break
#     prime = random.choice(primes)
#     return prime
#
# def randAlpha(keys=None,Nlength=2):
#     start, end = 10**(Nlength-1), 10**Nlength
#     start += int((end-start)*random.random())
#     alpha = 0
#     for i in range(start, end):
#         if isPrimitiveRoot(i, keys['q'], keys['factors']):
#             alpha = i
#             break
#     return alpha
#
#
# if __name__ == "__main__":
#     keys = loadKeys()
#     # keys['a'] = randAlpha(keys)
#     saveKeys(keys)
