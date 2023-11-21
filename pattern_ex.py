#rightangle pattern
def triangle(n):
    for i in range(0, n):
        for j in range(0, i):
            print('* ', end=" ")
        print('\r')
triangle(5)


 #trangle pattern

def trianglex(n):
    x = 0
    for i in range(0, n):
        for j in range(0, x):
            print(" ", end ="")
        x+=1
        for k in range(0, n):
            print("* ", end =" ")
        n-=1
        print('\r')
trianglex(5)
#triangle
def trianglex(n):
    x = 0
    for i in range(0, n):
        for j in range(0, x):
            print("", end ="")
        x+=1
        for k in range(0, n):
            print("* ", end =" ")
        n-=1
        print('\r')
trianglex(5)

#
def trianglex(n):
    x = 0
    for i in range(0, n):
        for j in range(0, x):
            print(" ", end =" ")
        x+=1
        for k in range(0, n):
            print("*", end =" ")
        n-=1
        print('\r')
trianglex(5)
# triangle
def trianglex(n):
    x =n-1
    for i in range(1, n):
        for j in range(0, x):
            print(" ", end=" ")
        x-=1
        for k in range(0, i):
            print("*", end=" ")
        print('\r')
trianglex(6)
#
def trianglex(n):
    x =n-1
    for i in range(1, n):
        for j in range(0, x):
            print(" ", end="")
        x-=1
        for k in range(0, i):
            print("*", end=" ")
        print('\r')
trianglex(6)

#fibnoic series with patterns
def fibnoic(n):
    x = 0
    for i in range(0, n):
        lst =fiseries
        for j in range(0, x):
           print(" ", end =" ")
        x+=1
        for k in range(0, n):
            print(lst[k], end=" ")
        n = n-1
        print('\r')
def fiseries()->list:
    return [1, 1, 2, 3, 5, 8]
