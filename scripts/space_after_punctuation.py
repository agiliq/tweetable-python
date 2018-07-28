# Formats text by adding a space after punctuations marks
import re, string;

def repl(*args): obj = args[0]; return obj.string[obj.start()] + ' ' + obj.string[obj.start() + 1]

re.sub('[' + string.punctuation + '][a-zA-Z0-9]+', repl, "this'will;be.formatted,with! spaces")
