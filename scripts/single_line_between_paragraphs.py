# Remove multiple new lines between paragraphs
import re

out = open('data/out-single-line-gap.txt', 'w')
out.write((re.sub('(\n\n)[\n]*', '\n\n', open('data/test.txt', 'r').read())))
