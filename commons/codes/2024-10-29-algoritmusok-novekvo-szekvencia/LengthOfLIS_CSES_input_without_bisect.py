import sys

def LengthOfLIS(nums):
    # Bináris keresés alkalmazása
    n = len(nums)
    result = []

    # Inicializáljuk a válaszlistát a result első elemével.
    result.append(nums[0])

    for i in range(1, n):
        if nums[i] > result[-1]:
            # Ha az aktuális szám nagyobb, mint a result utolsó eleme, az azt jelenti, hogy találtunk egy hosszabb növekvő részszekvenciát.
            # Ezért az aktuális számot hozzácsatoljuk a válaszlistához.
            result.append(nums[i])
        else:
            # Ha az aktuális szám nem nagyobb, mint a válaszlista utolsó eleme, akkor bináris keresést végzünk,
            # hogy megtaláljuk a válaszlista legkisebb elemét, amely nagyobb vagy egyenlő az aktuális számnál.
            low = 0
            high = len(result) - 1
            while low < high:
                mid = low + (high - low) // 2
                if result[mid] < nums[i]:
                    low = mid + 1
                else:
                    high = mid
            # A megtalált pozícióban lévő elemet frissítjük az aktuális számmal.
            # Ezzel fenntartjuk a válaszlista rendezett sorrendjét.
            result[low] = nums[i]

    # A válaszlista hossza a leghosszabb növekvő részsorozat hosszát jelenti.
    return len(result)


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