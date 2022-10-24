n = int(input('Digite primeiro numero: '))
n2 = int(input('Digite outro numero: '))
x = 1
r = 0
while x <= n2:
    r = r + n
    print(r)
    x = x + 1
print('{} x {} = {}'.format(n,n2,r))
