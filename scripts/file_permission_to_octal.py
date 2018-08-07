def file_permission_to_octal(perm):
    return ''.join([{'r--': '4', 'rw-': '6', 'r-x':'5', 'rwx':'7'}[x] for x in [perm[i:i+3] for i in range(0, len(perm), 3)]])


def test_file_permission_to_octal():
    assert file_permission_to_octal('rwxrw-r--') == '764'
