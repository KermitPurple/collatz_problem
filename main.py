from typing import List
from matplotlib import pyplot as plt

def collatz(n: int) -> List[int]:
    if n < 1:
        raise ValueError("n cannot start less than one")
    def inner(n: int) -> 'generator':
        yield n
        if n == 1:
            return
        if n % 2: # odd
            n *= 3
            n += 1
        else: # even
            n //= 2
        yield from inner(n)
    return list(inner(n))

def irange(count: int, step: int = 1) -> range:
    return range(1, count + 1, step)

def main():
    for i in irange(500):
        plt.plot(collatz(i), '-o')
    plt.show()

if __name__ == '__main__':
    main()
