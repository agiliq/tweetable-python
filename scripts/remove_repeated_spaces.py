# Remove multiple spaces from text
import re;

re.sub(r"[ ]+", ' ', 'this    sentence          has              non-uniform      spaces')
