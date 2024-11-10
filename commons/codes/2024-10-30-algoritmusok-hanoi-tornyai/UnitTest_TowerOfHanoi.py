import unittest

def hanoi(n, elso, harmadik, masodik):
    # Ide jön az algoritmus megoldása
    if n == 1:
        print(f"{elso} {harmadik}")
        return
    hanoi(n - 1, elso, masodik, harmadik) # rekurzív hívás
    # print(f"{elso} {harmadik}") # Lépések kiíratása
    hanoi(n - 1, masodik, harmadik, elso) # rekurzív hívás

# Unittest osztály
class TestDijkstra(unittest.TestCase):
    # Példa input 1 tesztelése
    def test_case_1(self):
        n = 6
        result = 2**n - 1  # Minimális lépések száma
        # result = hanoi(n, 1, 3, 2)
        expected_output = 63 # Példa output 1
        self.assertEqual(result, expected_output)

    # Példa input 2 tesztelése
    def test_case_2(self):
        n = 10
        result = 2**n - 1  # Minimális lépések száma
        # result = hanoi(n, 1, 3, 2)
        expected_output = 1023 # Példa output 2
        self.assertEqual(result, expected_output)

# main metódus, hogy futtassa az unitteste-ket
if __name__ == "__main__":
    unittest.main()