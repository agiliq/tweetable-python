ch = "█"

def bar(series):
    mn, mx = min(series), max(series)
    interval = (mx - mn) // 8
    bucketed = [(el - mn) // interval for el in series]
    return "\n".join(
        [f"{n} {b}" for n, b in zip(series, [ch * (el + 1) for el in bucketed])]
    )
