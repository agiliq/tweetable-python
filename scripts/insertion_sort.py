def insertion_sort(data):
    for i,v in enumerate(data):
        while i>0:
            if data[i-1] > data[i]:
                data[i-1],data[i] = data[i],data[i-1]
            else:
                break
            i = i-1
    return data
