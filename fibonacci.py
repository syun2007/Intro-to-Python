'''
Fibonacci sequence in 20 lines or more
By Sam Yun
g**n
'''



def fibonacci():
    fib = 0
    prev_fib = 0
    for i in range(int((input("How long do you want it?")))):
        if fib == 0:
            print(fib, end=' ')
            fib += 1
            print(fib, fib, end=" ")
        prev_fib = fib - prev_fib
        fib += prev_fib
        print(fib, end=" ")


def specific_fib(num):
    result = 0
    if num == 1:
        return 0
    elif num == 2 or num == 3:
        return 1
    else:
        prev_fib = 1
        fib = 2
        for i in range(int(num) - 4):
            prev_fib = fib - prev_fib
            fib += prev_fib
        return fib

#print(specific_fib(int(input("Which one? "))))
fibonacci()

