# Generates a pretty format for json for more readability
import json
json.dumps([{"one": 123, "two": 455, "three": 789}], indent=4)
