

# Inputs

n = int(input ('Number of points: '))

x = []
y = []

print()
print ('Coordinates for the points ...')
print()

for i in range(n):
    a = float (input(f'X {i + 1}: '))
    b = float (input(f'Y {i + 1}: '))
    
    x.append(a)
    y.append(b)

print()



# points and coordinates

print(f'{"Point":10} {"x":11} {"y":10}')
print('-' * 40)    

for i in range(n):
    print(f'{i+1} {x[i]:11} {y[i]:11}')


# Geometric charactristics calculations

print()
print('Geometric Characteristics:')
print()

Ax = 0
for i in range(n):
    a = x[i] + x[i-1]
    b = y[i] - y[i-1]
    m = a * b
    Ax = 0.5 * (Ax + m)

print (f'{"Ax:":6} {Ax:15.2f}')

Sx = 0
for i in range(n):
    a = x[i] - x[i-1]
    b = y[i]**2 + y[i] * y[i-1] + y[i-1]**2
    m = a * b
    Sx = -(1/6)*(Sx + m)

print(f'{"Sx:":6} {Sx:15.2f}')

Sy = 0
for i in range(n):
    a = y[i] - y[i-1]
    b = x[i]**2 + x[i] * x[i-1] + x[i-1]**2
    m = a * b
    Sy = (1/6) * (Sy + m)

print(f'{"Sy:":6} {Sy:15.2f}')


Ix = 0
for i in range(n):
    a = x[i] - x[i-1]
    b = y[i]**3 + (y[i]**2) * y[i-1] + y[i] * (y[i-1]**2) + y[i-1]**3
    m = a * b
    Ix = -(1/12) * (Ix + m)
    
print(f'{"Ix:":6} {Ix:15.2f}')

Iy = 0
for i in range(n):
    a = y[i] - y[i-1]
    b = x[i]**3 + (x[i]**2) * x[i-1] + x[i] * (x[i-1]**2) + x[i-1]**3
    m = a * b
    Iy = (1/12) * (Iy + m)
    
print(f'{"Iy:":6} {Iy:15.2f}')

Ixy = 0
for i in range(n):
    a = y[i] - y[i-1]
    b = (y[i] * (3 * x[i]**2 + 2 * x[i] * x[i-1] + x[i-1]**2)) + y[i-1] * (3 * x[i-1]**2 + 2 * x[i] * x[i-1] + x[i]**2)
    m = a * b
    Ixy = -(1/24) * (Ixy + m)

print(f'{"Ixy:":6} {Ixy:15.2f}')

xt = Sy / Ax
print(f'{"xt:":6} {xt:15.2f}')

yt = Sx / Ax
print(f'{"yt:":6} {yt:15.2f}')

Ixt = Ix - (yt**2) * Ax
print(f'{"Ixt:":6} {Ixt:15.2f}')

Iyt = Iy - (xt**2) * Ax
print(f'{"Iyt:":6} {Iyt:15.2f}')

Ixyt = Ixy + xt * yt * Ax
print(f'{"Ixyt:":6} {Ixyt:15.2f}')