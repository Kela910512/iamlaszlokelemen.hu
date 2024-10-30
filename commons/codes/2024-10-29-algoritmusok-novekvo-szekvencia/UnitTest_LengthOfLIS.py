# Ha olyan megoldást használunk, amely a bisect könyvtárra épül:
# import bisect
import unittest

def LengthOfLIS(n, graph):
    # Ide jön az algoritmus megoldása
    
# Tesztelhető segédfüggvény a bemenet feldolgozására
def parse_input(data):
    data = data.split()  # Input feldarabolása
    n = int(data[0])  # Kezdeti tömbünk mérete
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