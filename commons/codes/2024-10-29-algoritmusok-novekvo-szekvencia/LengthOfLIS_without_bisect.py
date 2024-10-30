import unittest

def LengthOfLIS(nums):
    # Bináris keresési megközelítés
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

# Unittest osztály
class TestLengthOfLIS(unittest.TestCase):
    
    # Példa input 1 tesztelése
    def test_case_1(self):
        input_data = "8 \n7 3 5 3 6 2 9 8"
        arr = parse_input(input_data)
        result = LengthOfLIS(arr)
        expected_output = 4  # Példa output 1
        self.assertEqual(result, expected_output)
        
    # Példa input 2 tesztelése
    def test_case_2(self):
        input_data = "10 \n10 8 6 7 7 3 2 8 6 3"
        arr = parse_input(input_data)
        result = LengthOfLIS(arr)
        expected_output = 3  # Példa output 2
        self.assertEqual(result, expected_output)

# main metódus, hogy futtassa az unitteste-ket
if __name__ == "__main__":
    unittest.main()
