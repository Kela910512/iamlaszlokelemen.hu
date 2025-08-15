---
title: Algoritmusok - Csúszóablakos keresés
date: 2024-11-25 08:15:00
categories: [Algoritmusok, Csúszóablakos keresés]
tags: [kereso algoritmus, csuszoablakos algoritmus]
image: /commons/images/posts/2024/2024-11-25-algoritmusok-csuszoablakos-kereses/CsuszoablakosKereses_header.jpeg
pin: false
math: true
graph: true
---

---

A csúszóablakos keresés egy hatékony algoritmus, amely különösen alkalmas olyan problémák megoldására, ahol egy adott részhalmaz tulajdonságait kell nyomon követni egy folyamatosan változó intervallumon belül.

## Feladat
> Egy zenei lejátszási listán vannak dalok, amelyeket egymás után játszanak le. A cél, hogy megtaláljuk a leghosszabb, ismétlődés nélküli részlistát a dalok sorrendjében.
{: .prompt-info }

![Desktop View](/commons/images/posts/2024/2024-11-25-algoritmusok-csuszoablakos-kereses/CsuszoablakosKereses.png)
_A csúszóablakos keresési algoritmus működése_

## Input
Az első sor tartalmaz egy $n$ egész számot, amely a lejátszási lista dalainak számát adja meg.
A második sor $n$ darab egész számot tartalmaz, amelyek az egyes dalok egyedi azonosítói (1-től induló természetes számok).

## Output
Írassuk ki a leghosszabb részlista hosszát, amely nem tartalmaz ismétlődő dalokat.

## Korlátozások
>
Futási limit: 1.00 s\
Memória limit: 512 MB
{: .prompt-warning }

>
$1 \le n \le 2 \cdot 10^5$\
$1 \le k_{i} \le 10^9$
{: .prompt-warning }

## Példa

### Input

```console
8
1 2 1 3 2 7 4 2
```


### Output

```console
5
```

## Lehetséges megközelítés
Használjunk egy csúszóablakos algoritmust, amely két mutatót használ:

- bal: az aktuális részlista kezdete,
- jobb: az aktuális részlista vége (amelyet iterálunk).

Egy halmazt használunk a részlista dalainak nyilvántartására, és ha duplikációt találunk, a bal mutatót eltoljuk, amíg az ismétlődő elem ki nem kerül a részlistából.

## Miért csúszóablakos algoritmus?
Egy olyan intervallumot (részlistát) keresünk, amelynek nincs ismétlődő eleme.
Az intervallum mérete folyamatosan változik, ahogy újabb elemeket adunk hozzá, és eltávolítjuk a nem kívánt elemeket.

A csúszóablakos algoritmus a lista elemeit legfeljebb kétszer dolgozza fel (egyszer hozzáadja az ablakhoz, egyszer eltávolítja belőle).
Ezért az algoritmus időbonyolultsága $O(n)$, ami hatékony a probléma megoldását tekintve.

## Lehetséges megoldás

```python
def longest_playlist(n, songs):
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

# Input beolvasása
n = int(input())
songs = list(map(int, input().split()))

# Eredmény kiíratása
print(longest_playlist(n, songs))
```

## Unit Test

```python
import unittest

def LongestPlaylist(n, songs):
    # Ide jön az algoritmus megoldása

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
```

## Tesztelés (CSES)

A CSES oldalán bejelentkezést követően lehetőség van az algoritmusra írt megoldásunk futtatására és tesztelésére: <https://cses.fi/problemset/submit/1141/>

## CSES teszt eredmények

![Desktop View](/commons/images/posts/2024/2024-11-25-algoritmusok-csuszoablakos-kereses/CSES_result_1.png){: width="150" height="196"}
_futási eredmények_

## Letölthető fájlok

> 
- [<i class="fa-solid fa-download fa-lg"></i>][1]&nbsp;&nbsp;&nbsp;&nbsp;UnitTest
- [<i class="fa-solid fa-download fa-lg"></i>][2]&nbsp;&nbsp;&nbsp;&nbsp;CSES input
- [<i class="fa-solid fa-download fa-lg"></i>][3]&nbsp;&nbsp;&nbsp;&nbsp;Megoldás + UnitTest
- [<i class="fa-solid fa-download fa-lg"></i>][4]&nbsp;&nbsp;&nbsp;&nbsp;Megoldás leghosszabb sorozat kiíratásával
{: .prompt-tip }

[1]:{{ site.url }}/commons/codes/2024-11-25-algoritmusok-csuszoablakos-kereses/UnitTest_Playlist.py
[2]:{{ site.url }}/commons/codes/2024-11-25-algoritmusok-csuszoablakos-kereses/Playlist_CSES_input.py
[3]:{{ site.url }}/commons/codes/2024-11-25-algoritmusok-csuszoablakos-kereses/Playlist_with_unit_test.py
[4]:{{ site.url }}/commons/codes/2024-11-25-algoritmusok-csuszoablakos-kereses/Playlist_with_sequence.py