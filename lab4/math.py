#1
import math
degree = float(input())
print(math.pi*degree/180)

#2
import math
height, base1, base2 = map(float,input().split())
print((base1+base2)/2*height)

#3
import math
sides, lenght = map(float, input().split())
print( (sides*lenght**2)/4*math.tan(360/sides*lenght))

#4 pallaelrogram
import math
length = float(input())
height = float(input())
print("area =", length*height)
