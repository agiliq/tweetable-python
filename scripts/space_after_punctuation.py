# Formats text by adding a space after punctuations marks
import re, string

def space_after_punctuation(txt):
    def repl(*args):
        obj = args[0]
        print(obj.__dir__())
        return obj.string[obj.start()] + ' ' + obj.string[obj.start()+1: obj.end()]

    return re.sub('[' + string.punctuation + '][a-zA-Z0-9]+', repl, txt)


def test_space_after_punctuation():
    assert space_after_punctuation("this'will;be.formatted,with! spaces") == "this' will; be. formatted, with! spaces"
