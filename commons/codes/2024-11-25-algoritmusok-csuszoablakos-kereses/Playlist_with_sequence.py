def LongestPlaylist(n, songs):
    seen = set()  # Halmaz az aktuális dalok követésére
    left = 0  # Csúszóablak bal oldala
    max_length = 0  # Leghosszabb részlista hossza
    best_start = 0  # Leghosszabb részlista kezdő indexe

    for right in range(n):  # Csúszóablak jobb oldala
        while songs[right] in seen:
            seen.remove(songs[left])
            left += 1  # Mozgassuk a bal oldalt
        seen.add(songs[right])
        
        # Frissítsük a max hosszt és a kezdő pozíciót, ha szükséges
        if right - left + 1 > max_length:
            max_length = right - left + 1
            best_start = left

    # A leghosszabb részlista meghatározása
    best_sequence = songs[best_start:best_start + max_length]
    
    return max_length, best_sequence

def main():
    n = int(input())  # Dalok száma
    songs = list(map(int, input().split()))  # Dalok egyedi azonosítói
    max_length, best_sequence = LongestPlaylist(n, songs)
    print(max_length)
    print(" ".join(map(str, best_sequence)))  # A sorozat kiírása szóközzel elválasztva

if __name__ == "__main__":
    main()
