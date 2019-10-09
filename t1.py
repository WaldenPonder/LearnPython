A = 90000
L = A/2

for i in range(1, 10):
    L = (L + A / L)/2
    print(L)