_input=input('Enter file permissions: ')
print(''.join([{'r--': '4', 'rw-': '6', 'r-x':'5', 'rwx':'7'}[x] for x in [_input[i:i+3] for i in range(0, len(_input), 3)]]))
