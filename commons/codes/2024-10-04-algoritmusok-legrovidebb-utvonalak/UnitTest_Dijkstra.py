import heapq
import unittest

def dijkstra(n, graph):
    # Ide jön az algoritmus megoldása
    
# Tesztelhető segédfüggvény a bemenet feldolgozására
def parse_input(data):
    data = data.split()  # Input feldarabolása
    n = int(data[0])  # városok száma
    m = int(data[1])  # járatok száma

    graph = [[] for _ in range(n + 1)]

    index = 2
    for _ in range(m):
        a = int(data[index])
        b = int(data[index + 1])
        c = int(data[index + 2])
        index += 3
        graph[a].append((b, c))

    return n, graph

# Unittest osztály
class TestDijkstra(unittest.TestCase):
    
    # Példa input 1 tesztelése
    def test_case_1(self):
        input_data = "3 4\n1 2 6\n1 3 2\n3 2 3\n1 3 4"
        n, graph = parse_input(input_data)
        result = dijkstra(n, graph)
        expected_output = [0, 5, 2]  # Példa output 1
        self.assertEqual(result, expected_output)

    # Példa input 2 tesztelése
    def test_case_2(self):
        input_data = "3 4\n1 2 4\n1 3 2\n3 2 3\n1 3 4"
        n, graph = parse_input(input_data)
        result = dijkstra(n, graph)
        expected_output = [0, 4, 2]  # Példa output 2
        self.assertEqual(result, expected_output)

# main metódus, hogy futtassa az unitteste-ket
if __name__ == "__main__":
    unittest.main()