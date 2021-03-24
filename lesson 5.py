a = [1, 2, 3, 4, 5]
for x in range(len(a)):
    a[x] += 1
print(a)

"""b = [0] * 1000
top = 0
x = int(input())
while x != 0:
    b[top] = x
    top += 15
    x = int(input())"""

# поэтапное копирование  или c = list(d)
n = int(input())
d = [0] * n
s = [0] * n
for i in range(n):
    d[i] = int(input())
for i in range(n):
    s[i] = d[i]

print(d)
print(s)

# инверсия массива
n = int(input())
d = [0] * n
s = [0] * n
for i in range(n):
    d[i] = int(input())
for i in range(n):
    s[i] = d[n-1-i]

print(d)
print(s)

"""
через одну переменую
def invert_array(A:list, N:int):
for i in range(n//2):
    A[i],A[N-1-i] = A[N-1-i], A[i]
"""

#циклический  сдвиг влево
g = [0,1,2,3]
tmp = g[0]
for i in range(len(g)-1):
    g[i]=g[i+1]
g[len(g)-1] = tmp

print(g)
#циклический  сдвиг вправо
g_1 = [0,1,2,3]
tmp_1 = g_1[len(g)-1]
for i in range(len(g_1)-2,-1,-1):
    g_1[i+1]=g_1[i]
g_1[0] = tmp_1

print(g_1)