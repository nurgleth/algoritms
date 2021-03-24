# прбоежаться по списку картежей
A = [(1, 5), (2, 3), (0, 0)]
for x, y in A:
    print(x, y)

s = "Hello"
print(s.find("lo"))
print(s.count("l"))

q = "AAAAAA"
q.replace("AAAA", "bbb") # строка неизменяемы тип
t = q.replace("AAAA", "bbb")
print(q)
print(t)
print(t[::-1])  # срезы строк и масссивов создают новые объекты, старые все еще существуют
print(t)

s = "qwerty"
s = s[::2] +s[::-2]
print(s)

D = [0,1,2,3,4]
D[0:3] = [10,20,30]
print(D)
D[0:3]= [0]
print(D)
f = "иванов иван иванович"
G = f.split()
print(G)
print(G[0].upper())
H = "-".join(G) # метод строки join
print(H)