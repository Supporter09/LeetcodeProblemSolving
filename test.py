arr = []

def display_pascal_triangle(x):
    while(len(arr) < x+1):
        arr.append(0)
    if(x == 1):
        n = len(arr)
        arr[0] = 1
        for i in range(1, n-1, 1):
            print(' ', sep='', end='')
        print(1, sep='', end='\n')
        return
    display_pascal_triangle(x-1)
    n = len(arr)
    for i in range(x-1, 0, -1):
        arr[i] += arr[i-1]
    for i in range(1, n-x, 1):
        print(' ', sep='', end='')
    for i in range(0, x, 1):
        print(arr[i], sep='', end=' ')
    print('\n', sep='', end='')
    return

display_pascal_triangle(10)