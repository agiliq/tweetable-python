def alternate_lines_from_file(file_name):
    c = open('data/alternate.txt', 'w')
    c.write('\n'.join([x for x in open(file_name, 'r').read().split('\n')[::2]]))
    c.close()
