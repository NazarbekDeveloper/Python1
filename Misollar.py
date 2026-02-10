import math

# 1-misol:
'''
x = 17.421
y = 10.365 * 10**-3
z = 0.828 * 10**5
surat = (y + (x - 1)**(1/3))**(1/4)
maxraj = abs(x - y) * (math.sin(z)**2 + math.tan(z))
f = surat / maxraj

print("f = ",round(f,5))
'''
# 2-misol:
'''
x = (float)(input("x = "))
x = (int)(x*10)
d = x % 10
print("d = ",d)
'''
# 3-misol
# a)
'''
n = (int)(input("n = "))
m = (int)(input("m = "))
a = ((n % 2 == 0) and (m % 2 == 0)) or ((n % 2 != 0) and (m % 2 != 0))
print("a) shart: ",a)
'''
# b)
'''
A = input("(true/false) a = ")
a = A.lower() == "true"
B = input("(ture/false) b = ")
b = B.lower() == "true"
if a != b:
    print(True)
else:
    print(False)
'''
# c)
'''
A = input("(true/false) a = ")
a = A.lower() == "true"
B = input("(ture/false) b = ")
b = B.lower() == "true"
C = input("(ture/false) c = ")
c = C.lower() == "true"
count = (a == True) + (b == True) + (c == True)
if count == 1:
    print(True)
else:
    print(False)
'''

# 4-misol

a = 1.5
x = float(input("x = "))
if x < -3:
    y = math.tan(x) + math.sqrt(math.log(abs(a - 3)))
elif -3 <= x and x <= 3:
    y = (a**2 - 3)**2 - math.sin(2*x)
else:
    y = (a + 3) - math.cos(math.pi * x)
print("y = ",y)




