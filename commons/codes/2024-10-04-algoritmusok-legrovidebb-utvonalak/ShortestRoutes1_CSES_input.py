'''
VÁROSOK ÉS JÁRATOK
'X' VÁROSBÓL 'Y' VÁROSBA 'Z' HOSSZÚ AZ ÚT

PÉLDA INPUT 1:
3 4
1 2 6
1 3 2
3 2 3
1 3 4

PÉLDA OUTPUT 1:
0 5 2

PÉLDA INPUT 2:
3 4
1 2 4
1 3 2
3 2 3
1 3 4

PÉLDA OUTPUT 2:
0 4 2

'''

import heapq # A prioritási sorok kezelése (min-heap)
import sys

def dijkstra(n, graph): # n -> városok száma | graph -> városok és járatok listája
    # Távolságok kezdetben végtelenek
    distances = [float('inf')] * (n + 1)
    distances[1] = 0  # A kezdő város (1-es) távolsága 0
    priority_queue = [(0, 1)]  # (távolság, város) -> 0 távolság a kezdő városra

    # Addig fut, amíg van elem a prioritási sorban
    while priority_queue:
        # A prioritási sor (min-heap) legkisebb elemének visszaadása és törlése a sorból
        current_distance, u = heapq.heappop(priority_queue)
        
        # Ha a jelenlegi távolság nagyobb, mint a tárolt távolság, kihagyjuk
        if current_distance > distances[u]:
            continue # jöhet a következő elem

        # Szomszédok feldolgozása -> Iterálunk a jelenlegi város (u) szomszédain, ahol 'v' a szomszédos város és 'hossz' a köztük lévő járat hossza
        for v, hossz in graph[u]:
            distance = current_distance + hossz # A kezdő városból (1) a szomszédos városba (v) vezető új távolság
            # Ha rövidebb utat találtunk v-hez, frissítjük és betesszük a prioritási sorba
            if distance < distances[v]:
                # Távolság frissítése
                distances[v] = distance
                # Hozzáadjuk a prioritási sorhoz
                heapq.heappush(priority_queue, (distance, v))

    return distances[1:]
    # Távolságok az összes városra, kivéve 1. ami = INF => 6. sor: distances = [float('inf')] * (n + 1)
        # Példa result => distances lista: [inf, 0, 5, 2]
            # inf: Nincs 0. város => csak helykitöltés => 6. sor: distances = [float('inf')] * (n + 1)
            # 0 egység: A 1-es városból önmagába
            # 5 egység: A 1-es városból a 2-es városba (a legrövidebb út: 1 → 3 → 2 útvonalon, ami 2 + 3 = 5 egység)
            # 2 egység: A 1-es városból a 3-as városba (1 → 3 => 2 vagy 4 egység => legrövidebb út: 2 egység)

def main():
    input = sys.stdin.read # Input
    data = input().split() # Input feldarabolása

    n = int(data[0]) # városok száma
    m = int(data[1]) # járatok járatok száma
    
    # üres szomszédsági lista minden város számára, ciklusváltozóra nincs szükség ('_')
    graph = [[] for _ in range(n + 1)]
    
    index = 2 # data[0] és data[1] már foglalt (városok és járatok), innen kezdjük a kiolvasást
    # frissítjük a gráfot az egyes járatok információival
    for _ in range(m):
        a = int(data[index])
        b = int(data[index + 1])
        c = int(data[index + 2])
        index += 3
        graph[a].append((b, c))
    
    distances = dijkstra(n, graph)
    
    print(' '.join(map(str, distances)))

if __name__ == "__main__":
    main()
