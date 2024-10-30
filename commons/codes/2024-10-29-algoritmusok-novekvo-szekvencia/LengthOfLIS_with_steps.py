import bisect

def LengthOfLIS(arr):
    lis = []  # Ez tárolja a lehetséges növekvő részszekvenciák legkisebb záró elemeit.
    
    # A `trace` listában tároljuk a `lis` lista állapotát minden lépés után
    trace = []
    
    for num in arr:
        pos = bisect.bisect_left(lis, num)  # Megkeressük a helyet, ahova `num` illeszkedik a lis-ben
        
        if pos == len(lis):
            lis.append(num)  # Ha a lista végén van, hozzáadjuk
        else:
            lis[pos] = num  # Ellenkező esetben kicseréljük a megfelelő helyen
            
        # A `lis` aktuális állapotát elmentjük
        trace.append(list(lis))
    
    # Visszaadjuk a leghosszabb részszekvencia hosszát és a lista állapotainak összes változatát
    return len(lis), trace

# Példa bemenet:
n = 8
arr = [7, 3, 5, 3, 6, 2, 9, 8]

# Számoljuk ki a hosszt és az állapotok nyomkövetését
length, trace = LengthOfLIS(arr)

# Kiírjuk a végrehajtott lépéseket
for step, state in enumerate(trace):
    print(f"Lépés {step + 1}: {state}")

print(f"Leghosszabb növekvő részszekvencia hossza: {length}")
