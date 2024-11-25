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

def main():
    n = int(input()) # Dalok száma
    songs = list(map(int, input().split())) # Dalok egyedi azonosítói
    max_length = LongestPlaylist(n, songs)
    print(max_length)
    
if __name__ == "__main__":
    main()
