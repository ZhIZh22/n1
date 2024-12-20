def f(a, b):
    return bin(int(a, 2) & int(b, 2))[2:].zfill(max(len(a), len(b)))

def g(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]


A = "101101"
B = "110011"

andr = f(A, B)
print(andr)

sumr = g(A, B)
print(sumr)
