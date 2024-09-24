from math import sqrt

"""Fonction secondaire"""


def isprime(p):
    """Ce programme cherche à voir si le nombre est premier ou pas"""
    if p <= 1:
        return False

    for i in range(2, int(sqrt(p))+ 1):
        if p % i == 0:
            return False
    return True

#### Fonction principale


def main():

    """Cette partie fait la recherche dans le cadre plus grand"""

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
