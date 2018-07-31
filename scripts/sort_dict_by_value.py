y={1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
print(dict([i for i in sorted(y.items(), key=lambda kv: kv[1])]))
