def print_pattern(m, n):

    for i in range(m):
        
        print("*" * n)

print("--- Print m x n pattern ---")
m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

print("\nResult:")
print_pattern(m, n)