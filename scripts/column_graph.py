ch = "█"

def col(sz):
    mn, mx = min(sz), max(sz)
    df = (mx - mn) // 8
    bkt = [(el - mn) // df for el in sz]
    hrz = [f"{b}{c}" for b, c in
           [(ch * (el + 1), " " * (8 - el)) for el in bkt]
           ]
    return "\n".join([" ".join(el) for el in list(map(list, zip(*hrz)))[::-1]])
