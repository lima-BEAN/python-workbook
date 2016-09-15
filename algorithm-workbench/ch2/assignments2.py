## Assume the variables result w, x, y and z are all integers and that
## w = 5, x = 4, y = 8, and z = 2. What value will be stored in result after
## each of the following statements execute?
## a. result = x + y   b. result = z * 2  c. result = y / x
## d. result = y - z   e. result = w // z

w = 5
x = 4
y = 8
z = 2
result = 0

# part a  = 12
result = x + y
print(result)

# part b = 4
result = z * 2
print(result)

# part c = 2     correct answer: 2.0   *Remember / operator gives float number
result = y / x
print(result)

# part d = 6
result = y - z
print(result)

# part e = 2
result = w // z
print(result)
