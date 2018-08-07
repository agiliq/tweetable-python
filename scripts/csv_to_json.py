# Converts a csv file to JSON
import csv,json

def csv_to_json(input_csv):
    reader = csv.DictReader(open(input_csv, 'r'), fieldnames=("User","Country","Age"))
    out=open('data/out.json','w'); out.write(json.dumps([row for row in reader]))

def test_csv_to_json():
    csv_to_json('data/example.csv')
    with open('data/out.json') as f:
        j = json.loads(f.read())
        assert list(j[0].keys()) == ['User','Country','Age']
