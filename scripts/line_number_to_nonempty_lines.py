# Add line number to a file where line is not empty
out = open('data/test-out.txt', 'w')
i = 0
for line in open('data/test.txt', 'r'):
    if line.strip():
        out.write(str(i) + line);i += 1
    else:
        out.write(line)
out.close()
