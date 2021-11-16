def sum_of_intervals(intervals):
    lis = []
    for i in intervals:
        for j in range(i[0], i[1]):
            if j not in lis:
                lis.append(j)
    return len(lis)
