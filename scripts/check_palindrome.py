s=input('Enter a string: ')
print('{} is {} a Palindrome'.format(s, '' if s==s[::-1] else 'not'))
