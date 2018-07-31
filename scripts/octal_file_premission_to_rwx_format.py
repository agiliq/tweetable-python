_input=input('Enter file permissions: ')
print(''.join([{'4':'r--', '6':'rw-','5':'r-x','7':'rwx'}[x] for x in str(_input)]))
