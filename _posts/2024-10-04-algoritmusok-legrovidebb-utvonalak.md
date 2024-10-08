---
title: Algoritmusok - Legrövidebb útvonalak
date: 2024-10-04 21:25:00
categories: [Informatikatanár MSc, Algoritmusok, Python]
tags: [legrovidebb utvonalak, shortest tracks, dijkstra]
image: /commons/images/posts/2024-10-04-algoritmusok-legrovidebb-utvonalak/Dijkstra_Shortest_Routes_header.jpeg
pin: true
math: true
graph: true
---

A Dijkstra-algoritmus egy hatékony módszer a legrövidebb útvonalak megtalálására egy súlyozott gráfban, ahol az élek nem negatív súlyúak. Edsger W. Dijkstra 1956-ban fejlesztette ki, és azóta széles körben alkalmazzák hálózati tervezésben, útvonaltervezésben és más optimalizálási feladatokban. Az algoritmus prioritási sort használ a csúcsok feldolgozásához, biztosítva, hogy a legrövidebb útvonalakat találja meg a kiindulási ponttól a célpontokig.

---

### Gráf típusok

A Dijkstra algoritmus működését két fajta gráf típussal tudjuk modellezni és vizsgálni:
+ Irányítatlan súlyozott (weighted undirected)
+ Irányított súlyozott (weighted directed)

Mindkét gráf típus esetében a Dijkstra algoritmus hatékonyan találja meg a legrövidebb utat, feltéve, hogy nincsenek negatív élhosszak. Ha negatív élhosszak is előfordulnak, akkor a Dijkstra algoritmus nem biztosít helyes eredményt, és más algoritmusokra van szükség, például a Bellman-Ford algoritmusra.

## Irányítatlan súlyozott gráf

Ebben a típusban a gráf élei irányítatlanok, vagyis minden él kétirányú. Ha van egy él, amely összeköt két csúcsot, az mindkét irányban használható.
A súlyok jellemzően azt mutatják meg, hogy milyen „költséggel” lehet átjutni egyik csúcsról a másikra.
A Dijkstra algoritmus működhet ilyen gráfok esetén is, az élek kétirányúsága miatt mindkét irányban figyelembe veszi a költséget.

![Desktop View](/commons/images/posts/2024-10-04-algoritmusok-legrovidebb-utvonalak/weighted_undirected_dijkstra.png)
_Irányítatlan súlyozott gráf_
> Az fenti képen látható irányítatlan gráfban $7$ város található és mindegyik város között jelezve van, hogy mennyi az utazási idő (költség).
{: .prompt-info }
> Célunk meghatározni a legrövidebb útvonalat a $0$ és $6$ városok között.
{: .prompt-tip }

### Lehetséges útvonalak
A $6$-os városba az alábbi városok érintésével juthatunk el:

|Útvonal$$_n$$| Útvonal              | Költség számítás      | $$\sum_{költség}$$   |
|:---:|:----------------------------:|:---------------------:|:--------------------:|
| 1   | $0 → 1 → 3 → 5 → 6$          | 2 + 5 + 15 + 6        |  28                  |
| 2   | $0 → 1 → 3 → 5 → 4 → 6$      | 2 + 5 + 15 + 6 + 2    |  30                  |
| 3   | $0 → 1 → 3 → 4 → 6$          | 2 + 5 + 10 + 2        |  19*                 |
| 4   | $0 → 1 → 3 → 4 → 5 → 6$      | 2 + 5 + 10 + 6 + 6    |  29                  |
| 5   | $0 → 2 → 3 → 5 → 6$          | 6 + 8 + 15 + 6        |  35                  |
| 6   | $0 → 2 → 3 → 5 → 4 → 6$      | 6 + 8 + 15 + 6 + 2    |  37                  |
| 7   | $0 → 2 → 3 → 4 → 6$          | 6 + 8 + 10 + 2        |  26                  |
| 8   | $0 → 2 → 3 → 4 → 5 → 6$      | 6 + 8 + 10 + 6 + 6    |  36                  |
|     |                              |                       | $$min_{költség}=$$19 |

## Irányított súlyozott gráf

Ebben a gráfban az élek irányítottak, vagyis minden élnek van egy meghatározott iránya. Ha van egy él a → b, akkor ez az él csak a-ból b-be használható, fordított irányban nem.
A Dijkstra algoritmus működik ilyen gráfokon is, figyelembe véve az élek irányát és súlyát. Csak olyan útvonalakat keres, amelyek az él irányával megegyezően haladnak.

![Desktop View](/commons/images/posts/2024-10-04-algoritmusok-legrovidebb-utvonalak/weighted_directed_dijkstra.png)
_Irányított súlyozott gráf_
> Az fenti képen látható irányított gráfban szintén $7$ város található és mindegyik város között jelezve van, hogy mennyi az utazási idő (költség), ugyanakkor adott városból csak a megengedett irányba / irányokba haladhatunk tovább, amelyeket a nyíl iránya jelez.
{: .prompt-info }
> Célunk meghatározni a legrövidebb útvonalat a $0$ és $6$ városok között.
{: .prompt-tip }

### Lehetséges útvonalak
A $6$-os városba az alábbi városok érintésével juthatunk el:

|Útvonal$$_n$$| Útvonal              | Költség számítás      | $$\sum_{költség}$$   |
|:---:|:----------------------------:|:---------------------:|:--------------------:|
| 1   | $0 → 2 → 3 → 5 → 6$          | 6 + 8 + 15 + 6        |  35                  |
| 2   | $0 → 2 → 3 → 5 → 4 → 6$      | 6 + 8 + 15 + 6 + 2    |  37                  |
| 3   | $0 → 2 → 3 → 4 → 6$          | 6 + 8 + 10 + 2        |  26*                 |
|     |                              |                       | $$min_{költség}=$$26 |


## Feladat
> Adott $n$ darab város és $m$ darab repülési útvonal a városok között, de minden útvonal az első városból indul.\
> Cél, hogy meghatározzuk az első városból minden másik városba vezető legrövidebb út hosszát úgy, hogy figyelembe vesszük az átszállásos lehetőségeket is.\
> Készítsünk Python programot a városok közötti legrövidebb út hosszának meghatározására.
{: .prompt-info }

## Input
Az input két részből áll: városok és járatok száma, illetve a repülési útvonalakat leíró sorok.

Az első bemeneti sorban két egész számot várunk: a városok és a járatok számát.
\
A városok számozottak: $1, 2, n$.

A repülési útvonalakat leíró sorok három egész számot tartalmaznak: indulási város, cél város és a két város között út hosszát. Minden járat egyirányú.

#### Példa Input

```console
4 6
1 2 7
1 3 2
1 4 4
3 2 4
4 2 1
3 4 1
```

![Desktop View](/commons/images/posts/2024-10-04-algoritmusok-legrovidebb-utvonalak/weighted_directed_dijkstra_example_graph.png){: width="600" height="300" }
_Példa inputhoz tartozó irányított súlyozott gráf_


## Output
Írassuk ki, hogy az első városból a többi városba mennyi a legrövidebb út hossza. A kimenet első értéke az önmagához vezető legrövidebb út legyen, ami ebben az esetben mindig `0` lesz.

#### Példa Output

```console
0 5 2 3
```

## Korlátozások
>
Futási limit: 1.00 s\
Memória limit: 512 MB
{: .prompt-warning }

>
$ 1 \le n \le 10^5 $\
$1 \le m \le 2 \cdot 10^5$\
$1 \le a,b \le n$\
$1 \le c \le 10^9$
{: .prompt-warning }

## Kiindulási kód

## Unit test

## További tesztelési lehetőségek

## Lehetséges megoldások