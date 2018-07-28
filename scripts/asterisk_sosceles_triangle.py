# Generates an Isosceles triangle
'\n'.join([ (11-x)*' '+ ''.join(['* ' for _ in range(x)]) for x in range(1,11, 2)])