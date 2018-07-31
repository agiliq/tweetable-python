search_text=input('Enter text to search:  ')
print([x for x in open('data/100west.txt', 'r').read().split('\n') if search_text.lower() in x.lower()])
