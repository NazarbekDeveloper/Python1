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

n = (int)(input("n = "))
m = (int)(input("m = "))
a = ((n % 2 == 0) and (m % 2 == 0)) or ((n % 2 != 0) and (m % 2 != 0))
print("a) shart: ",a)

print("b) shart: ")
