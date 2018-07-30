spark_chars = "▁▂▃▄▅▆▇██"


def sparkline(series):
    mn, mx = min(series), max(series)
    interval = (mx - mn) // 8
    bucketed = [(el - mn) // interval for el in series]
    spark_dict = dict(zip(range(9), spark_chars))
    return "".join([spark_dict[el] for el in bucketed])
