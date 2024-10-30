import bisect
import unittest

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

# Unittest osztály
class TestLongestIncreasingSubsequence(unittest.TestCase):
    
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