# Converts a given json file into a csv file.
import json, csv

_json = json.loads(open('data/example.json', 'r').read())
out = open('data/converted.csv', 'w')
[out.write(','.join([x[x.keys()[i]] for i in range(len(x))]) + '\n') for x in _json]
