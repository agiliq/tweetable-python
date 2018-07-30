# Decodes a base64 encoded file
import base64
base64.decode(open('data/encoded.txt', 'rb'), open('data/decoded.txt', 'w'))
