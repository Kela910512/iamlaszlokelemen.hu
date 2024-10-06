---
title: Algoritmusok - Legrövidebb útvonalak
date: 2024-10-04 21:25:00
categories: [Informatikatanár MSc, Algoritmusok]
tags: [legrovidebb utvonalak, shortest tracks, dijkstra]
image: /commons/images/posts/Dijkstra_Shortest_Routes_header.jpeg
---


## Feladat
Adott `n` darab város és `m` darab repülési útvonal a városok között, de minden útvonal az első városból indul. Cél, hogy meghatározzuk az első városból minden másik városba vezető legrövidebb út hosszát úgy, hogy figyelembe vesszük az átszállásos lehetőségeket is.


## Input
Az input két részből áll: városok és járatok száma, illetve a repülési útvonalakat leíró sorok.

Az első bemeneti sorban két egész számot várunk: a városok és a járatok számát.
\
A városok számozottak: `1, 2, n`.


A repülési útvonalakat leíró sorok három egész számot tartalmaznak: indulási város, cél város és a két város között út hosszát. Minden járat egyirányú.


## Output
Írassuk ki, hogy az első városból a többi városba mennyi a legrövidebb út hossza. A kimenet első értéke az önmagához vezető legrövidebb út legyen, ami ebben az esetben mindig `0` lesz.


## Korlátozások
Futási limit: 1.00 s
\
Memória limit: 512 MB
+ $ 1 \le n \le 10^5 $
+ $1 \le m \le 2 \cdot 10^5$
+ $1 \le a,b \le n$
+ $1 \le c \le 10^9$

$$ 1 \le n \le 10^5 $$


## Példa

### Input:

```python
3 4
1 2 6
1 3 2
3 2 3
1 3 4
```


### Output:

```python
0 5 2
```

## Kiindulási kód

## Unit test