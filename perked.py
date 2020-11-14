#hw1 perket.review
#author Deng Ting

if __name__ == '__main__':
    n = eval(input('please typein a positive integer: '))
    ingredients = list()
    for _ in range(n):
        ingredients.append([int(x) for x in input('please input s&b: ').split()])
    print()
    dz = 1000000000

    for a in range(1, 1 << n):
        cbitter = 0
        dsour = 1
        for b in range(n):
            h = 1<<b
            z = (1 << b) & a
            if z > 0:
                dsour *= ingredients[b][0]
                cbitter += ingredients[b][1]
                print(a,b,dsour,cbitter,dz)
        dz = min(dz,abs(dsour - cbitter))
    print(dz)
