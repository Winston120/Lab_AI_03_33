n = float(input('enter n = '))


def nat(i):
    if i == 1:
        return 'true'
    if i<1:
        return 'false'
    else:
        return nat(i-1)


print(nat(n))
