from utils import saveKeys, loadKeys, gcd, modinv
import random
import os
import hashlib


class Elgamal:
    def __init__(self, p, a):
        self.p = p
        self.a = a
        self.X = self.privateKey()['X']
        self.Y = self.pubicKey()['Y']

    def privateKey(self, replace: bool = False):
        private_Key = {}
        if replace:
            private_Key['X'] = self.X = random.randint(1, self.p - 1)
            saveKeys(private_Key, filename='privateKey.txt')
        elif os.path.isfile('privateKey.txt'):
            private_Key = loadKeys(filename='privateKey.txt')
        else:
            private_Key['X'] = self.X = random.randint(1, self.p - 1)
            saveKeys(private_Key, filename='privateKey.txt')
        return private_Key  # [X]

    def pubicKey(self):
        pubic_Key = {}
        if os.path.isfile('pubicKey.txt'):
            pubic_Key = loadKeys(filename='pubicKey.txt')
        else:
            pubic_Key['p'] = self.p
            pubic_Key['a'] = self.a
            pubic_Key['Y'] = self.Y = pow(self.a, self.X, self.p)
            saveKeys(pubic_Key, filename='pubicKey.txt')
        return pubic_Key  # [p, a, y]

    def __encode_md5(self, message):
        message_md5 = hashlib.md5(message.encode()).hexdigest()
        return int(message_md5, 16)

    def signing(self, message):
        m = self.__encode_md5(message)
        self.K = random.randint(1, self.p - 1)
        while gcd(self.K, self.p - 1) != 1:
            self.K = random.randint(1, self.p - 1)

        s1 = pow(self.a, self.K, self.p)
        s2 = modinv(self.K, self.p - 1) * (m - self.X * s1) % (self.p - 1)
        return s1, s2, self.K

    def verifying(self, s1, s2, message):
        m = self.__encode_md5(message)
        v1 = pow(self.a, m, self.p)
        v2 = (pow(self.Y, s1, self.p) * pow(s1, s2, self.p)) % self.p
        valid = v1 == v2
        return v1, v2, valid


# if __name__ == "__main__":
#     keys = loadKeys()
#     p, a = keys['p'], keys['a']
#     print(p)
#     print(a)
#     encryption = Elgamal(p, a)
#     private = Elgamal(p, a).privateKey()
#     print(private['X'])
#
#     # digital signature
#     message = 'hom nay toi vui qua'
#     s1, s2, k = encryption.signing(message)
#     print("s1=",s1)
#     print("s2=",s2)
#     print("k=", k)
#
#     # verify the signature
#     v1, v2, valid = encryption.verifying(s1, s2, message)
#     print(v1)
#     print(v2)
#     print('The signature is valid:', valid)
