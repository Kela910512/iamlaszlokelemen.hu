import unittest

def LongestPlaylist(n, songs):
    seen = set()  # Halmaz az aktuális dalok követésére
    left = 0  # Csúszóablak bal oldala
    max_length = 0  # Leghosszabb részlista hossza
    
    for right in range(n):  # Csúszóablak jobb oldala
        while songs[right] in seen:
            seen.remove(songs[left])
            left += 1  # Mozgassuk a bal oldalt
        seen.add(songs[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

def parse_input(data):
    data = data.split("\n")  # Input feldarabolása
    n = int(data[0])  # Dalok száma
    songs = list(map(int, data[1].split()))  # Dalok egyedi azonosítói

    return n, songs
    
# Unittest osztály
class TestLongestPlaylist(unittest.TestCase):
    
    # Példa input 1 tesztelése
    def test_case_1(self):
        input_data = "10\n2 2 1 1 2 1 2 1 2 1"
        n, songs = parse_input(input_data)
        result = LongestPlaylist(n, songs)
        expected_output = 2  # Példa output 1
        self.assertEqual(result, expected_output)

    # Példa input 2 tesztelése
    def test_case_2(self):
        input_data = "10\n45 9 37 81 69 99 49 71 90 30"
        n, songs = parse_input(input_data)
        result = LongestPlaylist(n, songs)
        expected_output = 10  # Példa output 2
        self.assertEqual(result, expected_output)

# main metódus, hogy futtassa az unitteste-ket
if __name__ == "__main__":
    unittest.main()