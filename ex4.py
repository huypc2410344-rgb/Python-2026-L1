num = int(input("Enter a number? "))
if num < 1:
    print(f"{num} is a NOT perfect number")
else:
    sum_divisors = sum([i for i in range(1, num) if num % i == 0])
    if sum_divisors == num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is a NOT perfect number")