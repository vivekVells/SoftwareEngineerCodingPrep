cast = ["Vettaikaran", 2002, "Enthiran2", 2017]
print(cast)

def fibN(n):
    a,b = 0,1

    while a<n:
        print(a, end= '  ')
        a, b = b, a+b
fibN(5);


x = [0]
print(x)
def appendL(li):
    li.append(1)
appendL(x)
print(x)

def foo(x):
    x = 'another value'
    print(x)

bar = 'some value'
foo(bar)

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    #return result

f100 = fib2(100)    # call it
print(f100)                # write the resul

if True:
    def ask_ok(prompt, retries=4, reminder='Please try again!'):
        while True:
            ok = input(prompt)
            if ok in ('y', 'ye', 'yes'):
                return True
            if ok in ('n', 'no', 'nop', 'nope'):
                return False
            retries = retries - 1
            if retries < 0:
                raise ValueError('invalid user response')
            print(reminder)
    ask_ok('Do you really want to quit?')
    ask_ok('OK to overwrite the file?', 2)
    ask_ok('OKto overwrite the file?', 2, 'Come on, only yes or no!')


def callMe(a, mutableList = []):
    mutableList.append(a)

    return a
a = 10
print(callMe(a))