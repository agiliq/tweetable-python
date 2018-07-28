# Add line number to text file
out = open('data/test-out.txt', 'w')
for i, j in enumerate(open('data/test.txt', 'r')): out.write(str(i + 1) + j)
out.close()