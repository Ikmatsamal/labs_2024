#1
def squares_gen(N):
    for i in range(1, N+1):
        yield i**2
N = 20
a = squares_gen(N)
for i in a:
    print(i)
#2
n = int(input())
c = (i for i in range (n))
even = (i for i in c if i%2==0)
print(*even, sep = ",")
#3
def delim(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
for num in delim(n):
    print(num)

#4
a,b = map(int,input().split())
squares = (i**2 for i in range(a,b + 1))
for i in squares:
    print(i)

#5
n = int(input())
c = (i for i in range(n,-1,-1))
print(*c)