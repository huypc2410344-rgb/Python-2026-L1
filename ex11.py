import math

def compute_distance(x1, y1, x2, y2):
    
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("--- Compute distance between point A and B ---")
x1 = float(input("Enter x-coordinate of point A (x1): "))
y1 = float(input("Enter y-coordinate of point A (y1): "))
x2 = float(input("Enter x-coordinate of point B (x2): "))
y2 = float(input("Enter y-coordinate of point B (y2): "))

distance = compute_distance(x1, y1, x2, y2)
print(f"The distance between the two points is: {distance}")
