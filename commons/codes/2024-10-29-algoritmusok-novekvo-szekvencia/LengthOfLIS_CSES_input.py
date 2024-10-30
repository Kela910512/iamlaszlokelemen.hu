import sys
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


# Tesztelhető segédfüggvény a bemenet feldolgozására
def parse_input(data):
    data = data.split()  # Input feldarabolása
    n = int(data[0])  # Tömb mérete
    arr = list(map(int, data[1:]))  # Az összes többi szám feldolgozása listába
    return arr

def main():
    input_data = sys.stdin.read() # Bemenet beolvasása teljes szövegként
    arr = parse_input(input_data) # A beolvasott szöveg feldolgozása listává
    result = LengthOfLIS(arr) # Leghosszabb növekvő részszekvencia hossza
    print(result) # Eredmény kiírása

if __name__ == "__main__":
    main()