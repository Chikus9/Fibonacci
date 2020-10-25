def fib(n):
    a = 0
    b = 1

    if n < 0:
        print('Enter a valid number')

    elif n == 1:
        print('Enter a no greater than one')

    else:

        for i in range(2,n):
            c= a+b
            if c<n:
                a = b
                b = c

                print(i)


fib(10)