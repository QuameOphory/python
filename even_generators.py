from itertools import count
from re import A


def even_generator(n):
    if n == 0: yield 0
    if n < 0: raise TypeError('can"t generate negative even numbers')
    for i in range(n):
        if i % 2 == 0: yield i

def fibonacci_generator(n):
    a, b, count = 0, 1, 1
    while count <= n:
        yield a
        a, b = b, a+b
        count += 1


def main():
    for i in even_generator(-3):
        print(i, end=' ')

if __name__ == '__main__':
    # main()
    for i in fibonacci_generator(10):
        print(i)