def return_character_count(_file):
    count = sum([len(each) for each in open(_file, 'rb') if not each.startswith(b'#') and len(each) <= 280])
    return _file if count <= 280 else None


print([return_character_count(each) for each in os.listdir() if each.endswith('.py')])
