---
title: Algoritmusok - Leghosszabb növekvő szekvencia hossza bináris kereséssel
date: 2024-10-29 08:15:00
categories: [Informatikatanár MSc, Algoritmusok]
tags: [novekvo szekvencia, increasing subsequence]
image: /commons/images/posts/2024-10-29-algoritmusok-novekvo-szekvencia/LengthOfLIS_header.jpeg
pin: true
math: true
graph: true
---

---

A leghosszabb növekvő szekvencia megtalálására szolgáló algoritmus egy hatékony eszköz a rendezett, folyamatosan növekvő részsorozatok azonosítására egy számokból álló sorozatban. Ez az algoritmus különösen hasznos adatelemzésben, sorozatok vizsgálatában és olyan problémák megoldásában, ahol az elemek rendezett növekedésének felismerése kulcsfontosságú.

## Feladat
> Feladatunk, hogy egy egész számokat tartalmazó tömbre megmondjuk, hány elem hosszúságú a megadható leghosszabb részszekvencia mérete.
{: .prompt-info }


![Desktop View](/commons/images/posts/2024-10-29-algoritmusok-novekvo-szekvencia/LengthOfLIS.png)
_Növekvő szekvencia algoritmus működése_

## Input
Az input két részből áll:
- A kezdeti tömbünk mérete (elemszám)
- Az egész számokat tartalmazó tömb

Az első bemeneti sorban egy egész számot várunk: tömb mérete.
\
A második sor pedig maga a tömb.

## Output
Írassuk ki, hogy hány elem hosszúságú a megadható leghosszabb részszekvencia mérete.

## Korlátozások
>
Futási limit: 1.00 s\
Memória limit: 512 MB
{: .prompt-warning }

>
$ 1 \le n \le 2 \cdot 10^5 $\
$1 \le x_{i} \le 2 \cdot 10^9 $
{: .prompt-warning }

## Példa

### Input:

```console
8
7 3 5 3 6 2 9 8
```


### Output:

```console
4
```

## Unit Test

```python
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
```

## Tesztelés (CSES)

A CSES oldalán bejelentkezést követően lehetőség van az algoritmusra írt megoldásunk futtatására és tesztelésére: <https://cses.fi/problemset/submit/1145/>

## Lehetséges megoldások

### Segédkönyvtárak (bisect) nélkül

```python
def LengthOfLIS(nums):
    # Bináris keresési megközelítés
    n = len(nums)
    result = []

    # Inicializáljuk a válaszlistát a result első elemével.
    result.append(nums[0])

    for i in range(1, n):
        if nums[i] > result[-1]:
            # Ha az aktuális szám nagyobb, mint a result utolsó eleme, az azt jelenti, hogy találtunk egy hosszabb növekvő részszekvenciát.
            # Ezért az aktuális számot hozzácsatoljuk a válaszlistához.
            result.append(nums[i])
        else:
            # Ha az aktuális szám nem nagyobb, mint a válaszlista utolsó eleme, akkor bináris keresést végzünk,
            # hogy megtaláljuk a válaszlista legkisebb elemét, amely nagyobb vagy egyenlő az aktuális számnál.
            low = 0
            high = len(result) - 1
            while low < high:
                mid = low + (high - low) // 2
                if result[mid] < nums[i]:
                    low = mid + 1
                else:
                    high = mid
            # A megtalált pozícióban lévő elemet frissítjük az aktuális számmal.
            # Ezzel fenntartjuk a válaszlista rendezett sorrendjét.
            result[low] = nums[i]

    # A válaszlista hossza a leghosszabb növekvő részsorozat hosszát jelenti.
    return len(result)
```

Ez a megoldás is jól működik bármilyen inputra alkalmazva, ugyanakkor nagyobb méretű inputok esetében már lassulást vélhetünk felfedezni a futási időkben. A CSES-en futtatva a kódot láthatjuk, hogy minden tesztesetre sikeresen lefut, de néhány nagyobb input esetén a futási idő több lesz, mint a `bisect` könyvtár implementálásával megírt megoldás.\
Az alábbi megoldással már javul a kódunk futási ideje, amelyet a `bisect` könyvtár használatával értünk el.

### A bisect könyvtár használatával

```python
import bisect

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
```

## CSES teszt eredmények

![Desktop View](/commons/images/posts/2024-10-29-algoritmusok-novekvo-szekvencia/CSES_result_1.png){: width="150" height="196"}
_bisect könyvtár használata nélkül elért futási eredmények_
![Desktop View](/commons/images/posts/2024-10-29-algoritmusok-novekvo-szekvencia/CSES_result_2.png){: width="150" height="196"}
_bisect könyvtár használatával elért futási eredmények_

## Letölthető fájlok

> 
- [<i class="fa-solid fa-download fa-lg"></i>][1]&nbsp;&nbsp;&nbsp;&nbsp;UnitTest
- [<i class="fa-solid fa-download fa-lg"></i>][2]&nbsp;&nbsp;&nbsp;&nbsp;CSES input (bisect)
- [<i class="fa-solid fa-download fa-lg"></i>][3]&nbsp;&nbsp;&nbsp;&nbsp;CSES input (without bisect)
- [<i class="fa-solid fa-download fa-lg"></i>][4]&nbsp;&nbsp;&nbsp;&nbsp;Megoldás lépések kiíratásával (bisect)
- [<i class="fa-solid fa-download fa-lg"></i>][5]&nbsp;&nbsp;&nbsp;&nbsp;Megoldás + UnitTest (bisect)
- [<i class="fa-solid fa-download fa-lg"></i>][6]&nbsp;&nbsp;&nbsp;&nbsp;Megoldás + UnitTest (without bisect)
{: .prompt-tip }

[1]:{{ site.url }}/commons/codes/2024-10-29-algoritmusok-novekvo-szekvencia/UnitTest_LengthOfLIS.py
[2]:{{ site.url }}/commons/codes/2024-10-29-algoritmusok-novekvo-szekvencia/LengthOfLIS_CSES_input.py
[3]:{{ site.url }}/commons/codes/2024-10-29-algoritmusok-novekvo-szekvencia/LengthOfLIS_CSES_input_without_bisect.py
[4]:{{ site.url }}/commons/codes/2024-10-29-algoritmusok-novekvo-szekvencia/LengthOfLIS_with_steps.py
[5]:{{ site.url }}/commons/codes/2024-10-29-algoritmusok-novekvo-szekvencia/LengthOfLIS_with_unit_test.py
[6]:{{ site.url }}/commons/codes/2024-10-29-algoritmusok-novekvo-szekvencia/LengthOfLIS_with_unit_test_without_bisect.py