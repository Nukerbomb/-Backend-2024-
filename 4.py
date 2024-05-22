def binsearch(spisok,elem):
    spisok = sorted(spisok)
    low = 0
    high = len(spisok)
    mid = 0
    while True:
        mid = (low+high)/2
        if spisok[int(mid)] == elem:
            return int(mid)
        elif spisok[int(mid)]<elem:
            low = mid+1
        if spisok[int(mid)]>elem:
            high = mid-1
        if low == high:
            return -1
elem = 24
spisok = [12,24,32,39,45,50,54]
print(binsearch(spisok,elem))