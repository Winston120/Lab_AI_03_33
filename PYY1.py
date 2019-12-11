n = int(input())


def f(s):
    if s<1:
        return 'Error'
    if s == 1:
        return 1
    else:
        for i in range(1, s + 1):
            for j in range(1, s + 1):
                print(i * j, end=' ')
            print()
        return 'yes'


print(f(n))
