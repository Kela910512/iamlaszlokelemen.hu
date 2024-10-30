import sys
 
def dijkstra(n, graph):
    # Távolságok kezdetben végtelenek
    distances = [float('inf')] * (n + 1)
    distances[1] = 0  # A kezdő város (1-es) távolsága 0
    visited = [False] * (n + 1)  # Jelzi, hogy meglátogattuk-e a várost

    while True:
        # Kiválasztjuk a legkisebb távolságú még nem látogatott várost
        min_distance = float('inf')
        u = -1
        for i in range(1, n + 1):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                u = i

        # Ha nem találtunk ilyen várost, akkor kész vagyunk
        if u == -1:
            break

        # Megjelöljük, hogy ezt a várost most meglátogattuk
        visited[u] = True

        # Szomszédok feldolgozása
        for v, hossz in graph[u]:
            if distances[u] + hossz < distances[v]:
                distances[v] = distances[u] + hossz

    return distances[1:]

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