def highestsum(lst):
    maxix = -1e100
    maxix2 = -1e100
    for i in range(len(lst)):
        if lst[i]>=maxix:
            maxix = lst[i]
    lst2 = lst
    for i in range(len(lst2)):
        if lst2[i] == maxix:
            lst2 = lst2[:i]+lst2[i+1:]
    for i in range(len(lst2)):
        if lst2[i]>=maxix2 and lst2[i]<=maxix:
            maxix2 = lst2[i]
    return maxix+maxix2
lst = [2, 7, 4, 1, 8]
print(highestsum(lst))