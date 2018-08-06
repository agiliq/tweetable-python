vwls = set('aeiou')

def pig(wd):
    if len(wd) < 2 or len(vwls & set(wd)) == 0:
        return f"{wd}way"
    elif wd[0] in vwls:
        return f"{wd}ay"
    else:
        x = min(wd.find(v) for v in vwls if v in wd);return f"{wd[x:]}{wd[:x]}way"


def pig_ltn(txt): return " ".join(pig(e) for e in txt.lower().split())
