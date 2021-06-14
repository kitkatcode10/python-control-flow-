# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


# triangle_length = (input('Enter the lengths of 3 sides of a triangle like this: a: b: c:  '))


print ('Enter the lengths of 3 sides of a triangle')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a == b and b == c: 
    print(f'A triangle with sides of {a}, {b}, and {c} is a equalateral triangle')

elif a != b and b != c and a != c: 
    print(f'A triangle with sides of {a}, {b}, and {c} is a scalene triangle')

else 
    print(f'A triangle with sides of {a}, {b}, and {c} is an isosceles triangle')

    