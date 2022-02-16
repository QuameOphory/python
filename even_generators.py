"""
Generators are special function cases that returns a series of values 
"""

# a generator to generate even numbers less than 'n'
def even_generator(n):
    if n == 0: yield 0
    #raises type error if 'n' is negative
    if n < 0: raise TypeError('can"t generate negative even numbers')
    #this for loop will submit all even numbers less than 'n' to the caller function one after the other
    for i in range(n):
        if i % 2 == 0: yield i

#a generator to generate 'n' fibonacci series
def fibonacci_generator(n):
    a, b, count = 0, 1, 1
    while count <= n:
        yield b
        a, b = b, a+b
        count += 1


def main():
    #line 21 will raise the TypeError which was included in the main generator function
    for i in even_generator(-3):
        print(i, end=' ')

if __name__ == '__main__':
    # main()
    for i in fibonacci_generator(10):
        print(i, end=' ')