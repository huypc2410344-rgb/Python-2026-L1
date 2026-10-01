# ==== Ex 1 ====
a = 10
area = 3.14 * (a**2)
print('area of a cirle is', area)

# ==== Ex 2 ====
C = 10
F = (C * 1.8) + 32
print('the temperature in Fahrenheit is', F)

# ==== Ex 3 ====
n = int(input('Nhap n: '))
is_prime = True

if n<= 1:
    is_prime = False
else:
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break;
if is_prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is NOT prime number")

# ==== Ex 4 ====
n = int(input('Nhap n: '))
divisor_sum = 0
for i in range(1,n):
    if n % i == 0:
        divisor_sum += i
if divisor_sum == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is NOT perfect number")
    
# ==== Ex 5 ====
fav = ["orange", "blue", "green", "white"]
color = input('What is your favorite color?')

for i in range (len(fav)):
    if color == fav[i]:
        print(f"Your colod is at index {i} in my list")
        break
else:
    print(f"Sorry, I could not find your color")
    
# ==== Ex 6 ====
range1 = range(0,7)
print([ i for i in range1])
range2 = range(1, 13, 3)
print([ i for i in range2])
range3 = range(5, 0, -1)
print([ i for i in range3])
range4 = range(6, -4, -2)
print([ i for i in range4])

# ==== Ex 7 ====
def remove_dollar_sign(s):
    return s.replace("$", "")

text_input = input("Enter a string with dollar signs: ")
result = remove_dollar_sign(text_input)
print(f"Result: {result}")
# ==== Ex 8 ====
def extract_even(l):
    result = [] #list rỗng để chứa các số chắn tìm được
    for x in l:
        if x % 2 == 0:
            result.append(x) #nếu chẵn thêm vào result
    return result            #trả về list mới
print(extract_even([1,2,5,-1,4,10]))

# ==== Ex 9 ====
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(5))

# ==== Ex 10 ====
def get_divisors(n):
    out = []
    for i in range(1, n+1):
        if n % i == 0:
            out += [i]
    return out
print(get_divisors(100))

# ==== Ex 11 ====
import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance between the points:", distance)

# ==== Ex 12 ====
m = int(input("Input m rows "))
n = int(input("Input n columns "))
for i in range(m):
    s = "" # for one line
    for j in range(n):
        if i == 0 or i == m-1 or j == 0 or j == n-1:
            s += "* "
        else:
            s += "  "
    print(s)

         
        
        




    
