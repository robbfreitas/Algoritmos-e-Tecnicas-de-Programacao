def soma (L):
    total = 0
    for e in L:
        total += e
    return total
def media (L):
    return (soma(L) / len (L))

L = [3,4,8]
print(media(L))
