# Converts a csv file to JSON
import csv,json
reader = csv.DictReader(open('data/example.csv', 'r'), fieldnames=("User","Country","Age"))
out=open('data/out.json','w'); out.write(json.dumps([row for row in reader]))
