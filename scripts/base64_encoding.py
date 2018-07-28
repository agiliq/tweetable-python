# Encodes a file to base64
import base64
base64.encode(open('data/100west.txt', 'r'), open('data/encoded.txt', 'w'))
