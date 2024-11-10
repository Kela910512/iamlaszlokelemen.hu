---
title: Algoritmusok - Hanoi Tornyai
date: 2024-10-30 08:15:00
categories: [Informatikatanár MSc, Algoritmusok, Problémamegoldás]
tags: [hanoi tornyai, tower of hanoi, hanoitower]
image: /commons/images/posts/2024-10-30-algoritmusok-hanoi-tornyai/TowerOfHanoi_header.jpeg
pin: true
math: true
graph: true
---

---

A Hanoi tornyai probléma egy híres matematikai és algoritmikai feladat, amelyet Édouard Lucas francia matematikus mutatott be 1883-ban.

## A Hanoi tornyai probléma részletes ismertetése
 A feladat kiinduló helyzetében adott egy torony, amely különböző méretű korongokból áll, és ezeket egy oszlopra helyeztük úgy, hogy a nagyobb korongok mindig a kisebb korongok alatt vannak. A cél, hogy a tornyot egy másik oszlopra helyezzük át úgy, hogy betartjuk a következő szabályokat:

- Egyszerre csak egy korongot mozgathatunk.
- Egy korongot sosem helyezhetünk egy kisebb korongra.
- A tornyot egy harmadik segédoszlop segítségével kell áthelyeznünk.

## Feladat
> Feladatunk megmondani, hogy $n$ darabszámú korong esetén mennyi a minimális korong áthelyezési lépés, illetve, hogy pontosan mi is az adott lépés. (Honnan hová helyezzük az adott korongot.)
{: .prompt-info }

![Desktop View](/commons/images/posts/2024-10-30-algoritmusok-hanoi-tornyai/TowerOfHanoi.gif){: width="50%" height="50%"}
_futási eredmények_

A Hanoi tornyai probléma elsőre egyszerűnek tűnhet, de a korongok számának növekedésével a megoldás komplexitása exponenciálisan növekszik. Ha $n$ a korongok száma, akkor az optimális megoldáshoz szükséges lépések száma: $2^n - 1$.

![Desktop View](/commons/images/posts/2024-10-30-algoritmusok-hanoi-tornyai/TowerOfHanoi.png)
_A Hanoi Tornyai feladat rekurzív algoritmusának működése_

## Input
Az input egyetlen eleme a korongok száma.

## Output
Írassuk ki, hogy hány lépésből oldható meg a feladat és pontosan mik a lépések.

## Korlátozások
>
Futási limit: 1.00 s\
Memória limit: 512 MB
{: .prompt-warning }

>
$1 \le n \le 16$
{: .prompt-warning }

## Példa

### Input:

```console
2
```


### Output:

```console
3
1 2
1 3
2 3
```

## Rekurzív megoldás

```python
# elso: 1. állvány
# masodik: 2. állvány (segéd)
# harmadik: 3. állvány

def hanoi(n, elso, harmadik, masodik):
    if n == 1:
        print(f"{elso} {harmadik}")
        return
    hanoi(n - 1, elso, masodik, harmadik) # rekurzív hívás
    print(f"{elso} {harmadik}") # Lépések kiíratása
    hanoi(n - 1, masodik, harmadik, elso) # rekurzív hívás

# Példa futtatás
while True:
    n = int(input("Add meg a korongok számát: "))
    if n <= 16 and n > 0:
        break
    print("A korongok száma min. 1 és max. 16 lehet. Próbáld újra.")

print(2**n - 1)  # Minimális lépések száma
hanoi(n, 1, 3, 2)
```

## Unit Test

Mivel a lépések számának meghatározásához adott egy képlet, így tesztelni a pontos lépések meghatározását szükséges csak. Ugyanakkor erre `unittest`-et írni csak úgy érdemes, ha például a várt eredmény egy szöveges file-ba kerül elhelyezésre és a futási eredmény ezzel kerül összehasonlításra. A CSES oldalán lévő egyszerű futtatási és ellenőrzési lehetőség miatt célszerűbb csak ott tesztelni a megírt python kódot.

## Tesztelés (CSES)

A CSES oldalán bejelentkezést követően lehetőség van az algoritmusra írt megoldásunk futtatására és tesztelésére: <https://cses.fi/problemset/submit/2165/>

## CSES teszt eredmények

![Desktop View](/commons/images/posts/2024-10-30-algoritmusok-hanoi-tornyai/CSES_result_1.png){: width="150" height="196"}
_futási eredmények_

## Letölthető fájlok

> 
- [<i class="fa-solid fa-download fa-lg"></i>][1]&nbsp;&nbsp;&nbsp;&nbsp;Hanoi Tornyai rekurzívan
- [<i class="fa-solid fa-download fa-lg"></i>][2]&nbsp;&nbsp;&nbsp;&nbsp;CSES input
{: .prompt-tip }

[1]:{{ site.url }}/commons/codes/2024-10-30-algoritmusok-hanoi-tornyai/TowerOfHanoi_recursive.py
[2]:{{ site.url }}/commons/codes/2024-10-30-algoritmusok-hanoi-tornyai/TowerOfHanoi_recursive_CSES_input.py