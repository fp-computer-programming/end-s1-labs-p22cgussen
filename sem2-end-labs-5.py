# Charlie CCG 1/24/2022

def is_triangle(a, b, c):
    if ((a<b+c) and (b<a+c) and (c<a+b)) == True:
        return True
    else:
        return False

print(is_triangle(1, 2, 2) == True)
print(is_triangle(7, 2, 2) == False)
print(is_triangle(1, 2, 3) == False)
