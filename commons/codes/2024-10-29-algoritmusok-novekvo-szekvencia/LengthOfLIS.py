import bisect

def LengthOfLIS(arr):
    # Ez a lista tárolja a különböző hosszúságú növekvő részszekvenciák legkisebb záró elemeit
    lis = []
    
    for num in arr:
        # Megkeressük azt a helyet, ahova a 'num' illeszkedik a lis listában
        pos = bisect.bisect_left(lis, num)
        
        # Ha a pozíció a lista végén van, hozzáadjuk a számot, mert ez növeli a részszekvenciát
        if pos == len(lis):
            lis.append(num)
        else:
            # Ellenkező esetben kicseréljük a meglévő elemet erre az új számra
            lis[pos] = num
    
    # A lis hossza lesz a leghosszabb növekvő részszekvencia hossza
    return len(lis)

# Példa a használatra:
n = 8
arr = [7, 3, 5, 3, 6, 2, 9, 8]

# A leghosszabb növekvő részszekvencia hossza
result = LengthOfLIS(arr)
print(result)